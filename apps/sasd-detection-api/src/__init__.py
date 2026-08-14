"""
src/__init__.py
"""
from flask import Flask

from src.blueprint import app_bp
from src.container import register_injector
from src.errors import register_error_handlers
from src.extensions import register_cors, register_pydantic_spec


def create_app() -> Flask:
    """
    Create and configure the application
    """
    app = Flask(__name__)

    # extensions
    register_cors(app)
    register_pydantic_spec(app)
    register_error_handlers(app)

    # blueprints
    app.register_blueprint(app_bp)

    # di
    register_injector(app)

    return app
