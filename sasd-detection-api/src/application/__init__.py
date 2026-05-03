"""
Flask app factory
"""
from flask import Flask, Blueprint
from src.application.extensions import register_cors
from src.presentation.blueprint.analysis import analysis_bp

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
    # import Flask routes before registering the blueprint
    import src.presentation.blueprint.analysis.routes   # pylint: disable=unused-import
    # register blueprints
    app_bp.register_blueprint(analysis_bp)
    app.register_blueprint(app_bp)
    return app
