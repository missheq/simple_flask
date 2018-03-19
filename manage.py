from flask_script import Manager

from app.views import record as record_view
from app import app

app.register_blueprint(record_view)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()