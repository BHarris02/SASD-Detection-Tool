"""
Version control system entities
"""
from dataclasses import dataclass
from typing import List

from src.domain.entity.common import Artefact
from src.domain.error.vcs import MalformedArtefactException
from src.domain.value_object.vcs import ArtefactLabel

@dataclass
class CommitArtefact(Artefact):
    """
    Commit artefact
    """
    message: str

    def __post_init__(self):
        if not str:
            raise MalformedArtefactException()

@dataclass
class IssueArtefact(Artefact):
    """
    Issue artefact
    """
    title: str
    body: str
    labels: List[ArtefactLabel]

    def __post_init__(self):
        if (not self.title) and (not self.body):
            raise MalformedArtefactException()

@dataclass
class CodeArtefact(Artefact):
    """
    Source code artefact
    """
    source_code: str

    def __post_init__(self):
        if not self.source_code:
            raise MalformedArtefactException()

@dataclass
class PullRequestArtefact(Artefact):
    """
    Pull request artefact
    """
    title: str
    body: str
    labels: List[ArtefactLabel]

    def __post_init__(self):
        if (not self.title) and (not self.body):
            raise MalformedArtefactException()
