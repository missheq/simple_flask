from flask_script import Manager

from myapp import create_app

manager = Manager(create_app())

