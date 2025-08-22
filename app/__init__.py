from flask import Flask
from flask_cors import CORS
from config import Config
from app.models import db
from routers import register_blueprints


def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)

    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

    db.init_app(app)

    register_blueprints(app)

    return app
