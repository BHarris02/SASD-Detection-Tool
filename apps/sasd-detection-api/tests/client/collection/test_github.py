"""
tests/client/collection/test_github.py
"""
from base64 import b64encode
from unittest import TestCase
from unittest.mock import MagicMock, patch

from requests import HTTPError

from src.client.collection import GitHubClient
from src.exception import (
    NoCommitsFoundException,
    NoFileContentException,
    NoFileFoundException,
    NotAFileException,
    NoIssuesFoundException,
    RepositoryNotFoundException
)


# pylint: disable=missing-function-docstring
class GitHubClientTest(TestCase):
    """
    Unit tests for `GitHubClient`
    """

    def setUp(self):
        patcher = patch("src.client.collection.github.get")
        self.mock_get = patcher.start()
        self.addCleanup(patcher.stop)

        self.client = GitHubClient(api_url="https://api.github.com", token="fake-token")

    # fetch_commits tests

    def test_fetch_commits_succeeds(self):
        fake_commits = [
            {"sha": "abc123", "commit": {"message": "test commit message"}},
            {"sha": "def456", "commit": {"message": "test commit message 2"}}
        ]

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_commits

        self.mock_get.return_value = mock_resp

        commits = self.client.fetch_commits("BHarris02", "SASD-Detection-Tool")

        self.assertEqual(len(commits), 2)
        self.assertEqual(commits[0].a_id, "abc123")
        self.assertEqual(commits[0].message, "test commit message")

    def test_fetch_commits_repository_not_found(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 404

        self.mock_get.return_value = mock_resp

        with self.assertRaises(RepositoryNotFoundException):
            self.client.fetch_commits("BHarris02", "SASD-Detection-Tool")

    def test_fetch_commits_no_commits_found(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 409

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NoCommitsFoundException):
            self.client.fetch_commits("BHarris02", "SASD-Detection-Tool")

    def test_fetch_commits_propagates_http_error(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.raise_for_status.side_effect = HTTPError()

        self.mock_get.return_value = mock_resp

        with self.assertRaises(HTTPError):
            self.client.fetch_commits("BHarris02", "SASD-Detection-Tool")

    # fetch_issues tests

    def test_fetch_issues_succeeds(self):
        fake_issues = [
            {"number": 1, "title": "Issue Title 1", "body": "This is Issue #1"},
            {"number": 2, "title": "Issue Title 2", "body": "This is Issue #2", "pull_request": {}}
        ]

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_issues

        self.mock_get.return_value = mock_resp

        issues = self.client.fetch_issues("BHarris02", "SASD-Detection-Tool")

        self.assertEqual(len(issues), 2)
        self.assertEqual(issues[0].a_id, "1")
        self.assertEqual(issues[0].title, "Issue Title 1")
        self.assertEqual(issues[0].body, "This is Issue #1")
        self.assertEqual(issues[0].is_pull_request, False)

        self.assertEqual(issues[1].is_pull_request, True)

    def test_fetch_issues_repository_not_found(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 404

        self.mock_get.return_value = mock_resp

        with self.assertRaises(RepositoryNotFoundException):
            self.client.fetch_issues("BHarris02", "SASD-Detection-Tool")

    def test_fetch_issues_no_issues_found(self):
        fake_issues = []

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_issues

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NoIssuesFoundException):
            self.client.fetch_issues("BHarris02", "SASD-Detection-Tool")

    def test_fetch_issues_with_only_pull_requests(self):
        fake_issues = [
            {"number": 1, "title": "Issue Title 1", "body": "This is Issue #1", "pull_request": {}},
            {"number": 2, "title": "Issue Title 2", "body": "This is Issue #2", "pull_request": {}}
        ]

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_issues

        self.mock_get.return_value = mock_resp

        issues = self.client.fetch_issues("BHarris02", "SASD-Detection-Tool")

        self.assertEqual(len(issues), 2)
        self.assertEqual(issues[0].a_id, "1")
        self.assertEqual(issues[0].title, "Issue Title 1")
        self.assertEqual(issues[0].body, "This is Issue #1")

        self.assertEqual(issues[0].is_pull_request, True)
        self.assertEqual(issues[1].is_pull_request, True)

    def test_fetch_issues_propagates_http_error(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.raise_for_status.side_effect = HTTPError()

        self.mock_get.return_value = mock_resp

        with self.assertRaises(HTTPError):
            self.client.fetch_issues("BHarris02", "SASD-Detection-Tool")

    # fetch_file tests

    def test_fetch_file_succeeds(self):
        raw_content = "print('Hello, World!')"
        encoded_content = b64encode(raw_content.encode("utf-8")).decode("utf-8")
        fake_content = {"sha": "abc123", "content": encoded_content}

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_content

        self.mock_get.return_value = mock_resp

        file = self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "hello.py")

        self.assertEqual(file.a_id, "abc123")
        self.assertEqual(file.content, raw_content)

    def test_fetch_file_no_file_found(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 404

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NoFileFoundException):
            self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "main.py")

    def test_fetch_file_no_file_content(self):
        fake_content = {"content": ""}

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_content

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NoFileContentException):
            self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "main.py")

    def test_fetch_file_directory_not_a_file(self):
        fake_content = [{"name": "hello.py", "type": "file"}]

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_content

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NotAFileException):
            self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "main.py")

    def test_fetch_file_symlink_not_a_file(self):
        fake_content = {"name": "link", "type": "symlink", "target": "somewhere.py"}

        mock_resp = MagicMock()
        mock_resp.status_code = 200
        mock_resp.json.return_value = fake_content

        self.mock_get.return_value = mock_resp

        with self.assertRaises(NotAFileException):
            self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "main.py")

    def test_fetch_file_propagates_http_error(self):
        mock_resp = MagicMock()
        mock_resp.status_code = 500
        mock_resp.raise_for_status.side_effect = HTTPError()

        self.mock_get.return_value = mock_resp

        with self.assertRaises(HTTPError):
            self.client.fetch_file("BHarris02", "SASD-Detection-Tool", "main.py")
