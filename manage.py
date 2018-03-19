from flask_script import Manager

from record.views import record as record_view
from record import app

app.register_blueprint(record_view)
manager = Manager(app)

if __name__ == '__main__':
    manager.run()