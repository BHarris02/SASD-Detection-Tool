"""
Interface to expose the required methods for analyzing artifacts.
"""
from typing import Protocol

from data.client.nlp.dtos import NLPAnalysisDto

class NLPApiService(Protocol):
    """
    Interface that exposes required methods for concrete `NLPApiService` classes.
    """

    def analyze_commit(self, commit: str) -> NLPAnalysisDto:
        """
        Fetch & parse commit `NLPAnalysisDto` from LLM API.
        """
        ...

    def analyze_issue(self, issue: str) -> NLPAnalysisDto:
        """
        Fetch & parse issue `NLPAnalysisDto` from LLM API.
        """
        ...

    def analyze_comment(self, comment: str) -> NLPAnalysisDto:
        """
        Fetch & parse source code comment `NLPAnalysisDto` from LLM API.
        """
        ...
