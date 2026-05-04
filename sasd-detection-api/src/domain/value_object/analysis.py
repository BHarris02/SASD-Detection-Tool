"""
Value objects for analysis entities
"""
from dataclasses import dataclass
from enum import Enum
from typing import List

from src.domain.entity.analysis import AnalysisResult
from src.domain.entity.common import Artefact
from src.domain.error.analysis import (
    SasdAnalysisExplanationMissingException,
    CweMappingIDMissingException,
    CweMappingTitleMissingException,
    CweMappingDescriptionMissingException
)

class SasdAnalysisSeverity(Enum):
    """
    Enum for severity of detected SASD
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass(frozen=True)
class SasdAnalysis:
    """
    SASD analysis
    """
    explanation: str
    severity: SasdAnalysisSeverity

    def __post_init__(self):
        if not self.explanation:
            raise SasdAnalysisExplanationMissingException()

@dataclass(frozen=True)
class CweMapping:
    """
    CWE mapping
    """
    cwe_id: str
    title: str
    description: str

    def __post_init__(self):
        if not self.cwe_id:
            raise CweMappingIDMissingException()
        if not self.title:
            raise CweMappingTitleMissingException()
        if not self.description:
            raise CweMappingDescriptionMissingException()

class AnalysisFailureReason(Enum):
    """
    Domain-level reasons an artefact could not be analysed
    """
    MALFORMED_ARTEFACT = "malformed_artefact"
    ANALYSIS_FAILED = "analysis_failed"

@dataclass(frozen=True)
class AnalysisFailure:
    """
    Record of failure to analyse an artefact.
    Implementation-specific failure details translated at gateway boundary
    """
    artefact: Artefact
    reason: AnalysisFailureReason

@dataclass(frozen=True)
class AnalysisBatch:
    """
    Outcome of analysing a group of artefacts.
    Contains partial success results.
    """
    results: List[AnalysisResult]
    failures: List[AnalysisFailure]
