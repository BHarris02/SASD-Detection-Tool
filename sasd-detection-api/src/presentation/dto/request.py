"""
Pydantic schemas modelling incoming requests
"""
from pydantic import BaseModel

class AnalysisRequest(BaseModel):
    """
    A reusable request schema for commits, issues, pull requests, and repository analysis requests
    """
    repository_owner: str
    repository_name: str

class AnalyseCodeCommentsRequest(BaseModel):
    """
    Analyse code comments request schema
    """
    source_code: str
