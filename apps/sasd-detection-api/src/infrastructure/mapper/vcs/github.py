"""
Mapper functions mapping GitHub DTOs to VCS domain entities
"""
from typing import List, Optional

from src.domain.entity.vcs import (
    CommitArtefact,
    IssueArtefact,
    ArtefactLabel,
    PullRequestArtefact
)
from src.domain.error.vcs import MalformedArtefactException
from src.infrastructure.client.vcs.github.dtos import (
    CommitDto,
    IssueDto,
    ArtefactLabelDto,
    PullRequestDto
)

def commit_dto_to_domain(dto: CommitDto) -> Optional[CommitArtefact]:
    """
    Map `CommitDto` to `CommitArtefact`
    """
    try:
        return CommitArtefact(message=dto.commit.message)
    except MalformedArtefactException:
        return None

def label_dto_to_domain(dto: ArtefactLabelDto) -> Optional[ArtefactLabel]:
    """
    Map `ArtefactLabelDto` to `ArtefactLabel`
    """
    try:
        return ArtefactLabel(
            name=dto.name,
            description=dto.description
        )
    except MalformedArtefactException:
        return None

def issue_dto_to_domain(dto: IssueDto) -> Optional[IssueArtefact]:
    """
    Map `IssueDto` to `IssueArtefact`
    """
    try:
        return IssueArtefact(
            title=dto.title,
            body=dto.body,
            labels=_map_artefact_label_dtos(dto.labels)
        )
    except MalformedArtefactException:
        return None

def pull_request_dto_to_domain(dto: PullRequestDto) -> Optional[PullRequestArtefact]:
    """
    Map `PullRequestDto` to `PullRequestArtefact`
    """
    try:
        return PullRequestArtefact(
            title=dto.title,
            body=dto.body,
            labels=_map_artefact_label_dtos(dto.labels)
        )
    except MalformedArtefactException:
        return None

def _map_artefact_label_dtos(labels: List[ArtefactLabelDto]) -> List[ArtefactLabel]:
    if not labels:
        return []
    mapped = [label_dto_to_domain(dto) for dto in labels]
    return [label for label in mapped if label is not None]
