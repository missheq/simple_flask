from flask_script import Manager

from app import creat_app
from scripts import manager as db_manager
manager = Manager(creat_app())
manager.add_command('database', db_manager)

if __name__ == '__main__':
    manager.run()