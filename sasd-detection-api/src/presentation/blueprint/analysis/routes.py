"""
REST endpoints for analysis actions
"""
from flask import  jsonify
from flask_pydantic_spec import Request, Response
from src.presentation.blueprint.analysis import analysis_bp, _analysis_spec
from src.presentation.dto.request import AnalysisRequest, AnalyseCodeCommentsRequest
from src.presentation.dto.response import AnalysisResponse

@analysis_bp.post("/commits")
@_analysis_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_commits():
    """
    Analyse commits endpoint
    """
    return jsonify({
        "status": "not implemented"
    }), 501

@analysis_bp.post("/issues")
@_analysis_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_issues():
    """
    Analyse issues endpoint
    """
    return jsonify({
        "status": "not implemented"
    }), 501

@analysis_bp.post("/code-comments")
@_analysis_spec.validate(
    body=Request(AnalyseCodeCommentsRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_code_comments():
    """
    Analyse code comments endpoint
    """
    return jsonify({
        "status": "not implemented"
    }), 501

@analysis_bp.post("/pull-requests")
@_analysis_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_pull_requests():
    """
    Analyse pull requests endpoint
    """
    return jsonify({
        "status": "not implemented"
    }), 501

@analysis_bp.post("/repository")
@_analysis_spec.validate(
    body=Request(AnalysisRequest),
    resp=Response(HTTP_200=AnalysisResponse)
)
def analyse_repository():
    """
    Analyse repository endpoint
    """
    return jsonify({
        "status": "not implemented"
    }), 501
