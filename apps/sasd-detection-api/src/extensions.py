"""
src/extensions.py
"""
from flask import Flask
from flask_cors import CORS
from flask_pydantic_spec import FlaskPydanticSpec


# pylint: disable=missing-function-docstring
app_spec = FlaskPydanticSpec(
    backend_name="sasd-detection-api",
    version="0.1.0-SNAPSHOT"
)


def register_pydantic_spec(app: Flask) -> None:
    app_spec.register(app)


def register_cors(app: Flask) -> None:
    CORS(app)
