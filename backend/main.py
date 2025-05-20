"""
Module Name: main.py
Description: Serves as the entry point for the Flask application. 
            Creates the Flask app, sets up configurations, enables 
            CORS, registers routes, and starts the server
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - Flask
    - flask_cors
    - api.routes.endpoints
    - api.utils.config
Usage:
    Run this module directly to start the Flask server
        python ./main.py
"""

from flask import Flask
from flask_cors import CORS
from api.routes.endpoints import api_bp, api
from api.utils.config import Config

def create_app():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(Config)

    CORS(app)

    api.register(app)

    app.register_blueprint(api_bp, url_prefix="/api")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host = "0.0.0.0", port = 5000, debug = True)