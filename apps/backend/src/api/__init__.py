"""
Factory function to create Flask application.
"""
from os import getenv

from dotenv import load_dotenv
from flask import Flask

from api.blueprint.health import health_bp
from api.blueprint.vcs import vcs_bp
from api.config import CONFIG_MAP
from api.extensions import (
    register_api_spec, register_cors, register_flask_injector
)

def create_app() -> Flask:
    """
    Create & configure Flask app.
    """
    load_dotenv()

    app = Flask(__name__)

    env = getenv("FLASK_ENV", "production")
    app.config.from_object(CONFIG_MAP[env])

    register_cors(app)
    _register_blueprints(app)
    register_api_spec(app)
    register_flask_injector(app)

    return app

def _register_blueprints(app: Flask) -> None:
    app.register_blueprint(health_bp)
    app.register_blueprint(vcs_bp)
