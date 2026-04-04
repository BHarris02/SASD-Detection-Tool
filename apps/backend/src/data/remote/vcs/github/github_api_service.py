"""
Concrete implementation of `VCSApiService` using GitHub API.
"""
from base64 import b64decode
from requests import get

from apps.backend.src.data.remote.vcs.dtos import (
    CommitDto, FileContentDto, IssueDto, IssueLabelDto, RepositoryItemDto
)
from apps.backend.src.data.remote.vcs.github.models import (
    GitHubCommitResponse
)
from apps.backend.src.data.remote.vcs.vcs_api_service import VCSApiService

class GitHubApiService(VCSApiService):
    """
    Service that fetches artifact DTOs from GitHub API.
    """
    def __init__(self, api_token: str, base_url: str, timeout: int) -> None:
        self._api_token = api_token
        self._base_url =  base_url
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self._api_token}"
        }
        self._timeout = timeout

    def fetch_commits(self, repo_url: str) -> list[CommitDto]:
        resp = get(
            url=f"{self._base_url}/repos/{repo_url}/commits",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        commits = resp.json()
        validated = [
            GitHubCommitResponse.model_validate(commit)
            for commit in commits
        ]
        return [ v.commit for v in validated ]

    def fetch_issues(self, repo_url: str) -> list[IssueDto]:
        resp = get(
            url=f"{self._base_url}/repos/{repo_url}/issues",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        issues = resp.json()
        return [
            IssueDto(
                title=issue["title"],
                description=issue["body"],
                labels = [
                    IssueLabelDto(
                        name=label["name"],
                        description=label["description"]
                    )
                    for label in issue["labels"]
                ]
            )
            for issue in issues
        ]

    def fetch_file_content(self, repo_url: str, file_path: str) -> FileContentDto:
        resp = get(
            url=f"{self._base_url}/repos/{repo_url}/contents/{file_path}",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        content = resp.json()
        decoded = b64decode(content["content"]).decode("utf-8")
        return FileContentDto(content=decoded)

    def fetch_repository_structure(self, repo_url: str) -> list[RepositoryItemDto]:
        ...
