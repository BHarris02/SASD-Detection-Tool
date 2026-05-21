"""
tests/test_smoke.py
"""


def test_app_boots(app):
    """
    Factory creates Flask app without throwing
    """
    assert app is not None
    assert app.config["TESTING"] is True


def test_health_endpoint_returns_ok(client):
    """
    GET /health returns 200 with {status: ok}
    """
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.is_json
    assert resp.get_json() == {"status": "ok"}


def test_health_is_unversioned(client):
    """
    Health check lives at /health, not /api/v1/health
    """
    versioned = client.get("/api/v1/health")
    assert versioned.status_code == 404
