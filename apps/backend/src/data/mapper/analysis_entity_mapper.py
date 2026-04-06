"""
Utility mapper functions to map from analysis DTO to business entity.
"""
from data.client.nlp.dtos import (
    NLPAnalysisDto, CWEMappingDto, SASDAnalysisDto,
)
from domain.entity.analysis import (
    NLPAnalysis, CWEMapping, SASDAnalysis, SASDAnalysisSeverity
)

def _severity_str_to_domain(severity: str) -> SASDAnalysisSeverity:
    return SASDAnalysisSeverity(severity)

def sasd_analysis_dto_to_domain(dto: SASDAnalysisDto) -> SASDAnalysis:
    """
    Map `SASDAnalysisDto` to `SASDAnalysis`.
    """
    return SASDAnalysis(
        explanation=dto.explanation,
        severity=_severity_str_to_domain(dto.severity),
    )

def cwe_mapping_dto_to_domain(dto: CWEMappingDto) -> CWEMapping:
    """
    Map `CWEMappingDto` to `CWEMapping`.
    """
    return CWEMapping(
        id=dto.id,
        name=dto.name,
        description=dto.description,
    )

def nlp_analysis_dto_to_domain(dto: NLPAnalysisDto) -> NLPAnalysis:
    """
    Map `NLPAnalysisDto` to `NLPAnalysis`.
    """
    return NLPAnalysis(
        is_sasd=dto.is_sasd,
        sasd_analysis=sasd_analysis_dto_to_domain(dto.sasd_analysis) if dto.sasd_analysis else None,
        cwe_mapping=cwe_mapping_dto_to_domain(dto.cwe_mapping) if dto.cwe_mapping else None,
    )
