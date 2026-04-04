"""
Concrete implementations of `NLPRepository` contract exposed in `domain` layer.
"""
from apps.backend.src.data.remote.nlp.nlp_api_service import NLPApiService
from apps.backend.src.domain.entity.analysis import NLPAnalysis
from apps.backend.src.domain.entity.vcs import Commit, FileContent, Issue
from apps.backend.src.domain.repository.nlp_repository_api import NLPRepository

class AnthropicNLPRepository(NLPRepository):
    """
    A concrete `NLPRepository` implemented using an Anthropic LLM.
    """
    def __init__(self, api_service: NLPApiService) -> None:
        self._api_service = api_service

    def analyze_commits(self, commits: list[Commit]) -> list[NLPAnalysis]:
        ...

    def analyze_issues(self, issues: list[Issue]) -> list[NLPAnalysis]:
        ...

    def analyze_code_comments(self, source_code: str) -> NLPAnalysis:
        ...

    def analyze_file_comments(self, content: FileContent) -> NLPAnalysis:
        ...
