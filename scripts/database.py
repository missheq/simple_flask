# -*- coding: utf-8 -*-
from flask_script import Manager
from app import db


manager = Manager(usage="Perform database operations")


@manager.option('-d', '--dbname', dest='db_name', required=True)
def drop(db_name):
    "Drops database tables"
    if db_name == 'record':
        db.drop_all()
    else:
        print "No DB named {}.".format(db_name)
    print "Done"


@manager.option('-d', '--dbname', dest='db_name', required=True)
def create(db_name):
    "Creates database tables from sqlalchemy models"
    if db_name == 'record':
        db.create_all(bind=None)
    else:
        print "No DB named {}.".format(db_name)
    print "Done"
