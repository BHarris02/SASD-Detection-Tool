"""
Concrete implementation of `NLPApiService` using Google API.
"""
import json

from google.genai import Client, types

from data.client.nlp.nlp_artifact_type import NLPArtifactType
from data.client.nlp.dtos import NLPAnalysisDto
from data.client.nlp.adapter import to_dto
from data.client.nlp.models import NLPAnalysisResponse
from data.client.nlp.nlp_api_service import NLPApiService

class GeminiApiService(NLPApiService):
    """
    Service that fetches analysis of artifacts from Google API using a Gemini model.
    """
    def __init__(self, api_token: str, model: str):
        self._client = Client(api_key=api_token)
        self._model = model

    def analyze_commit(self, commit: str):
        return self._analyze_artifact(artifact=commit, artifact_type=NLPArtifactType.COMMIT)
    
    def analyze_issue(self, issue: str) -> NLPAnalysisDto:
        return self._analyze_artifact(artifact=issue, artifact_type=NLPArtifactType.ISSUE)

    def analyze_comment(self, comment: str) -> NLPAnalysisDto:
        return self._analyze_artifact(artifact=comment, artifact_type=NLPArtifactType.COMMENT)
    
    def _analyze_artifact(self, artifact: str, artifact_type: str) -> NLPAnalysisDto:
        raw = self._client.models.generate_content(
            model=self._model,
            contents=[
                types.Content(
                    role="user",
                    parts=[
                        types.Part(
                            text=f"Analyze the following {artifact_type} for self-admitted security debt: \n\n {artifact}"
                        )
                    ]
                )
            ]
        ).text
        parsed = json.loads(raw)
        validated = NLPAnalysisResponse.model_validate(parsed)
        return to_dto(validated)
    