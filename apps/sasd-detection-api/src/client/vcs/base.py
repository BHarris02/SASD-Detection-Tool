"""
src/client/vcs/base.py
"""

from abc import ABC, abstractmethod

from src.model import ArtefactFetchResult


class VCSClient(ABC):
    """
    Abstract base class for VCS clients to implement
    """

    @abstractmethod
    def fetch_commits(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult:
        """
        Fetch commits from the API
        """

    @abstractmethod
    def fetch_issues(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult:
        """
        Fetch issues from the API
        """

    @abstractmethod
    def fetch_pulls(self, repo_owner: str, repo_name: str) -> ArtefactFetchResult:
        """
        Fetch pull requests from the API
        """
