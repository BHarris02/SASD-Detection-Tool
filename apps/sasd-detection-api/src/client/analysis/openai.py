"""
src/client/openai.py
"""
from openai import OpenAI

from src.client.analysis.api import AnalysisClient
from src.client.analysis.prompts import USER_PROMPT, SYSTEM_PROMPT
from src.client.analysis.schemas import SasdFindingBatchSchema
from src.exception import IncompleteAnalysisException
from src.model import Artefact, Commit, Cwe, SasdFinding


class OpenAiClient(AnalysisClient):
    """
    Outbound port that fetches analyses of artefacts via OpenAI API call
    """
    def __init__(self, api_url: str, token: str, model: str):
        self._client = OpenAI(base_url=api_url, api_key=token)
        self._model = model

    def analyse_commits(self, commits: list[Commit]) -> list[SasdFinding]:
        formatted = "\n".join(
            f"- id: {commit.a_id} \n message: {commit.message}"
            for commit in commits
        )
        return self._analyse_artefact(commits, USER_PROMPT.format(artefacts=formatted))

    def _analyse_artefact(self, artefacts: list[Artefact], user_prompt: str) -> list[SasdFinding]:
        """
        Generic helper that queries the model with any artefact type
        """
        artefacts_by_id = {artefact.a_id: artefact for artefact in artefacts}

        resp = self._client.beta.chat.completions.parse(
            model=self._model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            response_format=SasdFindingBatchSchema
        )

        batch = resp.choices[0].message.parsed

        if batch.reviewed_count != len(artefacts):
            raise IncompleteAnalysisException()

        return [
            SasdFinding(
                artefact=artefacts_by_id[finding.artefact_id],
                explanation=finding.explanation,
                severity=finding.severity,
                cwe=Cwe(
                    c_id=finding.cwe.c_id,
                    title=finding.cwe.title
                )
            )
            for finding in batch.findings
        ]
