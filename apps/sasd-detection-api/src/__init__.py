"""
src/__init__.py
"""

from os import environ

from flask import Flask, Blueprint
from injector import Module

from src.blueprint import health_bp
from src.config import config_map
from src.errors import register_error_handlers
from src.extensions import register_cors, register_flask_injector
from src.logger import configure_logging


def create_app(modules: list[Module] | None = None) -> Flask:
    """
    Create + configure Flask app
    """
    # config
    cfg = config_map[environ.get("FLASK_ENV", "production")]
    # logging
    configure_logging(level="DEBUG" if cfg.DEBUG else "INFO")

    # flask setup
    app = Flask(__name__)
    app.config.from_object(cfg)

    # register extensions
    register_error_handlers(app)
    register_cors(app)

    # app blueprint
    app_bp = Blueprint(name="app_bp", import_name=__name__, url_prefix="/api/v1")

    # register blueprints
    app.register_blueprint(health_bp)  # /health
    app.register_blueprint(app_bp)  # /api/v1

    # register flask injector
    register_flask_injector(app=app, modules=modules)

    return app
