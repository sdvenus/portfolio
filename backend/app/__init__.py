from flask import Flask
from config import Config
from .api.routes import api
from .authentication.routes import auth
from flask_migrate import Migrate
from models import db as root_db, login_manager, ma
from flask_cors import CORS
from helpers import JSONEncoder

def create_app(config_class=Config):
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(auth)
    app.register_blueprint(api)
    app.json_encoder = JSONEncoder
    app.config.from_object(config_class)
    root_db.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)
    migrate = Migrate(app, root_db)
    return app
