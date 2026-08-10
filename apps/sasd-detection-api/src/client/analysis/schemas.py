"""
src/client/analysis/schemas.py
"""
import re

from pydantic import BaseModel, field_validator

from src.model import SasdFindingSeverity

CWE_ID_PATTERN = re.compile(r"^CWE-\d+$")


class CweSchema(BaseModel):
    """
    Validate a model-provided CWE reference
    """
    c_id: str
    title: str

    @field_validator("c_id")
    @classmethod
    def validate_c_id_format(cls, value: str) -> str:
        if not CWE_ID_PATTERN.match(value):
            raise ValueError(f"Invalid CWE ID format: '{value}'")
        return value


class SasdFindingSchema(BaseModel):
    """
    Validate a single per-artefact SASD finding
    """
    artefact_id: str
    explanation: str
    severity: SasdFindingSeverity
    cwe: CweSchema


class SasdFindingBatchSchema(BaseModel):
    """
    Validate a batch of SASD findings
    """
    reviewed_count: int
    findings: list[SasdFindingSchema]
