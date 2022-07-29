import jwt
from app import db, app
from flask import jsonify, make_response, request
from . import auth
from app.auth.models import User
import datetime

@auth.route('/login', methods=['POST'])
def loginUser():
    data = request.json
    if 'email' not in data or 'password' not in data:
        return jsonify({"message": "Insufficient Credentials"}), 401

    user = User.query.filter_by(email=data['email']).first()
    if not user:
        return jsonify({"message": "User Does Not Exist"}), 401
    if user.check_password(data['password']):
        token = jwt.encode({
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")

        return jsonify({"message": "Successful Sign-In", "token": token}), 201
    return jsonify({"message": "Incorrect Password"}), 403

@auth.route('/register', methods=['POST'])
def register():
    data = request.json
    if 'email' not in data or 'password' not in data:
        return jsonify({"message": "Insufficient Credentials"}), 401
    user = User.query.filter_by(email=data['email']).first()
    if user:
        return jsonify({"message": "Email Already Registered With a User"}), 401
    try:
        u = User(email=data['email'])
        u.set_password(data['password'])
        db.session.add(u)
        db.session.commit()
        return jsonify({"message": "Successfully Registered"}), 201
    except:
        return jsonify({"message": "DataBase Error, Try Again Later"}), 401
