from flask import Blueprint, request, url_for, redirect
from app import db
from models import Record

record = Blueprint('record', __name__)

@record.route('/record/<bid>')
def login(bid):
    rd = db.session.query(Record).filter(Record.bid == bid).first()
    if rd is None:
    	print 'find a new record'
