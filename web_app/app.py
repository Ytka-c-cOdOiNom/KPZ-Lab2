import os
import psycopg2
from flask import Flask, jsonify
from time import sleep

app = Flask(__name__)

def get_db_connection():
    """Спроба підключитися до БД, доки вона не буде готова."""
    retries = 5
    while retries > 0:
        try:
          
            db_name = os.environ.get('POSTGRES_DB')
            db_user = os.environ.get('POSTGRES_USER')
            db_pass = os.environ.get('POSTGRES_PASSWORD')
            db_host = os.environ.get('DB_HOST') 

            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_pass,
                host=db_host
            )
            return conn
        except psycopg2.OperationalError as e:
            print(f"Помилка підключення до БД: {e}")
            retries -= 1
            print(f"Залишилось спроб: {retries}. Повтор через 5 сек.")
            sleep(5)
    
   
    raise Exception("Не вдалося підключитися до бази даних.")


@app.route('/users')
def get_users():
    """Реалізація ендпоінту /users """
    users_list = []
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        
     
        cur.execute("SELECT id, username FROM users;")
        users = cur.fetchall()
        
    
        for user in users:
            users_list.append({'id': user[0], 'username': user[1]})
            
        cur.close()
        conn.close()
        
        return jsonify(users_list)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)