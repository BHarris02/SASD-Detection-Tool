"""
src/model/analysis.py
"""
from dataclasses import dataclass
from enum import StrEnum

from .artefacts import Artefact


class SasdFindingSeverity(StrEnum):
    """
    Assessed impact of a detected SASD finding
    """
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"



@dataclass(frozen=True)
class Cwe:
    """
    A Common Weakness Enumeration reference identified by the model
    """
    c_id: str
    title: str


@dataclass(frozen=True)
class SasdFinding:
    """
    Domain model/entity to describe an analysis models findings
    """
    artefact: Artefact
    explanation: str
    severity: SasdFindingSeverity
    cwe: Cwe
