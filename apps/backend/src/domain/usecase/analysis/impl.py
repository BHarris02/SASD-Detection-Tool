"""
Concrete interactors for NLP analysis.
"""
from apps.backend.src.domain.common.error import DomainError
from apps.backend.src.domain.common.result import Result
from apps.backend.src.domain.entity.analysis import NLPAnalysis
from apps.backend.src.domain.repository.nlp_repository import NLPRepository
from apps.backend.src.domain.repository.vcs_repository import VCSRepository
from apps.backend.src.domain.usecase.analysis.api import (
    AnalyzeCommitsUseCase, 
    AnalyzeIssuesUseCase,
    AnalyzeCommentsUseCase,
    AnalyzeFileCommentsUseCase,
    AnalyzeRepositoryUseCase
)
from apps.backend.src.domain.usecase.vcs.api import GetRepositoryStructureUseCase

class AnalyzeCommitsUseCaseImpl(AnalyzeCommitsUseCase):
    """
    Analyze a repository's commit messages.
    """
    def __init__(self, nlp_repo: NLPRepository, vcs_repo: VCSRepository) -> None:
        self._nlp_repo = nlp_repo
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        try:
            commits = self._vcs_repo.get_commits(repo_url)
            analysis = self._nlp_repo.analyze_commits(commits)
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
    def __init__(self, nlp_repo: NLPRepository, vcs_repo: VCSRepository) -> None:
        self._nlp_repo = nlp_repo
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        try:
            issues = self._vcs_repo.get_issues(repo_url)
            analysis = self._nlp_repo.analyze_issues(issues)
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
    def __init__(self, nlp_repo: NLPRepository) -> None:
        self._nlp_repo = nlp_repo

    def __call__(self, source_code: str) -> Result[NLPAnalysis]:
        try:
            analysis = self._nlp_repo.analyze_code_comments(source_code)
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
    def __init__(self, nlp_repo: NLPRepository, vcs_repo: VCSRepository) -> None:
        self._nlp_repo = nlp_repo
        self._vcs_repo = vcs_repo

    def __call__(self, repo_url: str, file_path: str) -> Result[NLPAnalysis]:
        try:
            file_content = self._vcs_repo.get_file_content(repo_url, file_path)
            analysis = self._nlp_repo.analyze_file_comments(file_content)
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
