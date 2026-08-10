"""
src/client/analysis/api.py
"""
from abc import ABC, abstractmethod

from src.model import Commit, File, Issue, SasdFinding


class AnalysisClient(ABC):
    """
    Abstract base class implemented by concrete analysis client providers
    """

    @abstractmethod
    def analyse_commits(self, commits: list[Commit]) -> list[SasdFinding]:
        """
        Provide repository commits messages to model for analysis
        
        :param commits: A list of `Commit` artefacts for analysis
        
        :return list[SasdFinding]: A list of `SasdFinding` for commits positively containing SASD
        """

    @abstractmethod
    def analyse_issues(self, issues: list[Issue]) -> list[SasdFinding]:
        """
        Provide repository issues to model for analysis
        
        :param issues: A list of `Issue` artefacts for analysis
        
        :return list[SasdFinding]: A list of `SasdFinding` for issues positively containing SASD
        """

    @abstractmethod
    def analyse_file_content(self, file: File) -> SasdFinding:
        """
        Provide a single file to the model for analysis

        :param file: A `File` entity with content

        :return SasdFinding: The analysis findings for the file contents
        """
