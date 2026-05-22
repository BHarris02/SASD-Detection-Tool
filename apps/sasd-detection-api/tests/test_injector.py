"""
tests/test_injector.py
"""

from src.client.vcs.base import VCSClient


def test_vcs_client_resolves(app):
    client = app.extensions["injector"].get(VCSClient)
    assert isinstance(client, VCSClient)


def test_vcs_client_is_singleton(app):
    injector = app.extensions["injector"]
    a = injector.get(VCSClient)
    b = injector.get(VCSClient)
    assert a is b
