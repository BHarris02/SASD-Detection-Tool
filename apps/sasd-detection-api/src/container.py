"""
src/container.py
"""
from flask import Flask
from flask_injector import FlaskInjector

from src.module import ClientsModule, StrategiesModule, UsecaseModule


# pylint: disable=missing-function-docstring
def register_injector(app: Flask) -> None:
    FlaskInjector(app=app, modules=[ClientsModule, StrategiesModule, UsecaseModule])
