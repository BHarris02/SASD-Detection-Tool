"""
Application layer-specific analysis use case exceptions
"""
class NoArtefactsToAnalyseException(Exception):
    """
    Thrown when no artefacts were retrieved
    """

class NoCommentsToAnalyseException(Exception):
    """
    Thrown when no comments exist in a provided source code snippet
    """
