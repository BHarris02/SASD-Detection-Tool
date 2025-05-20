"""
Module Name: schemas.py
Description: This module provides defined Pydantic models for API requests and reponse validation.
            They ensure that data exchanged between clients and the server adhere to the defined formats.
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - pydantic
    - typing
Usage:
    Import the requred functions into your application. E.g.:
        from api.utils.schemas import AnalyzeCommitsRequest, AnalyzeIssuesRequest
"""
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

#requests
class AnalyzeCommitsRequest(BaseModel):
    repo: str = Field(...,
                      example = "owner/repo_name",
                      description = "Github respository in the format 'owner/repo'"
                      )

class AnalyzeIssuesRequest(BaseModel):
    repo: str = Field(...,
                      example = "owner/repo_name",
                      description = "Github respository in the format 'owner/repo'"
                      )
    
class AnalyzeMethodRequest(BaseModel):                            
    method_body: str = Field(...,
                             description= "The method's body including comments")
    
class AnalyzeCodeFileRequest(BaseModel):
    repo: str = Field(...,
                      example = "owner/repo",
                      description = "Github respository in the format 'owner/repo'"
                      )
    path: str = Field(...,
                      example = "src/main.py",
                      description = "File path to code file in repository")

class AnalyzeRepoRequest(BaseModel):
    repo: str = Field(
        ...,
        example="owner/repo",
        description="GitHub repository in the format 'owner/repo'"
    )

class FileContentRequest(BaseModel):
    repo: str = Field(
        ...,
        example="owner/repo",
        description="GitHub repository in the format 'owner/repo'"
    )
    file_path: str = Field(
        ...,
        example = "src/app.py",
        description="File path of the file in the repository"
    )

#responses    
class CWEAnalysisResponse(BaseModel):
    cwe_mapping: str | None = Field(None,
                                    example = "CWE-798: Use of Hard-coded Credentials")
    details: str | None = Field(None,
                                description = "Details about the CWE mapping by the model")
    
class MethodAnalysisResponse(BaseModel):
    sasd_detected: bool = Field(...,
                               example = "True",
                               description = "Whether or not SASD was detected")
    details: CWEAnalysisResponse = Field(...,
                         description = "NLP Models explanation")
    cwe_mapping: dict | None = Field(None, 
                                     description= "CWE mapping if model detected SASD")
    
    class Config:
        extra = "allow"

class CommitAnalysisResponse(BaseModel):
    commit_analysis: list = Field(...,
                                 example = [{"message": "Issue 1", "sasd_detected": True, "details": "This does not contain security debt."}]
    )

class IssueAnalysisResponse(BaseModel):
    issue_analysis: list = Field(...,
                                 example = [{"message": "Issue 1", "sasd_detected": True, "details": "This does not contain security debt."}]
    )

class CodeFileAnalysisResponse(BaseModel):
    code_analysis: List[MethodAnalysisResponse] = Field(...,
                                                        description = "Analysis results for all methods in a file")
    
class AnalyzeRepoResponse(BaseModel):
    commit_analysis: List[Dict[str, Any]] = Field(
        ...,
        description="Analysis results for commit messages"
    )
    issue_analysis: List[Dict[str, Any]] = Field(
        ...,
        description="Analysis results for issues"
    )
    code_analysis: List[Dict[str, Any]] = Field(
        ...,
        description="Analysis results for code files"
    )

class RepositoryStructureItem(BaseModel):
    name: str = Field(
        ...,
        example="folder",
        description="Name of the item (file or folder)"
    )
    type: str = Field(
        ...,
        example="folder",
        description="Type of the item, e.g., 'folder' or 'file'"
    )
    path: Optional[str] = Field(
        None,
        example="file.txt",
        description="File path if the item is a file"
    )
    children: List["RepositoryStructureItem"] = Field(
        default_factory=list,
        description="Child items if the item is a folder"
    )

class RepositoryStructureResponse(BaseModel):
    structure: List[RepositoryStructureItem] = Field(
        ...,
        description="The folder/file structure of the repository"
    )

RepositoryStructureItem.update_forward_refs()   #self-referencing

class FileContentResponse(BaseModel):
    file_content: str = Field(
        ...,
        description="The raw content of the file"
    )