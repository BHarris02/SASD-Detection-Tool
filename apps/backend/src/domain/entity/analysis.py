"""
Business entities for analysis.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class SASDAnalysisSeverity(Enum):
    """
    An enum representing the severity level of detected SASD.
    """
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

@dataclass
class SASDAnalysis:
    """
    SASD information from LLM API.
    """
    explanation: str
    severity: SASDAnalysisSeverity

@dataclass
class CWEMapping:
    """
    CWE mapping for detected SASD instances.
    """
    id: str
    name: str
    description: str

@dataclass
class NLPAnalysis:
    """
    Analysis returned from LLM API.
    """
    is_sasd: bool
    sasd_analysis: Optional[SASDAnalysis]
    cwe_mapping: Optional[CWEMapping]
