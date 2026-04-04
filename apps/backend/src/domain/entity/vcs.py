"""
Business entities for VCS.
"""
from dataclasses import dataclass
from enum import Enum

@dataclass
class Commit:
    """
    A commit message.
    """
    message: str

@dataclass
class IssueLabel:
    """
    An issue label.
    """
    name: str
    description: str

@dataclass
class Issue:
    """
    An issue ticket.
    """
    title: str
    description: str
    labels: list[IssueLabel]

@dataclass
class CodeSnippet:
    """
    A source code snippet.
    """
    signature: str
    body: str

@dataclass
class FileContent:
    """
    Content of a file.
    """
    content: str

class RepositoryItemType(Enum):
    """
    An enum to represent a repository item type.
    Either a file or folder.
    """
    FILE = "file"
    FOLDER = "folder"

@dataclass
class RepositoryItem:
    """
    A file or folder in a repository.
    """
    name: str
    path: str
    type: RepositoryItemType
    children: list["RepositoryItem"]
