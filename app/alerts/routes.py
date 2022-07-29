from app.alerts import alerts
from flask import jsonify

@alerts.route('/create')
def create_alert():
    pass

@alerts.route('/delete')
def delete_alert():
    pass

@alerts.route('/fetch_all/<str:filter>')
def fetch_all_alerts():
    pass
