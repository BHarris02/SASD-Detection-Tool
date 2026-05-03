"""
Version Control System gateway interface
"""
from abc import ABC, abstractmethod
from typing import Any

class VcsGateway(ABC):
    """
    VCS Gateway
    """
    @abstractmethod
    def fetch_commits(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch commits from data source
        """

    @abstractmethod
    def fetch_issues(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch issues from data source
        """

    @abstractmethod
    def fetch_pull_requests(self, repository_owner: str, repository_name: str) -> Any:
        """
        Fetch pull requests from data source
        """
