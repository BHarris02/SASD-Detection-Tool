"""
Functions to register additional Flask functionality.
"""
from flask import Flask
from flask_cors import CORS

def register_cors(app: Flask) -> None:
    """
    Register CORS
    """
    CORS(app)
