"""
Factory function to create Flask application.
"""
from os import getenv

from flask import Flask

from apps.backend.src.api.blueprint.health import health_bp
from apps.backend.src.api.config import CONFIG_MAP
from apps.backend.src.api.extensions import (
    register_cors, register_flask_injector
)

def create_app() -> Flask:
    """
    Create & configure Flask app.
    """
    app = Flask(__name__)

    env = getenv("FLASK_ENV", "production")
    app.config.from_object(CONFIG_MAP[env])

    register_cors(app)
    register_flask_injector(app)

    _register_blueprints(app)

    return app

def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(health_bp)
