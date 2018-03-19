from flask_script import Manager

from myapp.record.views import record as record
from myapp.models import app

app.register_blueprint(record)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()