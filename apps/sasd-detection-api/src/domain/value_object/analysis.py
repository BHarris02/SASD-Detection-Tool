"""
Value objects for analysis entities
"""
from dataclasses import dataclass
from enum import Enum

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
