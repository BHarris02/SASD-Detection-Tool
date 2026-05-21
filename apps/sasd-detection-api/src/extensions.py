"""
src/extensions.py
"""

from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from injector import Module

from src.container import get_modules


def register_cors(app: Flask) -> None:
    """
    CORS configuration
    """
    CORS(app=app, resources={r"/api/*": {"origins": app.config["CORS_ORIGINS"]}})


def register_flask_injector(app: Flask, modules: list[Module] | None = None) -> None:
    """
    Flask Injector for DI
    """
    FlaskInjector(app=app, modules=modules or get_modules())
