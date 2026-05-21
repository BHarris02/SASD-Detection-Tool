"""
test/test_error_handlers.py
"""


def test_unknown_route_returns_json_404(client):
    """
    HTTPException handler: unknown routes return JSON, not HTML
    """
    response = client.get("/api/v1/does-not-exist")
    assert response.status_code == 404
    assert response.is_json
    body = response.get_json()
    assert "error" in body
    assert "message" in body


def test_unhandled_exception_returns_json_500(app, client):
    """
    Generic Exception handler: routes that raise unexpectedly return JSON 500
    """

    @app.route("/__boom")
    def boom():
        raise RuntimeError("intentional")

    response = client.get("/__boom")
    assert response.status_code == 500
    assert response.is_json
    assert response.get_json() == {"error": "Internal server error"}
