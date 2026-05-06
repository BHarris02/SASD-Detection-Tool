"""
Version Control System gateway interface
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain.entity.vcs import (
    CommitArtefact,
    IssueArtefact,
    PullRequestArtefact
)

class VcsGateway(ABC):
    """
    VCS Gateway
    """
    @abstractmethod
    def fetch_commits(self, repository_owner: str, repository_name: str) -> List[CommitArtefact]:
        """
        Fetch commits from data source
        """

    @abstractmethod
    def fetch_issues(self, repository_owner: str, repository_name: str) -> List[IssueArtefact]:
        """
        Fetch issues from data source
        """

    @abstractmethod
    def fetch_pull_requests(self, repository_owner: str, repository_name: str) -> List[PullRequestArtefact]:
        """
        Fetch pull requests from data source
        """
