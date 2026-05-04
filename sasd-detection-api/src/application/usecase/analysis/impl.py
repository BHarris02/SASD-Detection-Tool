"""
Use case implementations
"""
from typing import Any

from src.application.gateway.analysis_gateway import AnalysisGateway
from src.application.gateway.vcs_gateway import VcsGateway
from src.application.usecase.analysis import (
    AnalyseCommitsUseCase,
    AnalyseIssuesUseCase,
    AnalyseCodeCommentsUseCase,
    AnalysePullRequestsUseCase,
    AnalyseRepositoryUseCase
)

class AnalyseCommitsUseCaseImpl(AnalyseCommitsUseCase):
    """
    Implementation of AnalyseCommitsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> Any:
        commits = self._vcs_gateway.fetch_commits(repository_owner, repository_name)
        commits_analysis = self._analysis_gateway.analyse_artefacts(commits)
        return commits_analysis

class AnalyseIssuesUseCaseImpl(AnalyseIssuesUseCase):
    """
    Implementation of AnalyseIssuesUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> Any:
        issues = self._vcs_gateway.fetch_issues(repository_owner, repository_name)
        issues_analysis = self._analysis_gateway.analyse_artefacts(issues)
        return issues_analysis

class AnalyseCodeCommentsUseCaseImpl(AnalyseCodeCommentsUseCase):
    """
    Implementation of AnalyseCodeCommentsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, source_code: str) -> Any:
        code_comments_analysis = self._analysis_gateway.analyse_artefacts(source_code)
        return code_comments_analysis

class AnalysePullRequestsUseCaseImpl(AnalysePullRequestsUseCase):
    """
    Implementation of AnalysePullRequestsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> Any:
        pull_requests = self._vcs_gateway.fetch_pull_requests(repository_owner, repository_name)
        pull_request_analysis = self._analysis_gateway.analyse_artefacts(pull_requests)
        return pull_request_analysis

class AnalyseRepositoryUseCaseImpl(AnalyseRepositoryUseCase):
    """
    Implementation of AnalyseRepositoryUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    # TODO: Implement use case logic to orchestrate fetching and analysing all artefacts
