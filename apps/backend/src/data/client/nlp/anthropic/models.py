"""
Anthropic specific DTO validators using Pydantic.
"""
from typing import Optional

from pydantic import BaseModel

class _AnthropicSASDAnalysisResponse(BaseModel):
    explanation: str
    severity: str

class _AnthropicCWEMappingResponse(BaseModel):
    id: str
    name: str
    description: str

class AnthropicNLPAnalysisResponse(BaseModel):
    """
    Anthropic API response validator.
    """
    is_sasd: bool
    sasd_analysis: Optional[_AnthropicSASDAnalysisResponse]
    cwe_mapping: Optional[_AnthropicCWEMappingResponse]
