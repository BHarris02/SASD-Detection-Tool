"""
src/client/vcs/config.py
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class VCSConfig:
    """
    Config variables for VCS clients
    """

    token: str
    base_url: str
    user_agent: str
    timeout: int
    api_version: str
