from app import db
from datetime import datetime

class Record(db.Model):
    __tablename__ = 'record'
    
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), unique=False)
    last_time = db.Column(db.String(100))
    
    def __init__(self, bid, status='unused', last_time=datetime.now()):
        self.bid = bid
        self.status = status
        self.last_time = last_time.isoformat()
        
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return u"Record<%d>" % self.bid

class Task(db.Model):
    """docstring for Task"""
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.String(100), nullable=False)
    tid = db.Column(db.String(100), nullable=False)

    def __init__(self):
        sel 
        
