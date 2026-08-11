"""
src/exception/analysis.py
"""

class IncompleteAnalysisException(Exception):
    """
    Thrown when a model returns incomplete analyses
    """

class NoArtefactsProvidedException(Exception):
    """
    Thrown when an empty list is provided for analysis
    """

class UnknownArtefactIdException(Exception):
    """
    Thrown when an artefact ID is hallucinated by the model
    """
