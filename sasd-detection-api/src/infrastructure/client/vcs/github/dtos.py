"""
Pydantic schemas to validate API response shapes
"""
from typing import List, Optional

from pydantic import BaseModel

class CommitDto(BaseModel):
    """
    Commit message DTO
    """
    message: str

class ArtefactLabelDto(BaseModel):
    """
    Issue label DTO
    """
    name: str
    description: Optional[str]

class IssueDto(BaseModel):
    """
    Issue DTO
    """
    title: str
    body: Optional[str]
    labels: List[ArtefactLabelDto]

class PullRequestDto(BaseModel):
    """
    Pull request DTO
    """
    title: str
    body: Optional[str]
    labels: List[ArtefactLabelDto]
