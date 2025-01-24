from flask import Flask, jsonify
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

@app.route('/status')
def status():
    status_var = os.getenv('MY_WEB_APP_STATUS')
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    if status_var:
        response = {
            'time': current_time,
            'status': status_var,
            'message': 'Status variable found'
        }
    else:
        response = {
            'time': current_time,
            'status': None,
            'message': 'Status variable not found'
        }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8017)