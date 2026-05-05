"""
Module wiring together Infrastructure dependencies
"""
from os import getenv

from injector import Module, provider, singleton

from src.application.gateway.analysis_gateway import AnalysisGateway
from src.application.gateway.vcs_gateway import VcsGateway
from src.infrastructure.client.vcs.github.client import GitHubClient
from src.infrastructure.gateway.vcs.github import GitHubVcsGateway

class InfrastructureModule(Module):
    """
    Wires together `infrastructure` dependencies
    """
    @provider
    @singleton
    def provide_vcs_gateway(self) -> VcsGateway:
        """
        Wire up VcsGateway
        """
        api_token = getenv("GITHUB_TOKEN")
        base_url = getenv("GITHUB_API_URL")
        timeout = getenv("GITHUB_API_TIMEOUT")
        user_agent = getenv("GITHUB_USER_AGENT")

        if not all([api_token, base_url, timeout, user_agent]):
            raise ValueError("Missing required API configuration variables")

        client = GitHubClient(api_token, base_url, timeout, user_agent)
        return GitHubVcsGateway(client=client)

    @provider
    @singleton
    def provide_analysis_gateway(self) -> AnalysisGateway:
        """
        Wire up AnalysisGateway
        """
        raise NotImplementedError()
