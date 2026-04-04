"""
Concrete interactors for VCS data collection.
"""
from apps.backend.src.domain.common.error import DomainError
from apps.backend.src.domain.common.result import Result
from apps.backend.src.domain.entity.vcs import FileContent, RepositoryItem
from apps.backend.src.domain.repository.vcs_repository import VCSRepository
from apps.backend.src.domain.usecase.vcs.api import GetFileContentUseCase, GetRepositoryStructureUseCase

class GetFileContentUseCaseImpl(GetFileContentUseCase):
    """
    Concrete interactor for fetching file content.
    """
    def __init__(self, repo: VCSRepository) -> None:
        self._repo = repo

    def __call__(self, repo_url: str, file_path: str) -> Result[FileContent]:
        try:
            file_content = self._repo.get_file_content(repo_url, file_path)
            return Result(
                success=True,
                value=file_content
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )

class GetRepositoryStructureUseCaseImpl(GetRepositoryStructureUseCase):
    """
    Concrete interactor for fetching repository structure.
    """
    def __init__(self, repo: VCSRepository) -> None:
        self._repo = repo

    def __call__(self, repo_url: str) -> Result[list[RepositoryItem]]:
        try:
            items = self._repo.get_repository_structure(repo_url)
            return Result(
                success=True,
                value=items
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )
