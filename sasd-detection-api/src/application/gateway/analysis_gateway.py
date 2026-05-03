"""
Analysis gateway interface
"""
from abc import ABC, abstractmethod
from typing import Any

class AnalysisGateway(ABC):
    """
    Analysis gateway
    """
    @abstractmethod
    def analyse_artefacts(self, artefact: Any) -> Any:
        """
        Analyse an artefact for self-admitted security debt
        """
