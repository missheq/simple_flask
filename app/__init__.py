from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import record as record_view
import os
basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()

def creat_app():

	app = Flask(__name__)
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/record.db'
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
	db.init_app(app)
	with app.app_contest():
		db.create_all()
	app.register_blueprint(record_view)
	return app


#from record import views