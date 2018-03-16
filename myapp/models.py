from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, text
from sqlalchemy.ext.hybrid import hybrid_property

from .database import Base
import time

class Record(Base):
    __tablename__ = 'record'
    
    id = Column(Integer, primary_key=True)
    bid = Column(Integer, nullable=False)
    status = Column(String(100), unique=True)
    last_time = Column(DateTime, default=text("current_timestamp"))
    
    def __init__(self, bid, status='unused', last_time=time.time()):
        self.bid = bid
        self.status = status
        self.last_time = last_time
        
    def get_id(self):
        return unicode(self.id)
    
    def __repr__(self):
        return u"Record<%d>" % self.bid
