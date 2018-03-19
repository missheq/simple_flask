from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


import time



class Record(db.Model):
    __tablename__ = 'record'
    
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(100), unique=True)
    last_time = db.Column(db.DateTime)
    
    def __init__(self, bid, status='unused', last_time=time.time()):
        self.bid = bid
        self.status = status
        self.last_time = last_time
        
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return u"Record<%d>" % self.bid
