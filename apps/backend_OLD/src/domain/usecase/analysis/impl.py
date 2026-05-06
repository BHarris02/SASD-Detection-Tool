"""
Concrete interactors for NLP analysis.
"""
from domain.common.error import DomainError
from domain.common.result import Result
from domain.entity.analysis import NLPAnalysis
from domain.gateway.nlp_gateway_api import NLPGateway
from domain.repository.vcs_repository_api import VCSRepository
from domain.usecase.analysis.api import (
    AnalyzeCommitsUseCase,
    AnalyzeIssuesUseCase,
    AnalyzeCommentsUseCase,
    AnalyzeFileCommentsUseCase,
    AnalyzeRepositoryUseCase
)
from domain.usecase.vcs.api import GetRepositoryStructureUseCase

class AnalyzeCommitsUseCaseImpl(AnalyzeCommitsUseCase):
    """
    Analyze a repository's commit messages.
    """
    def __init__(self, nlp_gateway: NLPGateway, vcs_repo: VCSRepository) -> None:
        self._nlp_gateway = nlp_gateway
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        try:
            commits = self._vcs_repo.get_commits(repo_url)
            analysis = self._nlp_gateway.analyze_commits(commits)
            return Result(
                success=True,
                value=analysis
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )

class AnalyzeIssuesUseCaseImpl(AnalyzeIssuesUseCase):
    """
    Analyze a repository's issues.
    """
    def __init__(self, nlp_gateway: NLPGateway, vcs_repo: VCSRepository) -> None:
        self._nlp_gateway = nlp_gateway
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        try:
            issues = self._vcs_repo.get_issues(repo_url)
            analysis = self._nlp_gateway.analyze_issues(issues)
            return Result(
                success=True,
                value=analysis
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )

class AnalyzeCommentsUseCaseImpl(AnalyzeCommentsUseCase):
    """
    Analyze a code snippet's comments.
    """
    def __init__(self, nlp_gateway: NLPGateway) -> None:
        self._nlp_gateway = nlp_gateway

    def __call__(self, source_code: str) -> Result[NLPAnalysis]:
        try:
            analysis = self._nlp_gateway.analyze_code_comments(source_code)
            return Result(
                success=True,
                value=analysis
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )

class AnalyzeFileCommentsUseCaseImpl(AnalyzeFileCommentsUseCase):
    """
    Analyze a file's comments.
    """
    def __init__(self, nlp_gateway: NLPGateway, vcs_repo: VCSRepository) -> None:
        self._nlp_gateway = nlp_gateway
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str, file_path: str) -> Result[NLPAnalysis]:
        try:
            file_content = self._vcs_repo.get_file_content(repo_url, file_path)
            analysis = self._nlp_gateway.analyze_file_comments(file_content)
            return Result(
                success=True,
                value=analysis
            )
        except DomainError as e:
            return Result(
                success=False,
                value=None,
                error=e
            )
        
class AnalyzeRepositoryUseCaseImpl(AnalyzeRepositoryUseCase):
    """
    Analyze all artifacts in a repository.
    """
    def __init__(
            self, 
            analyze_commits: AnalyzeCommitsUseCase,
            analyze_issues: AnalyzeIssuesUseCase,
            analyze_file_content: AnalyzeFileCommentsUseCase,
            get_repository_structure: GetRepositoryStructureUseCase
        ) -> None:
        self._analyze_commits = analyze_commits
        self._analyze_issues = analyze_issues
        self._analyze_file_content = analyze_file_content
        self._get_repo_structure = get_repository_structure

    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        return Result(
            success=False,
            value=None,
            error=DomainError("Not implemented.")
        )
