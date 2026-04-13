"""
Enum constants for NLP API artifact types.
"""
from enum import StrEnum

class NLPArtifactType(StrEnum):
    COMMIT = "commit message"
    ISSUE = "issue"
    COMMENT = "code comment"
