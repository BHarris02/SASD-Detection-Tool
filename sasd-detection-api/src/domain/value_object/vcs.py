"""
Value objects for VCS entities
"""
from dataclasses import dataclass

from src.domain.error.vcs import MalformedArtefactException

@dataclass(frozen=True)
class ArtefactLabel:
    """
    Repository-level label for issues and PRs
    """
    name: str
    description: str

    def __post_init__(self):
        if (not self.name) and (not self.description):
            raise MalformedArtefactException()
