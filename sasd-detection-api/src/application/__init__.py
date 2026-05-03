"""
Flask app factory
"""
from flask import Flask, Blueprint
from src.application.extensions import register_cors

def create_app() -> Flask:
    """
    Create Flask app.
    """
    app = Flask(__name__)
    # register extensions
    register_cors(app)
    # app blueprint
    app_bp = Blueprint(
        name="app_bp",
        import_name=__name__,
        url_prefix="/api/v1"
    )
    app.register_blueprint(app_bp)
    return app
