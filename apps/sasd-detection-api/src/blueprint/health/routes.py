"""
src/blueprint/health/routes.py
"""
from flask import Blueprint


health_bp = Blueprint(name="health_bp", import_name=__name__)

@health_bp.get("/health")
def get_health_route():
    """
    Health check endpoint
    """
    return {
        "status": "ok"
    }, 200
