"""
tests/clint/vcs/conftest.py
"""

import pytest

from src.client.vcs.config import VCSConfig
from src.client.vcs.github import GitHubClient

BASE_URL = "https://api.test"


@pytest.fixture
def vcs_config():
    return VCSConfig(
        token="test-token",
        base_url=BASE_URL,
        user_agent="test-agent/0.1",
        timeout=5,
        api_version="2022-11-28",
    )


@pytest.fixture
def github_client(vcs_config):
    return GitHubClient(vcs_config)
