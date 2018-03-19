import os
import logging

from flask import Flask

from .models import Record
from .record.views import record as record
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)
app.register_blueprint(record)


