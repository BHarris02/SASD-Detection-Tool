"""
Pydantic schemas to validate API response shapes
"""
from typing import List, Optional

from pydantic import BaseModel

class CommitMessageDto(BaseModel):
    """
    Nested commit message DTO
    """
    message: str

class CommitDto(BaseModel):
    """
    Commit message DTO
    """
    commit: CommitMessageDto

class ArtefactLabelDto(BaseModel):
    """
    Issue label DTO
    """
    name: str
    description: Optional[str] = None

class IssueDto(BaseModel):
    """
    Issue DTO
    """
    title: str
    body: Optional[str] = None
    labels: List[ArtefactLabelDto]

class PullRequestDto(BaseModel):
    """
    Pull request DTO
    """
    title: str
    body: Optional[str] = None
    labels: List[ArtefactLabelDto]
