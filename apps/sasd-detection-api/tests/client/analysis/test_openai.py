"""
tests/client/analysis/test_openai.py
"""
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.client.analysis import CweSchema, OpenAiClient, SasdFindingBatchSchema, SasdFindingSchema
from src.exception import (
    IncompleteAnalysisException,
    NoArtefactsProvidedException,
    UnknownArtefactIdException
)
from src.model import Commit, Cwe, File, Issue, SasdFindingSeverity


# pylint: disable=missing-function-docstring
class OpenAiClientTest(TestCase):
    """
    Unit tests for `OpenAiClient`
    """

    def setUp(self):
        patcher = patch("src.client.analysis.openai.OpenAI")
        self.mock_openai = patcher.start()
        self.addCleanup(patcher.stop)

        self.mock_parse = self.mock_openai.return_value.beta.chat.completions.parse

        self.client = OpenAiClient(
            api_url="https://models.github.ai/inference",
            token="fake-token",
            model="openai/gpt-5"
        )

    # analyse_commits tests

    def test_analyse_commits_succeeds(self):
        commits = [
            Commit(a_id="a1", message="Fix security issues in API"),
            Commit(a_id="b2", message="Temporary fix for authentication bug"),
            Commit(a_id="c3", message="Update README")
        ]

        batch = SasdFindingBatchSchema(
            reviewed_count=3,
            findings=[
                SasdFindingSchema(
                    artefact_id="b2",
                    explanation="Commit message admits a temporary/incomplete authentication fix",
                    severity=SasdFindingSeverity.HIGH,
                    cwe=CweSchema(c_id="CWE-287", title="Improper Authentication")
                )
            ]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        findings = self.client.analyse_commits(commits)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].artefact, commits[1])
        self.assertEqual(findings[0].explanation, batch.findings[0].explanation)
        self.assertEqual(findings[0].severity, SasdFindingSeverity.HIGH)
        self.assertEqual(
            findings[0].cwe,
            Cwe(c_id="CWE-287", title="Improper Authentication")
        )

    def test_analyse_commits_no_findings(self):
        commits = [Commit(a_id="a1", message="Update README")]

        batch = SasdFindingBatchSchema(reviewed_count=1, findings=[])

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        self.assertEqual(self.client.analyse_commits(commits), [])

    def test_analyse_commits_incomplete_analysis(self):
        commits = [
            Commit(a_id="a1", message="Fix security issues in API"),
            Commit(a_id="c3", message="Update README")
        ]

        batch = SasdFindingBatchSchema(
            reviewed_count=1,
            findings=[]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        with self.assertRaises(IncompleteAnalysisException):
            self.client.analyse_commits(commits)

    # _analyse_artefact - indirectly tested
    # tested once since the underlying logic is shared

    def test_analyse_artefact_no_artefacts_provided(self):
        commits = []

        with self.assertRaises(NoArtefactsProvidedException):
            self.client.analyse_commits(commits)

    def test_analyse_artefact_unknown_artefact_id(self):
        commits = [
            Commit(a_id="a1", message="Some message")
        ]

        batch = SasdFindingBatchSchema(
            reviewed_count=1,
            findings=[
                SasdFindingSchema(
                    artefact_id="unknown-id-z26",
                    explanation="some explanation",
                    severity=SasdFindingSeverity.HIGH,
                    cwe=CweSchema(c_id="CWE-287", title="Improper Authentication")
                )
            ]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        with self.assertRaises(UnknownArtefactIdException):
            self.client.analyse_commits(commits)

    # analyse_issues tests

    # pylint: disable=line-too-long
    def test_analyse_issues_succeeds(self):
        issues = [
            Issue(a_id="1", title="Login bypass", body="Auth check disabled for now", is_pull_request=False),
            Issue(a_id="2", title="Update docs", body="Fix typos in README", is_pull_request=False),
            Issue(a_id="3", title="Add tests", body="Increase coverage", is_pull_request=True)
        ]

        batch = SasdFindingBatchSchema(
            reviewed_count=3,
            findings=[
                SasdFindingSchema(
                    artefact_id="1",
                    explanation="Issue body admits authentication check was disabled",
                    severity=SasdFindingSeverity.CRITICAL,
                    cwe=CweSchema(c_id="CWE-287", title="Improper Authentication")
                )
            ]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        findings = self.client.analyse_issues(issues)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].artefact, issues[0])
        self.assertEqual(findings[0].explanation, batch.findings[0].explanation)
        self.assertEqual(findings[0].severity, SasdFindingSeverity.CRITICAL)
        self.assertEqual(
            findings[0].cwe,
            Cwe(c_id="CWE-287", title="Improper Authentication")
        )

    def test_analyse_issues_no_findings(self):
        issues = [Issue(a_id="a1", title="Update README", body="", is_pull_request=False)]

        batch = SasdFindingBatchSchema(reviewed_count=1, findings=[])

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        self.assertEqual(self.client.analyse_issues(issues), [])

    # pylint: disable=line-too-long
    def test_analyse_issues_incomplete_analysis(self):
        issues = [
            Issue(a_id="1", title="Login bypass", body="Auth check disabled for now", is_pull_request=False),
            Issue(a_id="2", title="Update docs", body="Fix typos in README", is_pull_request=False)
        ]

        batch = SasdFindingBatchSchema(
            reviewed_count=1,
            findings=[]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        with self.assertRaises(IncompleteAnalysisException):
            self.client.analyse_issues(issues)

    # analyse_file_content tests

    def test_analyse_file_content_succeeds(self):
        file = File(a_id="abc123", content="ssl_verify = False  # temporary, revisit later")

        batch = SasdFindingBatchSchema(
            reviewed_count=1,
            findings=[
                SasdFindingSchema(
                    artefact_id="abc123",
                    explanation="Content admits SSL verification is disabled temporarily",
                    severity=SasdFindingSeverity.HIGH,
                    cwe=CweSchema(c_id="CWE-295", title="Improper Certificate Validation")
                )
            ]
        )

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        finding = self.client.analyse_file_content(file)

        self.assertIsNotNone(finding)
        self.assertEqual(finding.artefact, file)
        self.assertEqual(finding.explanation, batch.findings[0].explanation)
        self.assertEqual(finding.severity, SasdFindingSeverity.HIGH)
        self.assertEqual(
            finding.cwe,
            Cwe(c_id="CWE-295", title="Improper Certificate Validation")
        )

    def test_analyse_file_content_no_findings(self):
        file = File(a_id="abc123", content="print('Hello, World!')")

        batch = SasdFindingBatchSchema(reviewed_count=1, findings=[])

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        finding = self.client.analyse_file_content(file)

        self.assertIsNone(finding)

    def test_analyse_file_content_incomplete_analysis(self):
        file = File(a_id="abc123", content="print('Hello, World!')")

        batch = SasdFindingBatchSchema(reviewed_count=0, findings=[])

        mock_completion = MagicMock()
        mock_completion.choices[0].message.parsed = batch
        self.mock_parse.return_value = mock_completion

        with self.assertRaises(IncompleteAnalysisException):
            self.client.analyse_file_content(file)
