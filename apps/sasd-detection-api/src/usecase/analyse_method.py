"""
src/usecase/analyse_method.py
"""
from abc import ABC, abstractmethod

from src.client.analysis import AnalysisClient
from src.model import MethodLanguage, SasdFinding
from src.strategy import MethodProcessorRegistry


class AnalyseMethodUseCase(ABC):
    """
    Orchestrates parsing and analysing method comments
    """
    @abstractmethod
    def __call__(self, method: str, language: str) -> SasdFinding:...


class AnalyseMethodUseCaseImpl(AnalyseMethodUseCase):
    """
    Orchestrates parsing and analysing method comments
    """
    def __init__(self, analysis: AnalysisClient, processor_registry: MethodProcessorRegistry):
        self._analysis = analysis
        self._processor_registry = processor_registry

    def __call__(self, method: str, language: str) -> SasdFinding:
        processor = self._processor_registry.get(MethodLanguage(language))
        parsed = processor.parse(method)
        return self._analysis.analyse_method(parsed)
