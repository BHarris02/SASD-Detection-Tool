"""
Module wiring together Application dependencies
"""
from injector import Module, provider, singleton

from src.application.gateway.analysis_gateway import AnalysisGateway
from src.application.gateway.vcs_gateway import VcsGateway
from src.application.usecase.analysis import (
    AnalyseCommitsUseCase,
    AnalyseIssuesUseCase,
    AnalyseCodeCommentsUseCase,
    AnalysePullRequestsUseCase
)
from src.application.usecase.analysis.impl import (
    AnalyseCommitsUseCaseImpl,
    AnalyseIssuesUseCaseImpl,
    AnalyseCodeCommentsUseCaseImpl,
    AnalysePullRequestsUseCaseImpl
)

class ApplicationModule(Module):
    """
    Wires together `application` dependencies
    """
    @provider
    @singleton
    def provide_analyse_commits_use_case(
        self,
        analysis_gateway: AnalysisGateway,
        vcs_gateway: VcsGateway
    ) -> AnalyseCommitsUseCase:
        """
        Wire up `AnalyseCommitsUseCase`
        """
        return AnalyseCommitsUseCaseImpl(analysis_gateway, vcs_gateway)

    @provider
    @singleton
    def provide_analyse_issuess_use_case(
        self,
        analysis_gateway: AnalysisGateway,
        vcs_gateway: VcsGateway
    ) -> AnalyseIssuesUseCase:
        """
        Wire up `AnalyseIssuesUseCase`
        """
        return AnalyseIssuesUseCaseImpl(analysis_gateway, vcs_gateway)

    @provider
    @singleton
    def provide_analyse_code_comments_use_case(
        self,
        analysis_gateway: AnalysisGateway
    ) -> AnalyseCodeCommentsUseCase:
        """
        Wire up `AnalyseCodeCommentsUseCase`
        """
        return AnalyseCodeCommentsUseCaseImpl(analysis_gateway)

    @provider
    @singleton
    def provide_analyse_pull_requests_use_case(
        self,
        analysis_gateway: AnalysisGateway,
        vcs_gateway: VcsGateway
    ) -> AnalysePullRequestsUseCase:
        """
        Wire up `AnalysePullRequestsUseCase`
        """
        return AnalysePullRequestsUseCaseImpl(analysis_gateway, vcs_gateway)
