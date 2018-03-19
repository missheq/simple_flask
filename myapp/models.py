from flask.ext.sqlalchemy import SQLAlchemy

import time

db = SQLAlchemy()

class Record(db.Model):
    __tablename__ = 'record'
    
    id = Column(db.Integer, primary_key=True)
    bid = Column(db.Integer, nullable=False)
    status = Column(db.String(100), unique=True)
    last_time = Column(db.DateTime, default=text("current_timestamp"))
    
    def __init__(self, bid, status='unused', last_time=time.time()):
        self.bid = bid
        self.status = status
        self.last_time = last_time
        
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return u"Record<%d>" % self.bid
