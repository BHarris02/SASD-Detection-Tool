"""
HTTP client to send requests to GitHub API
"""
from typing import List

from requests import get

from src.infrastructure.client.vcs.github.dtos import CommitDto, IssueDto, PullRequestDto

GITHUB_API_VERSION = "2022-11-28"

class GitHubClient:
    """
    HTTP client that fetches repository artefacts via GitHub API
    """
    def __init__(self, api_token: str, base_url: str, timeout: int, user_agent: str):
        self._base_url = base_url
        self._headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {api_token}",
            "X-GitHub-Api-Version": GITHUB_API_VERSION,
            "User-Agent": user_agent
        }
        self._timeout = timeout

    def fetch_commits(self, repository_owner: str, repository_name: str) -> List[CommitDto]:
        """
        Fetch commits via API call
        """
        resp = self._fetch(f"/repos/{repository_owner}/{repository_name}/commits")
        return [CommitDto.model_validate(commit) for commit in resp]

    def fetch_issues(self, repository_owner: str, repository_name: str) -> List[IssueDto]:
        """
        Fetch issues via API call
        """
        resp = self._fetch(f"/repos/{repository_owner}/{repository_name}/issues")
        # GitHub's /issues endpoint returns issues AND pull requests
        # Issues with `pull_request` key are disguised PRs
        return [
            IssueDto.model_validate(issue)
            for issue in resp
            if self._is_issue(issue)
        ]

    def fetch_pull_requests(
            self,
            repository_owner: str,
            repository_name: str
    ) -> List[PullRequestDto]:
        """
        Fetch pull requests via API call
        """
        resp = self._fetch(f"/repos/{repository_owner}/{repository_name}/pulls")
        return [PullRequestDto.model_validate(pr) for pr in resp]

    def _fetch(self, path: str) -> List[dict]:
        resp = get(
            url=f"{self._base_url}{path}",
            headers=self._headers,
            params={ "per_page": 100 }, # TODO: need to implement proper pagination
            timeout=self._timeout
        )
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def _is_issue(raw: dict) -> bool:
        return "pull_request" not in raw
