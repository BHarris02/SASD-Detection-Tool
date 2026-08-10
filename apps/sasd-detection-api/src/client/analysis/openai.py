"""
src/client/openai.py
"""
from openai import OpenAI

from src.client.analysis.api import AnalysisClient
from src.client.analysis.prompts import USER_PROMPT, SYSTEM_PROMPT
from src.client.analysis.schemas import SasdFindingBatchSchema
from src.exception import IncompleteAnalysisException
from src.model import Commit, Cwe, SasdFinding


class OpenAiClient(AnalysisClient):
    """
    Outbound port that fetches analyses of artefacts via OpenAI API call
    """
    def __init__(self, api_url: str, token: str, model: str):
        self._client = OpenAI(base_url=api_url, api_key=token)
        self._model = model

    def analyse_commits(self, commits: list[Commit]) -> list[SasdFinding]:
        commits_by_sha = {commit.sha: commit for commit in commits}

        resp = self._client.beta.chat.completions.parse(
            model=self._model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_PROMPT}
            ],
            response_format=SasdFindingBatchSchema
        )

        batch = resp.choices[0].message.parsed

        if batch.reviewed_count != len(commits):
            raise IncompleteAnalysisException()

        return [
            SasdFinding(
                artefact=commits_by_sha[finding.artefact_id],
                explanation=finding.explanation,
                severity=finding.severity,
                cwe=Cwe(
                    c_id=finding.cwe.c_id,
                    title=finding.cwe.title
                )
            )
            for finding in batch.findings
        ]
