"""
src/exception/artefacts.py
"""

class NoCommitsFoundException(Exception):
    """
    Thrown when no commits are found in a repository
    """


class NoIssuesFoundException(Exception):
    """
    Thrown when no issues or pulls are found in a repository
    """


class NoFileFoundException(Exception):
    """
    Thrown when no file is found at the provided repository path
    """


class NoFileContentException(Exception):
    """
    Thrown when a file is empty
    """


class NotAFileException(Exception):
    """
    Thrown when a non-file path is provided, e.g. path to a directory
    """


class RepositoryNotFoundException(Exception):
    """
    Thrown when a repository cannot be found
    """


class UnsupportedLanguageException(Exception):
    """
    Thrown when an unsupported language processor is requested
    """


class UnparsableMethodException(Exception):
    """
    Thrown when a method is unparsable due to invalid syntax
    """


class NoMethodFoundException(Exception):
    """
    Thrown when parsed source code has no method signature present
    """


class NoCommentsFoundException(Exception):
    """
    Thrown when a parsed method has neither a docstring nor comments
    """
