"""
An interface to expose the required contract methods for
artifact analysis via a remote LLM API.
"""
from typing import Protocol

from domain.entity.analysis import NLPAnalysis
from domain.entity.vcs import Commit, Issue, FileContent

class NLPGateway(Protocol):
    """
    Interface that exposes required methods for the `domain` interactors.
    These methods will be implemented in the `data` layer.
    """

    def analyze_commits(self, commits: list[Commit]) -> list[NLPAnalysis]:
        """
        Pass `Commit`s to LLM API, then fetch, parse, and map
        `NLPAnalysis`s from the API responses.
        """
        ...

    def analyze_issues(self, issues: list[Issue]) -> list[NLPAnalysis]:
        """
        Pass `Issue`s to LLM API, then fetch, parse, and map
        `NLPAnalysis`s from the API responses.
        """
        ...

    def analyze_code_comments(self, source_code: str) -> NLPAnalysis:
        """
        Pass provided `str` to LLM API, then fetch, parse,
        and map `NLPAnalysis` from the API response.
        """
        ...

    def analyze_file_comments(self, content: FileContent) -> NLPAnalysis:
        """
        Pass provided `FileContent` to LLM API, then fetch, parse,
        and map `NLPAnalysis` from API response.
        """
        ...
