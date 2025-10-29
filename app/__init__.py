from flask import Flask
from flask_cors import CORS
from config import ProductionConfig, DevelopmentConfig
from app.models import db
from rutas import register_blueprints
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    environment = os.getenv("ENV", "local")

    if environment == "production":
        app.config.from_object(ProductionConfig)
        cors_origins = ["https://system-control.netlify.app"]
    else:
        app.config.from_object(DevelopmentConfig)
        cors_origins = ["http://localhost:5432"]

    CORS(app, resources={r"/*": {"origins": cors_origins}}, supports_credentials=True)

    db.init_app(app)
    register_blueprints(app)

    return app
