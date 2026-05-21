"""
test/test_cors.py
"""

TEST_ORIGIN = "http://testorigin.test"


def test_cors_headers_on_api_routes(client):
    """
    CORS allows configured origins on /api/* preflight
    """
    resp = client.options(
        "/api/v1/does-not-exist",
        headers={
            "Origin": TEST_ORIGIN,
            "Access-Control-Request-Method": "GET",
        },
    )
    assert resp.headers.get("Access-Control-Allow-Origin") == TEST_ORIGIN


def test_cors_rejects_unconfigured_origin(client):
    """
    CORS only allows configured origins — others get no header
    """
    response = client.options(
        "/api/v1/does-not-exist",
        headers={
            "Origin": "http://evil.test",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert response.headers.get("Access-Control-Allow-Origin") is None


def test_cors_not_applied_to_health(client):
    """
    Health is unscoped from CORS — probes don't need it
    """
    resp = client.options(
        "/health",
        headers={
            "Origin": "http://localhost:5173",
            "Access-Control-Request-Method": "GET",
        },
    )
    assert resp.headers.get("Access-Control-Allow-Origin") is None
