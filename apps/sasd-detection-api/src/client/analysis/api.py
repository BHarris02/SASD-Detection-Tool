"""
src/client/analysis/api.py
"""
from abc import ABC, abstractmethod

from src.client.analysis.prompts import USER_PROMPT
from src.exception import (
    IncompleteAnalysisException,
    NoArtefactsProvidedException,
    UnknownArtefactIdException
)
from src.model import Artefact, Commit, Cwe, File, Issue, SasdFinding


class AnalysisClient(ABC):
    """
    Abstract base class implemented by concrete analysis client providers
    """

    # contract methods

    @abstractmethod
    def _query_model(self, user_prompt: str) -> list[SasdFinding]:
        """
        Generic helper that queries the underlying model with any artefact type
        """

    # concrete, shared methods

    def analyse_commits(self, commits: list[Commit]) -> list[SasdFinding]:
        """
        Provide repository commits messages to model for analysis
        
        :param commits: A list of `Commit` artefacts for analysis
        
        :return list[SasdFinding]: A list of `SasdFinding` for commits positively containing SASD
        """
        formatted = "\n".join(
            f"- id: {commit.a_id} \n message: {commit.message}"
            for commit in commits
        )
        return self._analyse_artefact(commits, USER_PROMPT.format(artefacts=formatted))

    def analyse_issues(self, issues: list[Issue]) -> list[SasdFinding]:
        """
        Provide repository issues to model for analysis
        
        :param issues: A list of `Issue` artefacts for analysis
        
        :return list[SasdFinding]: A list of `SasdFinding` for issues positively containing SASD
        """
        formatted = "\n".join(
            f"- id: {issue.a_id} \n title: {issue.title} \n body: {issue.body}"
            for issue in issues
        )
        return self._analyse_artefact(issues, USER_PROMPT.format(artefacts=formatted))

    def analyse_file_content(self, file: File) -> SasdFinding:
        """
        Provide a single file to the model for analysis

        :param file: A `File` entity with content

        :return SasdFinding: The analysis findings for the file contents
        """
        formatted = f"- id: {file.a_id} \n content: {file.content}"
        findings = self._analyse_artefact([file], USER_PROMPT.format(artefacts=formatted))
        return findings[0] if findings else None

    # private helpers

    def _resolve_artefact(self, artefacts_by_id: dict[str, Artefact], artefact_id: str) -> Artefact:
        """
        Helper that identifies and returns an Artefact by its ID

        :raises UnknownArtefactIdException: Thrown when the model hallucinates an `Artefact.a_id`
        """
        if artefact_id not in artefacts_by_id:
            raise UnknownArtefactIdException()
        return artefacts_by_id[artefact_id]

    def _analyse_artefact(
            self,
            artefacts: list[Artefact],
            user_prompt: str
        ) -> list[SasdFinding]:
        """
        Generic helper that queries the model with any artefact type
        """
        if not artefacts:
            raise NoArtefactsProvidedException()

        artefacts_by_id = {artefact.a_id: artefact for artefact in artefacts}
        batch = self._query_model(user_prompt)

        if batch.reviewed_count != len(artefacts):
            raise IncompleteAnalysisException()

        return [
            SasdFinding(
                artefact=self._resolve_artefact(artefacts_by_id, finding.artefact_id),
                explanation=finding.explanation,
                severity=finding.severity,
                cwe=Cwe(
                    c_id=finding.cwe.c_id,
                    title=finding.cwe.title
                )
            )
            for finding in batch.findings
        ]
