"""
Wires together `data` layer dependencies and exposes them via `@provider' decorated methods.
"""
from os import getenv

from injector import Module, provider, singleton

from data.client.nlp.nlp_api_service import NLPApiService
from data.client.nlp.anthropic.claude_api_service import ClaudeApiService
from data.client.nlp.google.gemini_api_service import GeminiApiService
from data.client.vcs.vcs_api_service import VCSApiService
from data.client.vcs.github.github_api_service import GitHubApiService
from data.gateway.nlp_gateway_impl import NLPGatewayImpl
from data.repository.vcs_repository_impl import GitHubVCSRepository
from domain.gateway.nlp_gateway_api import NLPGateway
from domain.repository.vcs_repository_api import VCSRepository

class DataModule(Module):
    """
    Wires together `data` layer dependencies and exposes them via `@provider' decorated methods.
    """

    @provider
    @singleton
    def provide_nlp_api_service(self) -> NLPApiService:
        provider = getenv("NLP_PROVIDER", "google")

        if provider == "anthropic":
            api_token = getenv("ANTHROPIC_API_TOKEN")
            base_url = getenv("ANTHROPIC_BASE_URL")
            model = getenv("ANTHROPIC_MODEL")

            if not all([api_token, base_url, model]):
                raise ValueError("Missing required Anthropic API configuration variables.")
            
            assert api_token and base_url and model

            return ClaudeApiService(
                api_token=api_token,
                base_url=base_url,
                model=model
            )

        elif provider == "google":
            api_token=getenv("GOOGLE_API_TOKEN")
            model=getenv("GOOGLE_MODEL")

            if not all([api_token, model]):
                raise ValueError("Missing required Google API configuration variables.")
            
            assert api_token and model

            return GeminiApiService(
                api_token=api_token,
                model=model
            )

        raise ValueError(f"Unknown NLP provider: {provider}")

    @provider
    @singleton
    def provide_nlp_gateway(self, api_service: NLPApiService) -> NLPGateway:
        return NLPGatewayImpl(api_service=api_service)

    @provider
    @singleton
    def provide_vcs_api_service(self) -> VCSApiService:
        """
        """
        api_token=getenv("GITHUB_API_TOKEN")
        base_url=getenv("GITHUB_BASE_URL")
        timeout=getenv("GITHUB_API_TIMEOUT")

        if not all([api_token, base_url, timeout]):
            raise ValueError("Missing required GitHub API configuration variables.")

        assert api_token and base_url and timeout

        return GitHubApiService(
            api_token=api_token,
            base_url=base_url,
            timeout=int(timeout)
        )

    @provider
    @singleton
    def provide_vcs_repository(self, api_service: VCSApiService) -> VCSRepository:
        """
        """
        return GitHubVCSRepository(api_service=api_service)
