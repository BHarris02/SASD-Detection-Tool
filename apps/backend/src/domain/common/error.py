"""
Domain-specific errors.
"""

class DomainError(Exception):
    """
    Base error class for domain-specific errors to subclass.
    """

class VCSError(DomainError):
    """
    VCS-domain specific errors.
    """

class AnalysisError(DomainError):
    """
    Analysis-domain specific errors.
    """
