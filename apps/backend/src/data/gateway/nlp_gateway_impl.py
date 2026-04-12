"""
Concrete implementations of `NLPGateway` contract exposed in `domain` layer.
"""
from data.client.nlp.nlp_api_service import NLPApiService
from data.mapper.analysis_entity_mapper import (
    nlp_analysis_dto_to_domain
)
from domain.entity.analysis import NLPAnalysis
from domain.entity.vcs import Commit, FileContent, Issue
from domain.gateway.nlp_gateway_api import NLPGateway

class AnthropicGateway(NLPGateway):
    """
    A concrete `NLPGateway` implemented using an Anthropic LLM.
    """
    def __init__(self, api_service: NLPApiService) -> None:
        self._api_service = api_service

    def analyze_commits(self, commits: list[Commit]) -> list[NLPAnalysis]:
        try:
            return [
                nlp_analysis_dto_to_domain(
                    self._api_service.analyze_commit(commit.message)
                )
                for commit in commits
            ]
        except Exception as e:
            raise e

    def analyze_issues(self, issues: list[Issue]) -> list[NLPAnalysis]:
        try:
            return [
                nlp_analysis_dto_to_domain(
                    self._api_service.analyze_issue(self._issue_to_str(issue))
                )
                for issue in issues
            ]
        except Exception as e:
            raise e

    def analyze_code_comments(self, source_code: str) -> NLPAnalysis:
        try:
            return nlp_analysis_dto_to_domain(
                self._api_service.analyze_comment(source_code)
            )
        except Exception as e:
            raise e

    def analyze_file_comments(self, content: FileContent) -> NLPAnalysis:
        try:
            return nlp_analysis_dto_to_domain(
                self._api_service.analyze_comment(content.content)
            )
        except Exception as e:
            raise e

    def _issue_to_str(self, issue: Issue) -> str:
        issue_str = [f"Title: {issue.title}"]

        if issue.description:
            issue_str.append(f"Description: {issue.description}")

        if issue.labels:
            label_names = ", ".join(label.name for label in issue.labels)
            issue_str.append(f"Labels: {label_names}")

        return "\n".join(issue_str)
