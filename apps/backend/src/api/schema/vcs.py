"""
Pydantic schemas to validate VCS requests and responses.
"""
from pydantic import BaseModel, Field

# GetRepositoryStructure

class GetRepositoryStructureRequest(BaseModel):
    repo_url: str

class GetRepositoryStructureResponse(BaseModel):
    response: list

# GetFileContent

class GetFileContentRequest(BaseModel):
    repo_url: str
    file_path: str

class GetFileContentResponse(BaseModel):
    response: dict[str, str]