import os
import psycopg2
from flask import Flask, jsonify
from flask_cors import CORS
from time import sleep

app = Flask(__name__)
CORS(app) 

def get_db_connection():
    """Підключення до БД, використовуючи мережеве ім'я контейнера."""
    retries = 5
    while retries > 0:
        try:
            db_host = "database" 
            db_name = os.environ.get('POSTGRES_DB')
            db_user = os.environ.get('POSTGRES_USER')
            db_pass = os.environ.get('POSTGRES_PASSWORD')
            
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_pass,
                host=db_host
            )
            print("--- УСПІШНЕ ПІДКЛЮЧЕННЯ ДО БД ---")
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print(f"Не вдалося підключитися до БД. Залишилось спроб: {retries}. Повтор через 5 сек.")
            sleep(5)
    
    print("--- НЕ ВДАЛОСЯ ПІДКЛЮЧИТИСЯ ДО БД ПІСЛЯ КІЛЬКОХ СПРОБ ---")
    raise Exception("Не вдалося підключитися до бази даних.")

@app.route('/api/items')
def get_items():
    """Frontend буде звертатися сюди"""
    items_list = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM items;")
        items = cur.fetchall()
        
        for item in items:
            items_list.append({'id': item[0], 'name': item[1]})
            
        cur.close()
        conn.close()
        return jsonify(items_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
