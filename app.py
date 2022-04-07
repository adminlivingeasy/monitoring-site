# save this as app.py
import logging
import psutil
import os
from datetime import datetime
from flask import Flask, Response, request,jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:Ikancucut182!!@34.101.234.107:5432/account-service"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

process = psutil.Process(os.getpid())

@app.route("/")
def hello():
    return jsonify({"message": "success"})

@app.route("/ping")
def ping() -> Response:
        response = Response(response='pong', status=200, mimetype='text/plain')
        response.headers['Cache-Control'] = 'no-store, must-revalidate'
        if request.environ.get('SERVER_PROTOCOL') == 'HTTP/1.0':
            response.headers['Expires'] = 0
        return jsonify({"message": response.status})

@app.route('/memory')
def print_memory():
    return jsonify({"memory": process.memory_info().rss})

@app.route('/dbcheck')
def testdb():
    try:
        db.session.query("1").from_statement("SELECT 1").all()
        return jsonify({"message": "DB Connected"})
    except:
        return jsonify({"message": "DB Not Connected"})

@app.route('/datetime')
def datetime_print():
    date = datetime.now()
    return jsonify({"datetime": str(date)})

if __name__ == "__main__":
    app.run()