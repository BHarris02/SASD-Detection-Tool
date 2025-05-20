"""
Module Name: test_data_collection.py
Description: This module contains unit test cases for functions in the data_collection module.
            The tests verify the correctness of:
                - fetch_commit_messages: ensuring commit messages are correctly extracted
                - fetch_issue_messages: ensuring issue tracker entries are correctly extracted
                - fetch_raw_code: ensuring raw code is correctly extracted and decoded
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - unittest
    - unittest.mock
    - api.utils.data_collection
    - base64
Usage:
    Run the test suite from the command line:
        python -m unittest tests.test_data_collection
"""
import unittest
from unittest.mock import MagicMock, patch
from api.utils.data_collection import fetch_commit_messages, fetch_issue_messages, fetch_raw_code
import base64

class TestDataCollection(unittest.TestCase):

    @patch("api.utils.data_collection.requests.get")
    def test_fetch_commit_messages(self, mock_get):
        fake_commits = [{
            "commit": {"message": "Commit 1 message"}
        },
        {
            "commit": {"message": "Commit 2 message"}
        }]
        mock_resp = MagicMock()
        mock_resp.json.return_value = fake_commits
        mock_get.return_value = mock_resp

        repo = "owner/repo"
        messages = fetch_commit_messages(repo)
        self.assertIsInstance(messages, list)
        self.assertEqual(messages, ["Commit 1 message", "Commit 2 message"])

    @patch("api.utils.data_collection.requests.get")
    def test_fetch_issue_messages(self, mock_get):
        fake_issues = [{
            "title": "Issue 1", 
            "body": "Body 1"
        },
        {
            "title": "Issue 2", 
            "body": "Body 2"
        }]
        mock_resp = MagicMock()
        mock_resp.json.return_value = fake_issues
        mock_get.return_value = mock_resp

        repo = "owner/repo"
        issues = fetch_issue_messages(repo)
        expected = ["Issue 1: Body 1", "Issue 2: Body 2"]
        self.assertEqual(issues, expected)

    @patch("api.utils.data_collection.requests.get")
    def test_fetch_raw_code(self, mock_get):
        original_content = "print('Hello World')"
        encoded_content = base64.b64encode(original_content.encode('utf-8')).decode('utf-8')
        fake_response = {
            "content": encoded_content
        }
        mock_resp = MagicMock()
        mock_resp.json.return_value = fake_response
        mock_get.return_value = mock_resp
        repo = "owner/repo"
        file_path = "dummy/path.py"
        code = fetch_raw_code(repo, file_path)
        self.assertEqual(code, original_content)

    @patch("api.utils.data_collection.fetch_raw_code")
    @patch("api.utils.data_collection.requests.get")
    def test_fetch_raw_files(self, mock_get, mock_fetch_raw_code):
        root_response = [
            {"type": "file", 
             "path": "file1.py"},
            {"type": "dir", 
             "path": "subdir"}
        ]
        subdir_response = [{
            "type": "file", 
            "path": "subdir/file2.py"
        }]

        mock_get.side_effect = [
            MagicMock(json=MagicMock(return_value=root_response)),
            MagicMock(json=MagicMock(return_value=subdir_response))
        ]

        def mock_code(repo, path):
            return f"content of {path}"
        mock_fetch_raw_code.side_effect = mock_code

        from api.utils.data_collection import fetch_raw_files
        repo = "owner/repo"
        path = ""
        result = fetch_raw_files(repo, path)

        expected = [
            ("file1.py", "content of file1.py"),
            ("subdir/file2.py", "content of subdir/file2.py")
        ]

        self.assertIsInstance(result, list)
        self.assertEqual(result, expected)
        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(mock_fetch_raw_code.call_count, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)