"""
src/blueprint/__init__.py
"""
from flask import Blueprint

from src.blueprint.analysis import analysis_bp
from src.blueprint.health import health_bp


app_bp = Blueprint(name="app_bp", import_name=__name__, url_prefix="/api/v1")

app_bp.register_blueprint(analysis_bp)
app_bp.register_blueprint(health_bp)
