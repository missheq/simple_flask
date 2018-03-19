from flask import Blueprint, request, flash, url_for, redirect

from ..models import Record

record = Blueprint('record', __name__)

@record.route('/record/<bid>', methods=['GET', 'POST'])
def login():
    rd = Record.query.filter(Record.bid == bid).first()
    if rd is None:
    	print 'find a new record'
