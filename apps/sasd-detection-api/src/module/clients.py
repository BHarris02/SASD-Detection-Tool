"""
src/module/clients.py
"""
from os import environ

from injector import Module, provider, singleton

from src.client.analysis import AnalysisClient, AnthropicClient, OpenAiClient
from src.client.collection import ArtefactCollectionClient, GitHubClient
from src.exception import MissingEnvironmentVariablesException


class ClientsModule(Module):
    """
    Wires together and provides external client singletons
    """

    @provider
    @singleton
    def provide_analysis_client(self) -> AnalysisClient:
        """
        Provide a concrete, configured client to analyse artefacts
        """
        model_provider = environ["ANALYSIS_PROVIDER"]
        api_url = environ["ANALYSIS_MODEL_URL"]
        token = environ["ANALYSIS_MODEL_TOKEN"]
        model = environ["ANALYSIS_MODEL"]

        if not all([model_provider, api_url, token, model]):
            raise MissingEnvironmentVariablesException()

        match model_provider.lower():
            case "openai": return OpenAiClient(
                api_url=api_url,
                token=token,
                model=model
            )
            case "anthropic": return AnthropicClient(
                api_key=token,
                model=model
            )

    @provider
    @singleton
    def provide_artefact_collection_client(self) -> ArtefactCollectionClient:
        """
        Provide a concrete, confirured client to collect artefacts
        """
        return GitHubClient(
            api_url=environ["GITHUB_API_URL"],
            token=environ["GITHUB_API_TOKEN"],
        )
