"""
src/usecase/analyse_issues.py
"""
from abc import ABC, abstractmethod

from src.client.analysis import AnalysisClient
from src.client.collection import ArtefactCollectionClient
from src.model import SasdFinding


class AnalyseIssuesUseCase(ABC):
    """
    Orchestrates fetching and analysing issues
    """
    @abstractmethod
    def __call__(self, repo_owner: str, repo_name: str) -> list[SasdFinding]: ...


class AnalyseIssuesUseCaseImpl(AnalyseIssuesUseCase):
    """
    Orchestrates fetching and analysing issues
    """
    def __init__(self, artefacts: ArtefactCollectionClient, analysis: AnalysisClient):
        self._artefacts = artefacts
        self._analysis = analysis

    def __call__(self, repo_owner: str, repo_name: str) -> list[SasdFinding]:
        issues = self._artefacts.fetch_issues(repo_owner, repo_name)
        return self._analysis.analyse_issues(issues)
