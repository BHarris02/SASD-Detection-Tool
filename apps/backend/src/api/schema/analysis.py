"""
Pydantic schemas to validate analysis requests and responses.
"""
from pydantic import BaseModel

# AnalyzeCommits

class AnalyzeCommitsRequest(BaseModel):
    repo_url: str

class AnalyzeCommitsResponse(BaseModel):
    response: list
