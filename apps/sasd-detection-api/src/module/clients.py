"""
src/module/clients.py
"""

from os import environ

from injector import Module, provider, singleton

from src.client.vcs.base import VCSClient
from src.client.vcs.config import VCSConfig
from src.client.vcs.github import GitHubClient


class ClientsModule(Module):
    """
    Wires together and provides HTTP client singletons
    """

    @provider
    @singleton
    def provide_vcs_config(self) -> VCSConfig:
        """
        Provide VCS configuration variables from environment
        """
        return VCSConfig(
            token=environ["GITHUB_TOKEN"],
            base_url=environ.get("GITHUB_BASE_URL", "https://api.github.com"),
            user_agent=environ.get("GITHUB_USER_AGENT", "sasd-detection-api/0.1"),
            timeout=int(environ.get("GITHUB_TIMEOUT", "10")),
            api_version=environ.get("GITHUB_API_VERSION", "2022-11-28"),
        )

    @provider
    @singleton
    def provide_vcs_client(self, config: VCSConfig) -> VCSClient:
        """
        Provide a configured, concrete VCS Client
        """
        return GitHubClient(config)
