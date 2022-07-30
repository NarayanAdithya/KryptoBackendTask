from inspect import currentframe
from app.alerts import alerts
from app.alerts.models import Alert
from flask import jsonify, json, request
from app.auth.models import token_required
from app import app, db

@alerts.route('/create', methods=['POST'])
@token_required
def create_alert(current_user):
    data = request.json
    if 'target_price' not in data or 'coin' not in data:
        return jsonify({'message': "Required Details Not Entered"}), 401
    a = Alert(target_price=data['target_price'], coin=data['coin'], user_id=current_user.id, status="CREATED")
    if Alert.query.filter(Alert.user_id == current_user.id).filter(Alert.coin == a.coin).filter(Alert.target_price == a.target_price).filter(Alert.status == a.status).first():
        return jsonify({"message": "Alert Already Exists"})
    try:
        db.session.add(a)
        db.session.commit()
        return jsonify({"message": "Alert Created SuccessFully"}), 200
    except:
        return jsonify({"message": "DataBase Error Encountered"}), 401

@alerts.route('/delete', methods=['POST'])
@token_required
def delete_alert(current_user):
    data = request.json
    if 'id' not in data:
        return jsonify({"message": "Enter the Id of the Alert You Want To Delete"}), 401
    a = Alert.query.filter_by(id=data['id']).first()
    if a:
        a.status = "DELETED"
        db.session.add(a)
        db.session.commit()
        return jsonify({"message": "Alert Deleted Successfully"}), 200
    return jsonify({"message": "Invalid Alert Id"}), 200

@alerts.route('/fetch_all/', methods=['POST'])
@alerts.route('/fetch_all/<string:filt>', methods=['POST'])
@token_required
def fetch_all_alerts(current_user, filt=''):
    res = current_user.alerts

    def f(elem):
        return elem.status == filt
    if filt != '':
        res = list(filter(f, res))
    temp = []
    for i in range(len(res)):
        temp.append({
            'target_price': res[i].target_price,
            'coin': res[i].coin,
            'user_id': res[i].user_id,
            'status': res[i].status,
            'created': res[i].created
        })
    return jsonify({"message": temp}), 200
