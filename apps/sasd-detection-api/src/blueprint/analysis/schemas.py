"""
src/blueprint/analysis/schemas.py
"""
from typing import Optional

from pydantic import BaseModel

from src.model import SasdFinding, SasdFindingSeverity


class AnalysisRequest(BaseModel):
    """
    Validate an incoming analysis request
    """
    repository_owner: str
    repository_name: str
    file_path: Optional[str] = None


class CweResponse(BaseModel):
    """
    Serialise a CWE reference for an API response
    """
    c_id: str
    title: str


class SasdFindingResponse(BaseModel):
    """
    Serialise a single SASD finding for an API response
    """
    artefact_id: str
    explanation: str
    severity: SasdFindingSeverity
    cwe: CweResponse


class AnalysisResponse(BaseModel):
    """
    Validate an outgoing analysis response
    """
    findings: list[SasdFindingResponse]

    @classmethod
    def from_findings(cls, findings: list[SasdFinding]) -> "AnalysisResponse":
        """
        Map from `SasdFinding` to `AnalysisResponse
        """
        return cls(
            findings=[
                SasdFindingResponse(
                    artefact_id=finding.artefact.a_id,
                    explanation=finding.explanation,
                    severity=finding.severity,
                    cwe=CweResponse(
                        c_id=finding.cwe.c_id,
                        title=finding.cwe.title
                    )
                )
                for finding in findings
            ]
        )
