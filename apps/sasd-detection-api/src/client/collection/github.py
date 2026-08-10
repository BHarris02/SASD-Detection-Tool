"""
src/client/github.py
"""
from base64 import b64decode

from requests import get

from src.client.collection.api import ArtefactCollectionClient
from src.exception import (
    NotAFileException,
    NoCommitsFoundException,
    NoFileContentException,
    NoFileFoundException,
    NoIssuesFoundException,
    RepositoryNotFoundException
)
from src.model import Commit, File, Issue


class GitHubClient(ArtefactCollectionClient):
    """
    Outbound port that fetches artefacts from GitHub repositories via API call
    """
    def __init__(self, api_url: str, token: str, timeout: int = 10):
        self._api_url = api_url
        self._headers = {
            "Authorization": f"token {token}"
        }
        self._timeout = timeout

    def fetch_commits(self, repo_owner: str, repo_name: str) -> list[Commit]:
        """
        Fetch commits messages from a provided repository
        
        :param repo_owner: The repository owner
        :param repo_name: The repository name
        
        :return list[Commit]: A list of Commit entities

        :raises RepositoryNotFoundException:
        :raises NoCommitsFoundException:
        """
        resp = get(
            url=f"{self._api_url}/repos/{repo_owner}/{repo_name}/commits",
            headers=self._headers,
            timeout=self._timeout
        )

        match resp.status_code:
            case 404: raise RepositoryNotFoundException()
            case 409: raise NoCommitsFoundException()

        resp.raise_for_status()
        commits = resp.json()

        return [
            Commit(
                sha=commit["sha"],
                message=commit["commit"]["message"]
            )
            for commit in commits
        ]

    def fetch_issues(self, repo_owner: str, repo_name: str) -> list[Issue]:
        """
        Fetch issues from a provided repository
        
        :param repo_owner: The repository owner
        :param repo_name: The repository name
        
        :return list[Issue]: A list of Issue entities

        :raises RepositoryNotFoundException:
        :raises NoIssuesFoundException:
        """
        resp = get(
            url=f"{self._api_url}/repos/{repo_owner}/{repo_name}/issues",
            headers=self._headers,
            timeout=self._timeout
        )

        if resp.status_code == 404:
            raise RepositoryNotFoundException()

        resp.raise_for_status()
        issues = resp.json()

        if issues == []:
            raise NoIssuesFoundException()

        return [
            Issue(
                number=issue["number"],
                title=issue["title"],
                body=issue["body"],
                is_pull_request="pull_request" in issue
            )
            for issue in issues
        ]

    def fetch_file(self, repo_owner: str, repo_name: str, file_path: str) -> File:
        """
        Fetch content from a specific file in the repository
        
        :param repo_owner: The repository owner
        :param repo_name: The repository name
        :param file_path: The path to the desired file

        :return File: A File entity with base 64 decoded content

        :raises RepositoryNotFoundException:
        :raises NoFileFoundException:
        :raises NoFileContentException:
        """
        resp = get(
            url=f"{self._api_url}/repos/{repo_owner}/{repo_name}/contents/{file_path}",
            headers=self._headers,
            timeout=self._timeout
        )

        if resp.status_code == 404:
            raise NoFileFoundException()

        resp.raise_for_status()
        content = resp.json()

        # both conditions needed to check against git submodules/symlinks
        if not isinstance(content, dict) or "content" not in content:
            raise NotAFileException()

        if content['content'] == "":
            raise NoFileContentException()

        return File(
            sha=content["sha"],
            content=b64decode(content["content"]).decode("utf-8")
        )
