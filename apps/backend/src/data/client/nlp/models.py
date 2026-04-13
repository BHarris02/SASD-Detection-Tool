"""
Shared Pydantic validators for NLP API responses.
"""
from typing import Optional

from pydantic import BaseModel

class SASDAnalysisResponse(BaseModel):
    explanation: str
    severity: str

class CWEMappingResponse(BaseModel):
    id: str
    name: str
    description: str

class NLPAnalysisResponse(BaseModel):
    """
    Shared NLP API response validator.
    """
    is_sasd: bool
    sasd_analysis: Optional[SASDAnalysisResponse] = None
    cwe_mapping: Optional[CWEMappingResponse] = None
