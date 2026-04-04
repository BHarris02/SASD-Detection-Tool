"""
Interface to expose the required methods for retrieving artifacts from the remote data source.
"""
from typing import Protocol

from apps.backend.src.data.remote.vcs.dtos import (
    CommitDto, IssueDto, FileContentDto, RepositoryItemDto
)

class VCSApiService(Protocol):
    """
    Interface that exposes the required methods for concrete VCSApiServices.
    """

    def fetch_commits(self, repo_url: str) -> list[CommitDto]:
        """
        Fetch & parse `CommitDto`s from remote data source.
        """
        ...

    def fetch_issues(self, repo_url: str) -> list[IssueDto]:
        """
        Fetch & parse `IssueDto`s from remote data source.
        """
        ...

    def fetch_file_content(self, repo_url: str, file_path: str) -> FileContentDto:
        """
        Fetch & parse `FileContent` from remote data source.
        """
        ...

    def fetch_repository_structure(self, repo_url: str) -> list[RepositoryItemDto]:
        """
        Fetch & parse all `RepositoryItem`s from remote data source.
        """
        ...
