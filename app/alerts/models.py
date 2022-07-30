from app import db
from datetime import datetime
from flask import json

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
