"""
An interface to expose the required contract methods for 
retrieving artifacts from a remote VCS repository data source.
"""
from typing import Protocol

from apps.backend.src.domain.entity.vcs import Commit, Issue, FileContent, RepositoryItem

class VCSRepository(Protocol):
    """
    Interface that exposes the required methods for the `domain` interactors.
    These methods will be implemented in the `data` layer.
    """

    def get_commits(self, repo_url: str) -> list[Commit]:
        """
        Fetch, parse, and map `Commit`s from the remote data source.

        These are **NOT** displayed to the user; they are directly passed
        to the `NLPRepository` for analysis.
        """
        ...

    def get_issues(self, repo_url: str) -> list[Issue]:
        """
        Fetch, parse, and map `Issue`s from the remote data source.

        These are **NOT** displayed to the user; they are directly passed
        to the `NLPRepository` for analysis.
        """
        ...

    def get_file_content(self, repo_url: str, file_path: str) -> FileContent:
        """
        Fetch, parse, and map `FileContent` from the remote data source.
        
        This **will** be displayed to the user to allow them to select segments
        of code to pass back to the API for analysis.
        """
        ...

    def get_repository_structure(self, repo_url: str) -> list[RepositoryItem]:
        """
        Fetch, parse, and map `RepositoryItem`s from the remote data source.

        This **will** be displayed to the user to allow them to view the repository
        structure, and select files to `get_file_content` for analysis.
        """
        ...
