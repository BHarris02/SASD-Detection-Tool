"""
Utility adapter function to map raw API responses to DTO.
"""
from data.client.nlp.dtos import (
    NLPAnalysisDto, SASDAnalysisDto, CWEMappingDto
)
from data.client.nlp.anthropic.models import AnthropicNLPAnalysisResponse

def to_dto(resp: AnthropicNLPAnalysisResponse) -> NLPAnalysisDto:
    """
    Map `AnthropicNLPAnalysisResponse` into `NLPAnalysisDto`.
    """
    sasd_dto = (
        SASDAnalysisDto(
            explanation=resp.sasd_analysis.explanation,
            severity=resp.sasd_analysis.severity
        )
        if resp.sasd_analysis else None
    )

    cwe_dto = (
        CWEMappingDto(
            id=resp.cwe_mapping.id,
            name=resp.cwe_mapping.name,
            description=resp.cwe_mapping.description
        )
        if resp.cwe_mapping else None
    )

    return NLPAnalysisDto(
        is_sasd=resp.is_sasd,
        sasd_analysis=sasd_dto,
        cwe_mapping=cwe_dto
    )
