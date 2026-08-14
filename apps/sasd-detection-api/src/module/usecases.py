"""
src/module/usecases.py
"""
from injector import Module, provider, singleton

from src.client.analysis import AnalysisClient
from src.client.collection import ArtefactCollectionClient
from src.strategy import MethodProcessorRegistry
from src.usecase import (
    AnalyseCommitsUseCase,
    AnalyseCommitsUseCaseImpl,
    AnalyseFileUseCase,
    AnalyseFileUseCaseImpl,
    AnalyseIssuesUseCase,
    AnalyseIssuesUseCaseImpl,
    AnalyseMethodUseCase,
    AnalyseMethodUseCaseImpl
)


class UsecaseModule(Module):
    """
    Wire together and provide usecase singletons
    """

    @provider
    @singleton
    def provide_analyse_commits(
        self,
        analysis: AnalysisClient,
        artefacts: ArtefactCollectionClient
    ) -> AnalyseCommitsUseCase:
        """
        Provide a wired-up usecase to analyse commit messages
        """
        return AnalyseCommitsUseCaseImpl(artefacts, analysis)

    @provider
    @singleton
    def provide_analyse_issues(
        self,
        analysis: AnalysisClient,
        artefacts: ArtefactCollectionClient
    ) -> AnalyseIssuesUseCase:
        """
        Provide a wired-up usecase to analyse issues
        """
        return AnalyseIssuesUseCaseImpl(artefacts, analysis)

    @provider
    @singleton
    def provide_analyse_file(
        self,
        analysis: AnalysisClient,
        artefacts: ArtefactCollectionClient
    ) -> AnalyseFileUseCase:
        """
        Provide a wired-up usecase to analyse file content
        """
        return AnalyseFileUseCaseImpl(artefacts, analysis)

    @provider
    @singleton
    def provide_analyse_method(
        self,
        analysis: AnalysisClient,
        processor_registry: MethodProcessorRegistry
    ) -> AnalyseMethodUseCase:
        """
        Provide a wired-up usecase to analyse a method's comments
        """
        return AnalyseMethodUseCaseImpl(analysis, processor_registry)
