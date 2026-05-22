"""
src/client/vcs/github.py
"""

from pydantic import ValidationError
from requests import Session
from requests.exceptions import ConnectionError as RequestsConnectionError, Timeout

from src.client.vcs.base import VCSClient
from src.client.vcs.config import VCSConfig
from src.client.vcs.exceptions import (
    VCSUnavailable,
    VCSNotFound,
    VCSRateLimited,
    VCSUnexpectedError,
)
from src.model import ArtefactFetchResult, CommitArtefact

_DEFAULT_PER_PAGE = 100


class GitHubClient(VCSClient):
    """
    Concrete implementation of `VCSClient` using GitHub API
    """

    def __init__(self, config: VCSConfig) -> None:
        self._config = config
        self._session = Session()
        self._session.headers.update(
            {
                "Accept": "application/vnd.github+json",
                "Authorization": f"Bearer {config.token}",
                "X-GitHub-Api-Version": config.api_version,
                "User-Agent": config.user_agent,
            }
        )

    def fetch_commits(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult[CommitArtefact]:
        resp = self._fetch(f"/repos/{repo_owner}/{repo_name}/commits")
        commits, skipped = [], 0
        for commit in resp:
            try:
                commits.append(CommitArtefact.model_validate(commit))
            except ValidationError:
                skipped += 1
        return ArtefactFetchResult(artefacts=commits, skipped=skipped)

    def fetch_issues(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult:
        raise NotImplementedError()

    def fetch_pulls(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult:
        raise NotImplementedError()

    def _fetch(self, path: str):
        try:
            resp = self._session.get(
                url=f"{self._config.base_url}{path}",
                params={"per_page": _DEFAULT_PER_PAGE},
                timeout=self._config.timeout,
            )
        except (RequestsConnectionError, Timeout) as e:
            raise VCSUnavailable("GitHub unreachable") from e

        if resp.status_code == 404:
            raise VCSNotFound(f"Not found: {path}")
        if resp.status_code == 403 and resp.headers.get("X-RateLimit-Remaining") == "0":
            raise VCSRateLimited("GitHub rate limit exhausted")
        if not resp.ok:
            raise VCSUnexpectedError(f"GitHub returned {resp.status_code}")

        return resp.json()
