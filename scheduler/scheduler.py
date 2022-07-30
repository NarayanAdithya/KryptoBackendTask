import time
import atexit
from flask import Flask
from apscheduler.schedulers.background import BackgroundScheduler
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import requests
from collections import defaultdict
import json
import pika
from datetime import datetime
from flask_login import UserMixin
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_URI')
crypto_data = defaultdict(int)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(70), unique=True)
    password_hash = db.Column(db.String(120))
    alerts = db.relationship('Alert', backref='user')

    def set_password(self, passw):
        self.password_hash = generate_password_hash(passw)

    def check_password(self, passw):
        return check_password_hash(self.password_hash, passw)

    def __repr__(self):
        return f"<User {self.email.split('@')[0]}>"

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    target_price = db.Column(db.String(120))
    coin = db.Column(db.String(120))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.String(120))
    created = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return f"<Alert {self.user_id} {self.coin}:{self.target_price}>"

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__)


def check_entries():
    data = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    for i in json.loads(data.text):
        crypto_data[i['symbol']] = i['current_price']
    q = Alert.query.filter_by(status="CREATED").all()
    print(q)
    print(crypto_data)
    for i in q:
        if i.target_price == str(crypto_data[i.coin]):
            print(f"Send Email To {i.user.email} for coin {i.coin}")
            i.status = 'TRIGGERED'
            credentials = pika.PlainCredentials('user', 'password')
            connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
            channel = connection.channel()
            channel.queue_declare(queue='task_queue', durable=True)
            channel.basic_publish(
                exchange='',
                routing_key='task_queue',
                body=f"Mail sent to {i.user.email} for {i.coin} at amount {i.target_price}",
                properties=pika.BasicProperties(
                delivery_mode=2  # make message persistent
                )
            )
            connection.close()
            db.session.add(i)
            db.session.commit()

scheduler = BackgroundScheduler()
scheduler.add_job(func=check_entries, trigger="interval", seconds=30)
scheduler.start()


@app.route('/end')
def end():
    atexit.register(lambda: scheduler.shutdown())
    return "Process Ended"

if __name__ == '__main__':
    app.run()
