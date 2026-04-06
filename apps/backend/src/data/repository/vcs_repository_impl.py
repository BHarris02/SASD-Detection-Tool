"""
Concrete implementations of VCSRepository contract exposed in `domain` layer.
"""
from apps.backend.src.data.mapper.vcs_entity_mapper import (
    commit_dto_to_domain,
    issue_dto_to_domain,
    file_content_dto_to_domain
)
from apps.backend.src.data.client.vcs.vcs_api_service import VCSApiService
from apps.backend.src.domain.entity.vcs import Commit, FileContent, Issue, RepositoryItem
from apps.backend.src.domain.repository.vcs_repository_api import VCSRepository

class GitHubVCSRepository(VCSRepository):
    """
    A concrete `VCSRepository` implemented using GitHub.
    """
    def __init__(self, api_service: VCSApiService) -> None:
        self._api_service = api_service

    def get_commits(self, repo_url: str) -> list[Commit]:
        try:
            commit_dtos = self._api_service.fetch_commits(repo_url)
            commits = [ commit_dto_to_domain(dto) for dto in commit_dtos ]
            return commits
        except Exception as e:
            raise e

    def get_issues(self, repo_url: str) -> list[Issue]:
        try:
            issue_dtos = self._api_service.fetch_issues(repo_url)
            issues = [ issue_dto_to_domain(dto) for dto in issue_dtos ]
            return issues
        except Exception as e:
            raise e

    def get_file_content(self, repo_url: str, file_path: str) -> FileContent:
        try:
            content_dto = self._api_service.fetch_file_content(repo_url, file_path)
            content = file_content_dto_to_domain(content_dto)
            return content
        except Exception as e:
            raise e

    def get_repository_structure(self, repo_url: str) -> list[RepositoryItem]:
        ...
