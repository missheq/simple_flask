from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .record.views import record as record

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.register_blueprint(record)
db = SQLAlchemy(app)
app.register_blueprint(record)