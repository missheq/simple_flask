from flask import Flask

from .models import db
from .record.views import record as record

def create_app():
    app = Flask(__name__)
    app.register_blueprint(record)
    db.init_app(app)
    return app
