from flask import Flask
from flask_migrate import Migrate
from config import config_by_name


# DELETE THIS LINE if it exists: db = SQLAlchemy()
# Instead, import db from models (placed below the app def to avoid circular imports)

def create_app(config_name):
    app = Flask(__name__)

    # Load config
    app.config.from_object(config_by_name[config_name])


    # Register Blueprints
    from app.main import main_bp
    from app.admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin-portal')

    return app