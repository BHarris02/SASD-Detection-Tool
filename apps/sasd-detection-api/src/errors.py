"""
src/errors.py
"""
from flask import Flask, jsonify

# pylint: disable=wildcard-import
from src.exception import *


_ERROR_STATUS_CODES = {
    # analysis
    IncompleteAnalysisException: 502,
    NoArtefactsProvidedException: 422,
    UnknownArtefactIdException: 502,
    # artefacts
    NotAFileException: 422,
    NoCommentsFoundException: 404,
    NoCommitsFoundException: 404,
    NoFileContentException: 422,
    NoFileFoundException: 404,
    NoIssuesFoundException: 404,
    RepositoryNotFoundException: 404,
    UnsupportedLanguageException: 422,
    UnparsableMethodException: 400,
    NoMethodFoundException: 404,
    # config
    MissingEnvironmentVariablesException: 500,
}

# pylint: disable=missing-function-docstring
def register_error_handlers(app: Flask) -> None:
    for exception_type, status_code in _ERROR_STATUS_CODES.items():
        app.register_error_handler(exception_type, _handle(status_code))
    app.register_error_handler(Exception, _handle(500))


def _handle(status_code: int):
    def handler(e: Exception):
        # each domain exception's docstring doubles as its user-facing message
        message = (type(e).__doc__ or "An unexpected error occurred").strip()
        return jsonify({"error": message}), status_code
    return handler
