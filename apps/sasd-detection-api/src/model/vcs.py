"""
src/model/vcs.py
"""

from abc import ABC
from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel


class Artefact(ABC):
    """
    Abstract base class for artefacts
    """


T = TypeVar("T", bound=Artefact)


class CommitMessage(BaseModel):
    """
    Nested commit message
    """

    message: str


class CommitArtefact(Artefact, BaseModel):
    """
    Commit message artefact
    """

    commit: CommitMessage


@dataclass
class ArtefactFetchResult(Generic[T]):
    """
    API fetch results with artefacts and skipped count
    """

    artefacts: list[T]
    skipped: int = 0
