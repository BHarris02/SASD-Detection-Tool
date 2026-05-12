"""
Aggregated analysis entities
"""
from dataclasses import dataclass
from typing import List

from src.domain.entity.analysis import AnalysisResult, AnalysisFailure

@dataclass(frozen=True)
class AnalysisBatch:
    """
    Outcome of analysing a group of artefacts.
    Contains partial success results.
    """
    results: List[AnalysisResult]
    failures: List[AnalysisFailure]
