from flask import Flask
from flask_cors import CORS
from config import ProductionConfig, DevelopmentConfig
from app.models import db
from rutas import register_blueprints
import os

def create_app():
    app = Flask(__name__)

    if os.environ.get("RENDER") == "true": 
        app.config.from_object(ProductionConfig)
        cors_origins = ["https://tu-frontend.netlify.app"]  
    else:
        app.config.from_object(DevelopmentConfig)
        cors_origins = ["http://localhost:5173"] 

    CORS(app, resources={r"/*": {"origins": cors_origins}}, supports_credentials=True)

    db.init_app(app)

    register_blueprints(app)

    return app
