"""
src/client/collection/api.py
"""
from abc import ABC, abstractmethod

from src.model import Commit, File, Issue


class ArtefactCollectionClient(ABC):
    """
    Abstract base class exposing the contract required to collect artefacts
    """

    @abstractmethod
    def fetch_commits(self, repo_owner: str, repo_name: str) -> list[Commit]:
        """
        Fetch commits messages from a provided repository
        
        :param repo_owner: The repository owner
        :param repo_name: The repository name
        
        :return list[Commit]: A list of Commit entities

        :raises RepositoryNotFoundException:
        :raises NoCommitsFoundException:
        """

    @abstractmethod
    def fetch_issues(self, repo_owner: str, repo_name: str) -> list[Issue]:
        """
        Fetch issues from a provided repository
        
        :param repo_owner: The repository owner
        :param repo_name: The repository name
        
        :return list[Issue]: A list of Issue entities

        :raises RepositoryNotFoundException:
        :raises NoIssuesFoundException:
        """

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
