"""
Use case implementations
"""
from src.application.error.analysis import (
    NoArtefactsToAnalyseException,
    NoCommentsToAnalyseException
)
from src.application.gateway.analysis_gateway import AnalysisGateway
from src.application.gateway.vcs_gateway import VcsGateway
from src.application.usecase.analysis import (
    AnalyseCommitsUseCase,
    AnalyseIssuesUseCase,
    AnalyseCodeCommentsUseCase,
    AnalysePullRequestsUseCase,
    AnalyseRepositoryUseCase
)
from src.domain.entity.vcs import CodeArtefact
from src.domain.service.comment_detection import contains_comments
from src.domain.value_object.analysis import AnalysisBatch


class AnalyseCommitsUseCaseImpl(AnalyseCommitsUseCase):
    """
    Implementation of AnalyseCommitsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> AnalysisBatch:
        commits = self._vcs_gateway.fetch_commits(repository_owner, repository_name)
        if not commits:
            raise NoArtefactsToAnalyseException()
        return self._analysis_gateway.analyse_artefacts(commits)

class AnalyseIssuesUseCaseImpl(AnalyseIssuesUseCase):
    """
    Implementation of AnalyseIssuesUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> AnalysisBatch:
        issues = self._vcs_gateway.fetch_issues(repository_owner, repository_name)
        if not issues:
            raise NoArtefactsToAnalyseException()
        return self._analysis_gateway.analyse_artefacts(issues)

class AnalyseCodeCommentsUseCaseImpl(AnalyseCodeCommentsUseCase):
    """
    Implementation of AnalyseCodeCommentsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway) -> None:
        self._analysis_gateway = analysis_gateway

    def __call__(self, source_code: str) -> AnalysisBatch:
        if not contains_comments(source_code):
            raise NoCommentsToAnalyseException()
        return self._analysis_gateway.analyse_artefacts(
            [CodeArtefact(source_code=source_code)]
        )

class AnalysePullRequestsUseCaseImpl(AnalysePullRequestsUseCase):
    """
    Implementation of AnalysePullRequestsUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    def __call__(self, repository_owner: str, repository_name: str) -> AnalysisBatch:
        pull_requests = self._vcs_gateway.fetch_pull_requests(repository_owner, repository_name)
        if not pull_requests:
            raise NoArtefactsToAnalyseException()
        return self._analysis_gateway.analyse_artefacts(pull_requests)

class AnalyseRepositoryUseCaseImpl(AnalyseRepositoryUseCase):
    """
    Implementation of AnalyseRepositoryUseCase contract
    """
    def __init__(self, analysis_gateway: AnalysisGateway, vcs_gateway: VcsGateway) -> None:
        self._analysis_gateway = analysis_gateway
        self._vcs_gateway = vcs_gateway

    # TODO: Implement use case logic to orchestrate fetching and analysing all artefacts
