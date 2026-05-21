"""
src/errors.py
"""

from logging import getLogger

from flask import Flask, jsonify, request
from werkzeug.exceptions import HTTPException

_logger = getLogger(__name__)


def register_error_handlers(app: Flask) -> None:
    """
    Error handlers for specific exception types
    """

    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return jsonify({"error": e.name, "message": e.description}), e.code

    @app.errorhandler(Exception)
    def handle_unexpected_exception(_):
        _logger.exception("Unhandled exception on %s %s", request.method, request.path)
        return jsonify({"error": "Internal server error"}), 500
