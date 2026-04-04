"""
Interactor interfaces to expose available VCS data collection interactors to dependent layers, 
whilst hiding implementation details.
"""
from typing import Protocol

from apps.backend.src.domain.common.result import Result
from apps.backend.src.domain.entity.vcs import FileContent, RepositoryItem

class GetFileContentUseCase(Protocol):
    """
    Interface to expose file content fetching interactor to `api` layer.
    """
    def __call__(self, repo_url: str, file_path: str) -> Result[FileContent]:
        """
        Calls `VCSRepository().get_file_content(repo_url, file_path)` and passes
        returned `FileContent` to user.
        """
        ...

class GetRepositoryStructureUseCase(Protocol):
    """
    Interface to expose repository structure fetching interactor to `api` layer.
    """
    def __call__(self, repo_url: str) -> Result[list[RepositoryItem]]:
        """
        Calls `VCSRepository().get_repository_structure(repo_url)` and passes
        returned `RepositoryItem`s to user.
        """
        ...
