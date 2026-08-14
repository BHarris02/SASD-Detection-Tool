"""
src/blueprint/analysis/routes.py
"""
from flask import Blueprint, request
from flask_pydantic_spec import Request, Response

from src.blueprint.analysis.schemas import AnalysisRequest, AnalyseMethodRequest, AnalysisResponse
from src.extensions import app_spec
from src.usecase import (
    AnalyseCommitsUseCase,
    AnalyseFileUseCase,
    AnalyseIssuesUseCase,
    AnalyseMethodUseCase
)


analysis_bp = Blueprint(name="analysis_bp", import_name=__name__, url_prefix="/analysis")

@analysis_bp.post("/commits")
@app_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_commits_route(analyse_commits: AnalyseCommitsUseCase):
    """
    Analyse commits endpoint
    """
    req: AnalysisRequest = request.context.body
    findings = analyse_commits(req.repository_owner, req.repository_name)
    return AnalysisResponse.from_findings(findings).model_dump()


@analysis_bp.post("/issues")
@app_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_issues_route(analyse_issues: AnalyseIssuesUseCase):
    """
    Analyse issues endpoint
    """
    req: AnalysisRequest = request.context.body
    findings = analyse_issues(req.repository_owner, req.repository_name)
    return AnalysisResponse.from_findings(findings).model_dump()


@analysis_bp.post("/file")
@app_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_file_route(analyse_file_content: AnalyseFileUseCase):
    """
    Analyse file endpoint
    """
    req: AnalysisRequest = request.context.body
    findings = analyse_file_content(req.repository_owner, req.repository_name, req.file_path)
    return AnalysisResponse.from_findings(findings).model_dump()


@analysis_bp.post("/method")
@app_spec.validate(
    body=Request(AnalyseMethodRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_method_route(analyse_method: AnalyseMethodUseCase):
    """
    Analyse method comments route
    """
    req: AnalyseMethodRequest = request.context.body
    findings = analyse_method(req.method, req.language)
    return AnalysisResponse.from_findings(findings).model_dump()
