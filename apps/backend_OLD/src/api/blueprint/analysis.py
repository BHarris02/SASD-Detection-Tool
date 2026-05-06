"""
REST endpoints for analysis functionality.
"""
from flask import Blueprint, request
from flask_pydantic_spec import Request, Response

from api.extensions import api_spec
from api.schema.analysis import (
    AnalyzeCommitsRequest,
    AnalyzeCommitsResponse
)
from api.utils.serializer import serialize
from domain.usecase.analysis.api import (
    AnalyzeCommitsUseCase
)

analysis_bp = Blueprint(
    name="analysis_bp",
    import_name=__name__,
    url_prefix="/analysis"
)

@analysis_bp.post("/commits")
@api_spec.validate(
    body=Request(AnalyzeCommitsRequest),
    resp=Response(HTTP_200=AnalyzeCommitsResponse)
)
def analyze_commits(analyze_commits: AnalyzeCommitsUseCase):
    repo_url = request.context.body.repo_url
    result = analyze_commits(repo_url)
    return serialize(result)