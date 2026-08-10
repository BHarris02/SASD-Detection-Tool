"""
src/model/artefacts.py
"""
from abc import ABC
from dataclasses import dataclass


@dataclass(frozen=True)
class Artefact(ABC):
    """
    Abstract base class that represents artefacts in a repository
    """
    a_id: str


@dataclass(frozen=True)
class Commit(Artefact):
    """
    Domain model/entity for a Commit message
    """
    message: str


@dataclass(frozen=True)
class Issue(Artefact):
    """
    Domain model/entity for an Issue or Pull request
    """
    title: str
    body: str
    is_pull_request: bool


@dataclass(frozen=True)
class File(Artefact):
    """
    Domain model/entity for a source code file
    """
    content: str
