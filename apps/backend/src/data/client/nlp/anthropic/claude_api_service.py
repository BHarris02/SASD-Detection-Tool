"""
Concrete implementation of `NLPApiService` using Anthropic API.
"""
from json import loads

from anthropic import Anthropic
from anthropic.types import TextBlock

from data.client.nlp.nlp_artifact_type import NLPArtifactType
from data.client.nlp.dtos import (
    NLPAnalysisDto
)
from data.client.nlp.adapter import to_dto
from data.client.nlp.models import NLPAnalysisResponse
from data.client.nlp.nlp_api_service import NLPApiService

class ClaudeApiService(NLPApiService):
    """
    Service that fetches analysis of artifacts from Anthopic API using Claude model.
    """

    _SYSTEM_PROMPT = """
        You are a security debt analysis expert specialising in detecting Self-Admitted Security Debt (SASD) in software project artefacts.
        
        Analyse the provided artefact and respond ONLY with a JSON object matching this structure, with no preamble, markdown, or explanation:
        {
            "is_sasd": <bool>,
            "sasd_analysis": {
                "explanation": <str>,
                "severity": <"Low" | "Medium" | "High" | "Critical">
            } | null,
            "cwe_mapping": {
                "id": <str>,
                "name": <str>,
                "description": <str>
            } | null
        }
        
        Rules:
        - Set "is_sasd" to true if the artefact contains self-admitted security debt, false otherwise.
        - If "is_sasd" is true, populate "sasd_analysis" and "cwe_mapping" with the most relevant CWE entry.
        - If "is_sasd" is false, set both "sasd_analysis" and "cwe_mapping" to null.
    """

    def __init__(self, api_token: str, base_url: str, model: str) -> None:
        self._client = Anthropic(api_key=api_token, base_url=base_url)
        self._model = model

    def analyze_commit(self, commit: str) -> NLPAnalysisDto:
        return self._analyze_artifact(artifact=commit, artifact_type=NLPArtifactType.COMMIT)

    def analyze_issue(self, issue: str) -> NLPAnalysisDto:
        return self._analyze_artifact(artifact=issue, artifact_type=NLPArtifactType.ISSUE)

    def analyze_comment(self, comment: str) -> NLPAnalysisDto:
        return self._analyze_artifact(artifact=comment, artifact_type=NLPArtifactType.COMMENT)

    def _analyze_artifact(self, artifact: str, artifact_type: str) -> NLPAnalysisDto:
        resp = self._client.messages.create(
            model=self._model,
            max_tokens=1024,
            system=self._SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": f"""
                        Analyze the following {artifact_type} for self-admitted security debt:
                        \n\n {artifact}
                    """
                }
            ]
        )
        text_block = next(
            block for block in resp.content
            if isinstance(block, TextBlock)
        )
        raw = loads(text_block.text)
        validated = NLPAnalysisResponse.model_validate(raw)
        return to_dto(validated)
