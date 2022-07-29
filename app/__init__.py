from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

import config

app = Flask(__name__)
if os.environ.get('environment') == 'Development':
    app.config.from_object(config.Development)
elif os.environ.get('environment') == 'Production':
    app.config.from_object(config.Production)

# Database Configuration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Blueprint Registration
from app.auth import auth
app.register_blueprint(auth, url_prefix='/auth')

from app import routes
