"""
REST endpoints for VCS functionality.
"""
from flask import Blueprint, jsonify, request

from api.util.serializer import serialize_result
from domain.usecase.vcs.api import GetRepositoryStructureUseCase

vcs_bp = Blueprint(
    name="vcs_bp",
    import_name=__name__,
    url_prefix="/vcs"
)

@vcs_bp.get("/repo-structure")
def get_repository_structure(get_repository_structure: GetRepositoryStructureUseCase):
    repo_url = request.args.get("repoUrl")
    return serialize_result(get_repository_structure(repo_url))

@vcs_bp.get("/file-content")
def get_file_content():
    return jsonify({
        "error": "not implemented"
    })
