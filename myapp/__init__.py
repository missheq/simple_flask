from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .record.views import record as record
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
    app.register_blueprint(record)
    db.init_app(app)
    return app
