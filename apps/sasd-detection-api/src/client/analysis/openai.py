"""
src/client/openai.py
"""
from openai import OpenAI

from src.client.analysis.api import AnalysisClient
from src.client.analysis.prompts import SYSTEM_PROMPT
from src.client.analysis.schemas import SasdFindingBatchSchema


class OpenAiClient(AnalysisClient):
    """
    Outbound port that fetches analyses of artefacts via OpenAI API call
    """
    def __init__(self, api_url: str, token: str, model: str):
        self._client = OpenAI(base_url=api_url, api_key=token)
        self._model = model

    def _query_model(self, user_prompt: str) -> list[SasdFindingBatchSchema]:
        resp = self._client.beta.chat.completions.parse(
            model=self._model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            response_format=SasdFindingBatchSchema
        )

        return resp.choices[0].message.parsed
