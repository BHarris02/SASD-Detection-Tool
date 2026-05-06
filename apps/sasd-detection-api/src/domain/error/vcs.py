"""
Domain errors specific to version control system
"""
class MalformedArtefactException(Exception):
    """
    Exception thrown when attempting to construct an artefact with missing data
    """

class NoArtefactsException(Exception):
    """
    Exception thrown if no artefacts were successfully retrieved
    """
