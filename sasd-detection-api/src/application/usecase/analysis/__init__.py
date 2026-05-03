"""
Use case interfaces exposed at module level
"""
from abc import ABC, abstractmethod
from typing import Any

# TODO: `domain` entities, value objects, and errors

class AnalyseCommitsUseCase(ABC):
    """
    Fetch and analyse commits orchestrator
    """
    @abstractmethod
    def __call__(self, repository_owner: str, repository_name: str) -> Any:...

class AnalyseIssuesUseCase(ABC):
    """
    Fetch and analyse issues orchestrator
    """
    @abstractmethod
    def __call__(self, repository_owner: str, repository_name: str) -> Any:...

class AnalyseCodeCommentsUseCase(ABC):
    """
    Analyse code comments orchestrator
    """
    @abstractmethod
    def __call__(self, source_code: str) -> Any:...

class AnalysePullRequestsUseCase(ABC):
    """
    Fetch and analyse pull requests orchestrator
    """
    @abstractmethod
    def __call__(self, repository_owner: str, repository_name: str) -> Any:...

class AnalyseRepositoryUseCase(ABC):
    """
    Fetch and analyse all repository artefacts orchestrator
    """
    @abstractmethod
    def __call__(self, repository_owner: str, repository_name: str) -> Any:...

# export all interfaces

__all__ = [
    "AnalyseCommitsUseCase",
    "AnalyseIssuesUseCase",
    "AnalyseCodeCommentsUseCase",
    "AnalysePullRequestsUseCase",
    "AnalyseRepositoryUseCase"
]
