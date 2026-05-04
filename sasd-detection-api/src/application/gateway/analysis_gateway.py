"""
Analysis gateway interface
"""
from abc import ABC, abstractmethod
from typing import List

from src.domain.value_object.analysis import AnalysisBatch
from src.domain.entity.common import Artefact

class AnalysisGateway(ABC):
    """
    Analysis gateway
    """
    @abstractmethod
    def analyse_artefacts(self, artefacts: List[Artefact]) -> AnalysisBatch:
        """
        Analyse artefacts for self-admitted security debt.
        Return partial success results
        """
