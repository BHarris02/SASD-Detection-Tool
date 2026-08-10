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
