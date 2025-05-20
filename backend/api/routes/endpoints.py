"""
Module Name: endpoints.py
Description: Provides API endpoints for the SASD Detection API. Defines a Flask bluepint
            and registers routes for analysing commit messages, issue messages, single 
            method comments, full files, and full repository data. It also includes endpoints
            for retrieving repository structure and file content.
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - requests
    - flask
    - flask_pydantic_spec
    - pydantic
    - api.utils.data_collection
    - api.utils.nlp
    - api.utils.data_preprocessing
    - api.utils.schemas
    - api.utils.config
Usage:
    This module is part of a larger Flask application. To use these endpoints in the app, 
    import and api blueprint  and FlaskPydanticSpec into the main application module and
    register the blueprint with the Flask app.
"""

import requests
from flask import Blueprint, request, jsonify, render_template
from flask_pydantic_spec import FlaskPydanticSpec, Request, Response
from api.utils.data_collection import (fetch_commit_messages, fetch_issue_messages, fetch_raw_files, fetch_raw_code)
from api.utils.nlp import (analyze_messages, analyze_method, map_to_cwe)
from api.utils.data_preprocessing import process_code
from pydantic import ValidationError
from api.utils.schemas import *
from api.utils.config import GITHUB_API_TOKEN
from api.utils.schemas import *

api_bp = Blueprint("api", __name__)
api = FlaskPydanticSpec("flask", title="SASD Detection API", version="1.0.0", path="/apidocs")

@api_bp.route("/docs")
def swagger_ui():
    return render_template("swagger_ui.html")

@api_bp.route("/analyze/commits", methods=["POST"])
@api.validate(body=Request(AnalyzeCommitsRequest), resp=Response(HTTP_200 = CommitAnalysisResponse), tags=["api"])
def analyze_commits() -> None:
    try:
        data = AnalyzeCommitsRequest(**request.json)
        repo = data.repo

        commit_messages = fetch_commit_messages(repo)
        nlp_analysis = analyze_messages(commit_messages)
        
        return jsonify({
            "commit_analysis": nlp_analysis
        }), 200
    
    except ValidationError as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_commits) Validation Error: {e.errors()}"
        }), 400
    except Exception as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_commits) An Error occurred: {str(e)}"
        }), 500

@api_bp.route("/analyze/issues", methods=["POST"])
@api.validate(body=Request(AnalyzeIssuesRequest), resp=Response(HTTP_200 = IssueAnalysisResponse), tags=["api"])
def analyze_issues() -> None:
    try:
        data = AnalyzeIssuesRequest(**request.json)
        repo = data.repo

        issues = fetch_issue_messages(repo)
        nlp_analysis = analyze_messages(issues)

        return jsonify({
            "issue_analysis": nlp_analysis
        }), 200
    
    except ValidationError as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_issues) Validation Error: {e.errors()}"
        }), 400     
    except Exception as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_issues) An Error occurred: {str(e)}"
        }), 500

@api_bp.route("/analyze/method", methods=["POST"])
@api.validate(body=Request(AnalyzeMethodRequest), resp=Response(HTTP_200 = MethodAnalysisResponse), tags=["api"])
def analyze_single_method() -> None:
    try:
        data = AnalyzeMethodRequest(**request.json)
        method_body = data.method_body

        nlp_analysis = analyze_method(method_body)

        if nlp_analysis["sasd_detected"]:
            cwe_mapping = map_to_cwe(nlp_analysis.get("details", ""))

            resp = MethodAnalysisResponse(
                sasd_detected=nlp_analysis.get("sasd_detected"),
                details=CWEAnalysisResponse(
                    cwe_mapping=cwe_mapping.get("cwe_mapping"),
                    details=cwe_mapping.get("details")
                )
            )
        else:
            resp = MethodAnalysisResponse(
                sasd_detected=nlp_analysis.get("sasd_detected"),
                details=CWEAnalysisResponse(
                    cwe_mapping="N/a",
                    details="N/a"
                )
            )


        return jsonify(
            resp.dict()
        ), 200
    
    except ValidationError as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_single_method) Validation Error: {e.errors()}"
        }), 400     
    except Exception as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_source_code) An Error occurred: {str(e)}"
        }), 500

@api_bp.route("/analyze/file", methods=["POST"])
@api.validate(body=Request(AnalyzeCodeFileRequest), resp=Response(HTTP_200 = CodeFileAnalysisResponse), tags=["api"])
def analyze_code_file() -> None:
    try:
        data = AnalyzeCodeFileRequest(**request.json)
        repo = data.repo
        path = data.path
    
        raw_code = fetch_raw_code(repo, path)
        methods = process_code(raw_code)

        code_analysis = []
        for method in methods:
            sasd_analysis = analyze_method(method["method_body"])
            cwe_mapping = map_to_cwe(sasd_analysis.get("details", ""))

            method_response = {
                "sasd_detected": sasd_analysis.get("sasd_detected"),
                "method_signature": method["method_signature"],
                "details": {
                    "cwe_mapping": cwe_mapping.get("cwe_mapping"),
                    "details": cwe_mapping.get("details")
                },
                "cwe_mapping": cwe_mapping
            }

            #sasd_analysis["cwe_mapping"] = cwe_mapping
            code_analysis.append(method_response)

        resp = CodeFileAnalysisResponse(code_analysis=code_analysis)
        
        return jsonify(
            resp.dict()
        ), 200
    
    except ValidationError as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_code_file) Validation Error: {e.errors()}"
        }), 400     
    except Exception as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_code_file) An Error occurred: {str(e)}"
        }), 500

@api_bp.route("/analyze/repo", methods=["POST"])
@api.validate(body=Request(AnalyzeRepoRequest), resp=Response(HTTP_200 = AnalyzeRepoResponse), tags=["api"])
def analyze_full_repo():
    try:
        data = request.json
        repo = data.get("repo")

        if not repo:
            return jsonify({
                "error": "Repository URL required"
            }), 400
        
        commit_analysis = analyze_messages(fetch_commit_messages(repo))
        issue_analysis = analyze_messages(fetch_issue_messages(repo))

        raw_files = fetch_raw_files(repo, "")
        relevant_file_exts = {".py", ".java", ".cpp"}
        code_analysis = []

        for file_path, file_content in raw_files:
            if any(file_path.endswith(ext) for ext in relevant_file_exts):
                methods = process_code(file_content)

                for method in methods:
                    sasd_analysis = analyze_method(method["method_body"])
                    cwe_mapping = map_to_cwe(sasd_analysis.get("details", ""))

                    sasd_analysis["cwe_mapping"] = cwe_mapping
                    code_analysis.append({
                        "file_path": file_path,
                        "method_signature": method.get("method_signature"),
                        **sasd_analysis
                    })
        
        return jsonify({
            "commit_analysis": commit_analysis,
            "issue_analysis": issue_analysis,
            "code_analysis": code_analysis
        }), 200
    
    except ValidationError as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_full_repo) Validation Error: {e.errors()}"
        }), 400
    except Exception as e:
        return jsonify({
            "error": f"[endpoints.py] (analyze_full_repo) An Error occurred: {str(e)}"
        }), 500
    
@api_bp.route("/repo/structure", methods=["GET"])
@api.validate(resp=Response(HTTP_200 = RepositoryStructureResponse), tags=["api"])
def get_repo_structure():
    repo_url = request.args.get("repo_url")

    if not repo_url:
        return jsonify({
            "error": "Repository URL ('Owner/Repo') required"
        }), 400
    
    try:
        owner, repo = repo_url.split("/")[:2]

        github_api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
        headers = {"Authorization": f"token {GITHUB_API_TOKEN}"}
        resp = requests.get(github_api_url, headers=headers)

        if resp.status_code != 200:
            return jsonify({
                "error": f"Failed to get Repository Structure: {resp.text}"
            })
        
        contents = resp.json()

        def parse_structure(contents) -> list:
            struct = []
            for item in contents:
                if item["type"] == "dir":
                    dir_resp = requests.get(item["url"], headers=headers)
                    dir_contents = dir_resp.json()

                    struct.append({
                        "name": item["name"],
                        "type": "folder",
                        "children": parse_structure(dir_contents)
                    })
                else:
                    struct.append({
                        "name": item["name"],
                        "type": "file",
                        "path": item["path"]
                    })
            return struct
        
        struct = parse_structure(contents)
        return jsonify({
            "structure": struct
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": f"Failed to retrieve Structure: {str(e)}"
        }), 500
    
@api_bp.route("/file/content", methods=["POST"])
@api.validate(body=Request(FileContentRequest), resp=Response(HTTP_200 = FileContentResponse), tags=["api"])
def get_file_content():
    try:
        data = request.json
        repo = data.get("repo")
        file_path = data.get("file_path")

        if not repo or not file_path:
            return jsonify({
                "error": "Both Repository and File Path are required"
            }), 400
        
        file_content = fetch_raw_code(repo, file_path)

        return jsonify({
            "file_content": file_content
        }), 200
    
    except Exception as e:
        return jsonify({
            "error": f"Failed to fetch file content {str(e)}"
        }), 500