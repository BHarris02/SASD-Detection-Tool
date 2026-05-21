"""
tests/conftest.py
"""

from os import environ

import pytest

from src import create_app


@pytest.fixture
def app():
    """
    Flask app configured for tests
    """
    environ["FLASK_ENV"] = "testing"
    flask_app = create_app()
    flask_app.config["TESTING"] = True
    yield flask_app


@pytest.fixture
def client(app):  # pylint: disable=redefined-outer-name
    """
    Flask test client
    """
    return app.test_client()
