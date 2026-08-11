"""
src/module/clients.py
"""
from os import environ

from injector import Module, provider, singleton

from src.client.analysis import AnalysisClient, OpenAiClient
from src.client.collection import ArtefactCollectionClient, GitHubClient


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
        return OpenAiClient(
            api_url=environ["GITHUB_MODELS_URL"],
            token=environ["GITHUB_MODELS_TOKEN"],
            model=environ["ANALYSIS_MODEL"]
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
