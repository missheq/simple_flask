from flask import Blueprint, request, url_for, redirect
from app import db
from models import Record

record = Blueprint('record', __name__)

@record.route('/record/<bid>')
def find(bid):
    rd = Record.query.filter(Record.bid == bid).first()
    if rd is None:
        db.session.add(Record(bid))
        db.session.commit()
        print 'find a new record'
    return 'ok'
