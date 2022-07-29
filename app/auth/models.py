from app import app, db
import jwt
from flask_login import UserMixin
from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps

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

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        else:
            return jsonify({'message': "Token is Missing"}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms="HS256")
            current_user = User.query.filter_by(email=data['email']).first()
        except:
            return jsonify({'message': 'Token Is Invalid!!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
