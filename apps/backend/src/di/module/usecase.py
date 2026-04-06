"""
Wire together `domain` layer dependencies and exposes them via `@provider` decorated methods.
"""
from injector import provider, singleton

from apps.backend.src.domain.gateway.nlp_gateway_api import NLPGateway
from apps.backend.src.domain.repository.vcs_repository_api import VCSRepository
from apps.backend.src.domain.usecase.analysis.api import (
    AnalyzeCommitsUseCase,
    AnalyzeIssuesUseCase,
    AnalyzeCommentsUseCase,
    AnalyzeFileCommentsUseCase,
    AnalyzeRepositoryUseCase
)
from apps.backend.src.domain.usecase.analysis.impl import (
    AnalyzeCommitsUseCaseImpl,
    AnalyzeIssuesUseCaseImpl,
    AnalyzeCommentsUseCaseImpl,
    AnalyzeFileCommentsUseCaseImpl,
    AnalyzeRepositoryUseCaseImpl
)
from apps.backend.src.domain.usecase.vcs.api import (
    GetFileContentUseCase, GetRepositoryStructureUseCase
)
from apps.backend.src.domain.usecase.vcs.impl import (
    GetFileContentUseCaseImpl, GetRepositoryStructureUseCaseImpl
)

class UsecaseModule:
    """
    Wire together `domain` layer dependencies and exposes them via `@provider` decorated methods.
    """

    @provider
    @singleton
    def provide_analyze_commits(
        self,
        nlp_gateway: NLPGateway,
        vcs_repo: VCSRepository
    ) -> AnalyzeCommitsUseCase:
        """
        Provide a singleton instance of `AnalyzeCommitsUseCase`.
        """
        return AnalyzeCommitsUseCaseImpl(nlp_gateway=nlp_gateway, vcs_repo=vcs_repo)

    @provider
    @singleton
    def provide_analyze_issues(
        self,
        nlp_gateway: NLPGateway,
        vcs_repo: VCSRepository
    ) -> AnalyzeIssuesUseCase:
        """Provide a singleton instance of `AnalyzeIssuessUseCase`."""
        return AnalyzeIssuesUseCaseImpl(nlp_gateway=nlp_gateway, vcs_repo=vcs_repo)

    @provider
    @singleton
    def provide_analyze_comments(
        self,
        nlp_gateway: NLPGateway,
    ) -> AnalyzeCommentsUseCase:
        """Provide a singleton instance of `AnalyzeCommentssUseCase`."""
        return AnalyzeCommentsUseCaseImpl(nlp_gateway=nlp_gateway)

    @provider
    @singleton
    def provide_analyze_file_comments(
        self,
        nlp_gateway: NLPGateway,
        vcs_repo: VCSRepository,
    ) -> AnalyzeFileCommentsUseCase:
        """Provide a singleton instance of `AnalyzeFileCommentsUseCase`."""
        return AnalyzeFileCommentsUseCaseImpl(nlp_gateway=nlp_gateway, vcs_repo=vcs_repo)

    @provider
    @singleton
    def provide_analyze_repository(
        self,
        analyze_commits: AnalyzeCommitsUseCase,
        analyze_issues: AnalyzeIssuesUseCase,
        analyze_file_comments: AnalyzeFileCommentsUseCase,
        get_repository_structure: GetRepositoryStructureUseCase,
    ) -> AnalyzeRepositoryUseCase:
        """Provide a singleton instance of `AnalyzeRepositoryUseCase`."""
        return AnalyzeRepositoryUseCaseImpl(
            analyze_commits=analyze_commits,
            analyze_issues=analyze_issues,
            analyze_file_content=analyze_file_comments,
            get_repository_structure=get_repository_structure,
        )

    @provider
    @singleton
    def provide_get_file_content_use_case(
        self,
        repo: VCSRepository
    ) -> GetFileContentUseCase:
        """Provide a singleton instance of `GetFileContentUseCase`."""
        return GetFileContentUseCaseImpl(repo)

    @provider
    @singleton
    def provide_get_repository_structure_use_case(
        self,
        repo: VCSRepository
    ) -> GetRepositoryStructureUseCase:
        """Provide a singleton instance of `GetRepositoryStructureUseCase`."""
        return GetRepositoryStructureUseCaseImpl(repo)
