from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/info')
def get_info():
    """Реалізація ендпоінту /info"""
    return jsonify({
        'service_name': 'Service A',
        'status': 'OK',
        'message': 'Hello from Service A!'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)