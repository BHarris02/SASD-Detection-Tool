"""
DTOs for raw responses from LLM API calls.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class SASDAnalysisDto:
    """
    SASD info DTO.
    """
    explanation: str
    severity: str

@dataclass
class CWEMappingDto:
    """
    CWE mapping DTO.
    """
    id: str
    name: str
    description: str

@dataclass
class NLPAnalysisDto:
    """
    Analysis DTO.
    """
    is_sasd: bool
    sasd_analysis: Optional[SASDAnalysisDto]
    cwe_mapping: Optional[CWEMappingDto]
