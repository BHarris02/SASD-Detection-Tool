"""
Domain specific errors for analysis
"""

# AnalysisResult entity errors

class SasdAnalysisMissingException(Exception):
    """
    Missing SasdAnalysis on AnalysisResult
    """

class CweMappingMissingException(Exception):
    """
    Missing CweMapping on AnalysisResult
    """

class MalformedAnalysisException(Exception):
    """
    Malformed AnalysisResult
    """

# SasdAnalysis value object errors

class SasdAnalysisExplanationMissingException(Exception):
    """
    Missing explanantion on SasdAnalysis
    """

# CweMapping value object errors

class CweMappingIDMissingException(Exception):
    """
    Missing cwe_id on CweMapping
    """

class CweMappingTitleMissingException(Exception):
    """
    Missing cwe_title on CweMapping
    """

class CweMappingDescriptionMissingException(Exception):
    """
    Missing cwe_description on CweMapping
    """
