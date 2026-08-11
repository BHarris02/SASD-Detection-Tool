"""
src/usecase/analyse_file.py
"""
from abc import ABC, abstractmethod

from src.client.analysis import AnalysisClient
from src.client.collection import ArtefactCollectionClient
from src.model import SasdFinding


class AnalyseFileUseCase(ABC):
    """
    Orchestrates fetching and analysing a file's content
    """
    @abstractmethod
    def __call__(self, repo_owner: str, repo_name: str, file_path: str) -> SasdFinding: ...


class AnalyseFileUseCaseImpl(AnalyseFileUseCase):
    """
    Orchestrates fetching and analysing a file's content
    """
    def __init__(self, artefacts: ArtefactCollectionClient, analysis: AnalysisClient):
        self._artefacts = artefacts
        self._analysis = analysis

    def __call__(self, repo_owner: str, repo_name: str, file_path: str) -> SasdFinding:
        file = self._artefacts.fetch_file(repo_owner, repo_name, file_path)
        return self._analysis.analyse_file_content(file)
