from app import db
import time

class Record(db.Model):
    __tablename__ = 'record'
    
    id = db.Column(db.Integer, primary_key=True)
    bid = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(100), unique=False)
    #last_time = db.Column(db.DateTime)
    
    def __init__(self, bid, status='unused'):
        self.bid = bid
        self.status = status
        self.last_time = last_time
        
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return u"Record<%d>" % self.bid
