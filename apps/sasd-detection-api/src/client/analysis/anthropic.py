"""
src/client/analysis/anthropic.py
"""
from anthropic import Anthropic

from src.client.analysis.api import AnalysisClient
from src.client.analysis.prompts import SYSTEM_PROMPT
from src.client.analysis.schemas import SasdFindingBatchSchema


class AnthropicClient(AnalysisClient):
    """
    Outbound port that fetches analyses of artefacts via Anthropic API call
    """
    def __init__(self, api_key: str, model: str, timeout: float = 10.0, max_tokens: int = 1024):
        self._client = Anthropic(api_key=api_key, timeout=timeout)
        self._model = model
        self._max_tokens = max_tokens

    def _query_model(self, user_prompt: str) -> list[SasdFindingBatchSchema]:
        resp = self._client.messages.parse(
            max_tokens=self._max_tokens,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            model=self._model,
            output_config=SasdFindingBatchSchema
        )

        return resp.parsed_output
