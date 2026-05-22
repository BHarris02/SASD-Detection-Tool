"""
tests/client/vcs/test_github.py
"""

import pytest
import responses
from requests.exceptions import ConnectionError as RequestsConnectionError, Timeout

from src.client.vcs.exceptions import (
    VCSNotFound,
    VCSRateLimited,
    VCSUnavailable,
    VCSUnexpectedError,
)
from src.model import CommitArtefact

BASE_URL = "https://api.test"
COMMITS_PATH = "/repos/octocat/hello-world/commits"


def _commit(message: str) -> dict:
    """Minimal commit JSON shape — extend if CommitArtefact gains fields."""
    return {"commit": {"message": message}}


@responses.activate
def test_fetch_commits_returns_artefacts(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json=[_commit("first"), _commit("second")],
        status=200,
    )

    result = github_client.fetch_commits("octocat", "hello-world")

    assert len(result.artefacts) == 2
    assert result.skipped == 0
    assert all(isinstance(a, CommitArtefact) for a in result.artefacts)
    assert result.artefacts[0].commit.message == "first"


@responses.activate
def test_fetch_commits_skips_invalid_artefacts(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json=[_commit("valid"), {"not": "a commit"}, _commit("also valid")],
        status=200,
    )

    result = github_client.fetch_commits("octocat", "hello-world")

    assert len(result.artefacts) == 2
    assert result.skipped == 1


@responses.activate
def test_fetch_commits_raises_not_found_on_404(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json={"message": "Not Found"},
        status=404,
    )

    with pytest.raises(VCSNotFound):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_raises_rate_limited_on_403_with_exhausted_header(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json={"message": "API rate limit exceeded"},
        status=403,
        headers={"X-RateLimit-Remaining": "0"},
    )

    with pytest.raises(VCSRateLimited):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_raises_unexpected_error_on_403_without_rate_limit_header(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json={"message": "Forbidden"},
        status=403,
    )

    with pytest.raises(VCSUnexpectedError):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_raises_unexpected_error_on_500(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json={"message": "Server Error"},
        status=500,
    )

    with pytest.raises(VCSUnexpectedError):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_raises_unavailable_on_connection_error(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        body=RequestsConnectionError("connection refused"),
    )

    with pytest.raises(VCSUnavailable):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_raises_unavailable_on_timeout(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        body=Timeout("read timed out"),
    )

    with pytest.raises(VCSUnavailable):
        github_client.fetch_commits("octocat", "hello-world")


@responses.activate
def test_fetch_commits_requests_max_per_page(github_client):
    responses.get(
        f"{BASE_URL}{COMMITS_PATH}",
        json=[],
        status=200,
    )

    github_client.fetch_commits("octocat", "hello-world")

    call = responses.calls[0].request
    assert call.url is not None
    assert "per_page=100" in call.url
