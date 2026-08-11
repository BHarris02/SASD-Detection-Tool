"""
src/__init__.py
"""
from flask import Flask
from flask_injector import FlaskInjector

from src.blueprint import app_bp
from src.module import ClientsModule, UsecaseModule


def create_app() -> Flask:
    """
    Create and configure the application
    """
    app = Flask(__name__)
    app.register_blueprint(app_bp)
    FlaskInjector(app=app, modules=[ClientsModule, UsecaseModule])
    return app
