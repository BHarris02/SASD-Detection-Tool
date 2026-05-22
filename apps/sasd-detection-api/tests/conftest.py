"""
tests/conftest.py
"""

import pytest

from src import create_app


@pytest.fixture
def app(monkeypatch):
    """
    Flask app configured for tests
    """
    monkeypatch.setenv("FLASK_ENV", "testing")
    monkeypatch.setenv("GITHUB_TOKEN", "test-token")
    flask_app = create_app()
    flask_app.config["TESTING"] = True
    yield flask_app


@pytest.fixture
def client(app):  # pylint: disable=redefined-outer-name
    """
    Flask test client
    """
    return app.test_client()
