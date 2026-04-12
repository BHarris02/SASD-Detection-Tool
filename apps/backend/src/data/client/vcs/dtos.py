"""
Pydantic DTOs to validate raw responses from VCS API calls.
"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class CommitDto:
    """
    Commit message DTO.
    """
    message: str

@dataclass
class IssueLabelDto:
    """
    Issue label DTO.
    """
    name: str
    description: str

@dataclass
class IssueDto:
    """
    Issue DTO.
    """
    title: str
    description: Optional[str]
    labels: Optional[list[IssueLabelDto]]

@dataclass
class FileContentDto:
    """
    File content DTO.
    """
    content: str

@dataclass
class RepositoryItemDto:
    """
    Repository tree item DTO.
    """
    name: str
    path: str
    type: str
    children: list["RepositoryItemDto"]
