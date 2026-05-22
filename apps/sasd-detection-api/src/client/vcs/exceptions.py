"""
src/client/vcs/exceptions.py
"""


class VCSError(Exception): ...


class VCSUnavailable(VCSError): ...


class VCSRateLimited(VCSError): ...


class VCSNotFound(VCSError): ...


class VCSUnexpectedError(VCSError): ...
