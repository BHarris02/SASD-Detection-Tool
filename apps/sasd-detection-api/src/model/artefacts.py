"""
src/model/artefacts.py
"""
from abc import ABC
from dataclasses import dataclass

class Artefact(ABC):
    """
    Abstract base class that represents artefacts in a repository
    """


@dataclass(frozen=True)
class Commit(Artefact):
    """
    Domain model/entity for a Commit message
    """
    sha: str
    message: str


@dataclass(frozen=True)
class Issue(Artefact):
    """
    Domain model/entity for an Issue or Pull request
    """
    number: str
    title: str
    body: str
    is_pull_request: bool


@dataclass(frozen=True)
class File(Artefact):
    """
    Domain model/entity for a source code file
    """
    sha: str
    content: str
