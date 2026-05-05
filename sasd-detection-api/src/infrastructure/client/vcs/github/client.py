"""
HTTP client to send requests to GitHub API
"""
from typing import Any
from requests import get

class GitHubClient:
    """
    HTTP client that fetches repositort artefacts via GitHub API
    """
    def __init__(self, api_token: str, base_url: str, timeout: int):
        self._api_token = api_token
        self._base_url = base_url
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {self._api_token}"
        }
        self._timeout = timeout

    def fetch_commits(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch commits via API call
        """
        resp = get(
            url=f"{self._base_url}/repos/{repository_owner}/{repository_name}/commits",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        commits = resp.json()
        return commits

    def fetch_issues(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch issues via API call
        """
        resp = get(
            url=f"{self._base_url}/repos/{repository_owner}/{repository_name}/issues",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        issues = resp.json()
        return issues

    def fetch_pull_requests(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch pull requests via API call
        """
        resp = get(
            url=f"{self._base_url}/repos/{repository_owner}/{repository_name}/pulls",
            headers=self._headers,
            timeout=self._timeout
        )
        resp.raise_for_status()
        prs = resp.json()
        return prs
