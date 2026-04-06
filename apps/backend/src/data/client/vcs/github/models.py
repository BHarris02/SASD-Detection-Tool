"""
GitHub specific DTO validators.
"""
from pydantic import BaseModel

from apps.backend.src.data.remote.vcs.dtos import (
    CommitDto, IssueDto, FileContentDto
)

class GitHubCommitResponse(BaseModel):
    """
    `CommitDto` validator.
    """
    commit: CommitDto

class GitHubIssueResponse(BaseModel):
    """
    `IssueDto` validator.
    """
    issue: IssueDto

class GitHubFileContentResponse(BaseModel):
    """
    `FileContentDto` validator.
    """
    file_content: FileContentDto
