"""
Utility mapper functions to map from `data` DTO to `domain` business entity.
"""
from data.client.vcs.dtos import (
    CommitDto, IssueDto, IssueLabelDto, FileContentDto, RepositoryItemDto
)
from domain.entity.vcs import (
    Commit, Issue, IssueLabel, FileContent, RepositoryItem, RepositoryItemType
)

def commit_dto_to_domain(dto: CommitDto) -> Commit:
    """
    Map `CommitDto` to `Commit`.
    """
    return Commit(
        message=dto.message
    )

def _issue_label_dto_to_domain(dto: IssueLabelDto) -> IssueLabel:
    return IssueLabel(
        name=dto.name,
        description=dto.description
    )

def issue_dto_to_domain(dto: IssueDto) -> Issue:
    """
    Map `IssueDto` to `Issue`.
    """
    return Issue(
        title=dto.title,
        description=dto.description,
        labels=[
            _issue_label_dto_to_domain(label_dto)
            for label_dto in dto.labels
        ] if dto.labels else []
    )

def file_content_dto_to_domain(dto: FileContentDto) -> FileContent:
    """
    Map `FileContentDto` to `FileContent`.
    """
    return FileContent(
        dto.content
    )

def repository_item_dto_to_domain(dto: RepositoryItemDto) -> RepositoryItem:
    """
    Map `RepositoryItemDto` to `RepositoryItem`.
    """
    return RepositoryItem(
        name=dto.name,
        path=dto.path,
        type=RepositoryItemType(dto.type),
        children=dto.children
    )
