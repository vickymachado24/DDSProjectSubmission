from flask import Flask
from .models import db
from .routes import create_routes

def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)

    create_routes(app)

    return app
