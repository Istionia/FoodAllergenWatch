# __init__.py
from flask import Flask
from .extensions import db, migrate
from config import Config
import logging

def create_app():
    app = Flask(__name__)
    
    # Load configuration
    app.config.from_object(Config)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Import and register blueprints
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # Set up logging
    if not app.debug:
        logging.basicConfig(level=logging.INFO)
    
    return app