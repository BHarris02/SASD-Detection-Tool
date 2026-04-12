"""
Health check endpoint.
"""
from flask import Blueprint, jsonify

health_bp = Blueprint(
    name="health_bp",
    import_name=__name__
)

@health_bp.get("/health")
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({
        "status": "ok"
    }), 200
