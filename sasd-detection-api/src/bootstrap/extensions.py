"""
Functions to register additional Flask functionality.
"""
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector

from src.bootstrap.di.container import Container

def register_cors(app: Flask) -> None:
    """
    Register CORS
    """
    CORS(app)

def register_flask_injector(app: Flask) -> None:
    """
    Register FlaskInjector for DI
    """
    FlaskInjector(
        app=app,
        modules=Container.modules
    )
