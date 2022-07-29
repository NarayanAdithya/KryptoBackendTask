import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config():
    ENVIRONMENT = os.environ.get('environment')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sjskfdojg&*&(9')

class Development(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

class Production(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
