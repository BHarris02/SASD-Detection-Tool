"""
REST endpoints for VCS functionality.
"""
from flask import Blueprint, request
from flask_pydantic_spec import Response

from api.extensions import api_spec
from api.schema.vcs import (
    GetRepositoryStructureRequest,
    GetRepositoryStructureResponse,
    GetFileContentRequest,
    GetFileContentResponse
)
from api.utils.serializer import serialize
from domain.usecase.vcs.api import (
    GetFileContentUseCase,
    GetRepositoryStructureUseCase
)

vcs_bp = Blueprint(
    name="vcs_bp",
    import_name=__name__,
    url_prefix="/vcs"
)

@vcs_bp.get("/repo-structure")
@api_spec.validate(
    query=GetRepositoryStructureRequest,
    resp=Response(HTTP_200=GetRepositoryStructureResponse)
)
def get_repository_structure(get_repository_structure: GetRepositoryStructureUseCase):
    repo_url = request.args.get("repo_url")
    result = get_repository_structure(repo_url)
    return serialize(result)


@vcs_bp.get("/file-content")
@api_spec.validate(
    query=GetFileContentRequest,
    resp=Response(HTTP_200=GetFileContentResponse)
)
def get_file_content(get_file_content: GetFileContentUseCase):
    repo_url = request.args.get("repo_url")
    file_path = request.args.get("file_path")
    result = get_file_content(repo_url, file_path)
    return serialize(result)
