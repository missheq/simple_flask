import os
import logging

from flask import Flask

from .database import init_engine, init_db, db_session
from .models import Record
from .record.views import record as record


assets = Environment()



def create_app(db_uri='any'):

    app = Flask(__name__)
    app.config.from_object('myapp.default_config')
    app.config.from_pyfile(os.path.join(app.instance_path, 'config.py'))
    
    if db_uri == 'Test':
        init_engine(app.config['TEST_DATABASE_URI'])
    else:
        init_engine(app.config['DATABASE_URI'])
        
    #Register Blueprints
    app.register_blueprint(record)

    #App logging
#    app.logger.setLevel(logging.WARNING)
#    logger_handler = logging.FileHandler(os.path.join(app.config['LOG_LOCATION'],
#                                                      'app_errors.log'))
#    formatter = logging.Formatter('%(asctime)s  %(levelname)s - %(message)s'
#                              ' [in %(pathname)s:%(lineno)d]')
#    logger_handler.setFormatter(formatter)
#    app.logger.addHandler(logger_handler)


    @app.teardown_request
    def shutdown_session(exception=None):
        db_session.remove()
    
    return app
