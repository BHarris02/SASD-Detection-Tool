"""
Analysis entities
"""
from dataclasses import dataclass
from typing import Optional

from src.domain.entity.common import Artefact
from src.domain.error.analysis import (
    SasdAnalysisMissingException,
    CweMappingMissingException,
    MalformedAnalysisException
)
from src.domain.value_object.analysis import SasdAnalysis, CweMapping

@dataclass
class AnalysisResult:
    """
    Analysis result
    """
    artefact: Artefact
    is_sasd: bool
    sasd_analysis: Optional[SasdAnalysis]
    cwe_mapping: Optional[CweMapping]

    def __post_init__(self):
        if self.is_sasd:
            if not self.sasd_analysis:
                raise SasdAnalysisMissingException()
            if not self.cwe_mapping:
                raise CweMappingMissingException()
        else:
            if (self.sasd_analysis is not None) or (self.cwe_mapping is not None):
                raise MalformedAnalysisException()
