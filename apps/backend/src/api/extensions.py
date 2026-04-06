"""
Extensions apps for Flask application.
"""
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector

from di.container import AppContainer

def register_cors(app: Flask) -> None:
    """
    Register CORS with Flask app.
    """
    CORS(app)

def register_flask_injector(app: Flask) -> None:
    """
    Register FlaskInjector with Flask app for DI.
    """
    FlaskInjector(
        app=app,
        modules=AppContainer.modules
    )
