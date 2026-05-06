"""
Extensions apps for Flask application.
"""
from flask import Flask
from flask_cors import CORS
from flask_injector import FlaskInjector
from flask_pydantic_spec import FlaskPydanticSpec

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

api_spec = FlaskPydanticSpec(
    "flask",
    title="SASD Detection API",
    version="1.0.0",
    path="/apidocs"
)

def register_api_spec(app: Flask) -> None:
    """
    Register FlaskPydanticSpec with Flask app for OpenAPI docs.
    """
    api_spec.register(app)
