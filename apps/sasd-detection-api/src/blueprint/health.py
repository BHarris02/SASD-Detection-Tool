"""
src/blueprint/health.py
"""

from flask import Blueprint

health_bp = Blueprint(name="health_bp", import_name=__name__)


@health_bp.get("/health")
def health():
    """
    Health check route
    """
    return {"status": "ok"}
