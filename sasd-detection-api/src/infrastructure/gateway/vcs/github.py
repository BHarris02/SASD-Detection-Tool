"""
Concrete implementation of `VcsGateway` using GitHub
"""
from src.application.gateway.vcs_gateway import VcsGateway
from src.domain.error.vcs import NoArtefactsException
from src.infrastructure.client.vcs.github.client import GitHubClient
from src.infrastructure.mapper.vcs.github import (
    commit_dto_to_domain,
    issue_dto_to_domain,
    pull_request_dto_to_domain
)

class GitHubGateway(VcsGateway):
    """
    GitHub VCS gateway implementation
    """
    def __init__(self, client: GitHubClient):
        self._client = client

    def fetch_commits(self, repository_owner, repository_name):
        """
        Fetch commits via GitHub API call
        """
        commit_dtos = self._client.fetch_commits(repository_owner, repository_name)
        commits = [commit_dto_to_domain(dto) for dto in commit_dtos]
        if not commits:
            raise NoArtefactsException()
        return commits


    def fetch_issues(self, repository_owner, repository_name):
        """
        Fetch issues via GitHub API call
        """
        issue_dtos = self._client.fetch_issues(repository_owner, repository_name)
        issues = [issue_dto_to_domain for dto in issue_dtos]
        if not issues:
            raise NoArtefactsException()
        return issues

    def fetch_pull_requests(self, repository_owner, repository_name):
        """
        Fetch PRs via GitHub API call
        """
        pr_dtos = self._client.fetch_pull_requests(repository_owner, repository_name)
        prs = [pull_request_dto_to_domain(dto) for dto in pr_dtos]
        if not prs:
            raise NoArtefactsException()
        return prs
