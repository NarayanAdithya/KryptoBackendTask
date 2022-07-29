from app import app
from flask import jsonify
from app.auth.models import token_required

@app.route('/')
def home():
    return jsonify({"message": "Adithya Narayan Krypto Task"})

@app.route('/tokentest', methods=["POST", "GET"])
@token_required
def token_req(current_user):
    return jsonify({"message": f"Token Found, Successfull Login of {current_user.email}"})