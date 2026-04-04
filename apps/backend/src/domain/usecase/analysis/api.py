"""
Interactor interfaces to expose available NLP analysis interactors to dependent layers, 
whilst hiding implementation details.
"""
from typing import Protocol

from apps.backend.src.domain.common.result import Result
from apps.backend.src.domain.entity.analysis import NLPAnalysis

class AnalyzeCommitsUseCase(Protocol):
    """
    Interface to expose commit analysis interactor to `api` layer.
    """
    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        """
        Calls `VCSRepository().get_commits(repo_url)` and passes returned `Commit`s to 
        `NLPRepository().analyze_commits(commits)`.
        """
        ...

class AnalyzeIssuesUseCase(Protocol):
    """
    Interface to expose issue analysis interactor to `api` layer.
    """
    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        """
        Calls `VCSRepository().get_issues(repo_url)` and passes returned `Issue`s to 
        `NLPRepository().analyze_issues(issues)`.
        """
        ...

class AnalyzeCommentsUseCase(Protocol):
    """
    Interface to expose comment analysis interactor to `api` layer.
    """
    def __call__(self, source_code: str) -> Result[NLPAnalysis]:
        """
        Passes provided `source_code` to `NLPRepository().analyze_comments(source_code)`.
        """
        ...

class AnalyzeFileCommentsUseCase(Protocol):
    """
    Interface to expose file comment analysis interactor to `api` layer.
    """
    def __call__(self, repo_url: str, file_path: str) -> Result[NLPAnalysis]:
        """
        Calls `VCSRepository().get_file_content(repo_url, file_path)` and passes 
        returned `FileContent`to `NLPRepository().analyze_file_comments(file_content)`.
        """
        ...

class AnalyzeRepositoryUseCase(Protocol):
    """
    Interface to expose entire repository analysis interactor to `api` layer.
    """
    def __call__(self, repo_url: str) -> Result[list[NLPAnalysis]]:
        """
        An orchestrator that calls: 
        - `AnalyzeCommitsUseCase(repo_url)`
        - `AnalyzeIssuesUseCase(repo_url)`
        - `GetRepositoryStructureUseCase(repo_url)` 
            then calls `AnalyzeFileCommentsUseCase(repo_url, file_path)` 
            for each `RepositoryItem` returned.
        """
        ...
