"""
Module Name: test_endpoints_integration.py
Description: This module contains integration test cases for functions in the endpoints module.
            It tests all routes provided by the SASD Detection API. Tests use Flask's test client 
            and mock external dependencies to ensure the endpoints behave as expected.
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - unittest
    - unittest.mock
    - Flask
    - api.routes.endpoints
Usage:
    Run the test suite from the command line:
        python -m unittest tests.test_endpoints_integration
"""
import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from api.routes.endpoints import api_bp

class TestEndpointsIntegration(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.register_blueprint(api_bp)
        self.client = self.app.test_client()

    @patch("api.routes.endpoints.fetch_commit_messages")
    @patch("api.routes.endpoints.analyze_messages")
    def test_analyze_commits(self, mock_analyze_messages, mock_fetch_commit_messages):
        mock_fetch_commit_messages.return_value = ["Commit message 1", "Commit message 2"]
        mock_analyze_messages.return_value = [{
            "message": "Commit message 1",
            "sasd_detected": True,
            "details": "Detail 1"
        },
        {
            "message": "Commit message 2",
            "sasd_detected": False,
            "details": "Detail 2"
        }]
        payload = {
            "repo": "owner/repo"
        }
        response = self.client.post('/analyze/commits', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("commit_analysis", data)
        self.assertEqual(len(data["commit_analysis"]), 2)

    def test_analyze_commits_validation_error(self):
        resp = self.client.post('/analyze/commits', json={})
        self.assertEqual(resp.status_code, 422)
        data = resp.get_json()
        self.assertIsInstance(data, list)
        self.assertIn("msg", data[0])
        self.assertEqual(data[0]["msg"], "field required")

    @patch("api.routes.endpoints.fetch_commit_messages", side_effect=Exception("Unexpected error"))
    def test_analyze_commits_exception(self, _):
        payload = {
            "repo": "owner/repo"
        }
        resp = self.client.post('/analyze/commits', json=payload)
        self.assertEqual(resp.status_code, 500)
        data = resp.get_json()
        self.assertIn("error", data)

    @patch("api.routes.endpoints.fetch_issue_messages")
    @patch("api.routes.endpoints.analyze_messages")
    def test_analyze_issues(self, mock_analyze_messages, mock_fetch_issue_messages):
        mock_fetch_issue_messages.return_value = ["Issue 1", "Issue 2"]
        mock_analyze_messages.return_value = [{
            "message": "Issue 1",
            "sasd_detected": True,
            "details": "Detail 1"
        },
        {
            "message": "Issue 2",
            "sasd_detected": False,
            "details": "Detail 2"
        }]
        payload = {
            "repo": "owner/repo"
        }
        response = self.client.post('/analyze/issues', json={"repo": "owner/repo"})
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("issue_analysis", data)
        self.assertEqual(len(data["issue_analysis"]), 2)

    def test_analyze_issues_validation_error(self):
        resp = self.client.post('/analyze/issues', json={})
        self.assertEqual(resp.status_code, 422)

    @patch("api.routes.endpoints.fetch_issue_messages", side_effect=Exception("Mock failure"))
    def test_analyze_issues_exception(self, _):
        resp = self.client.post('/analyze/issues', json={ "repo": "owner/repo" })
        self.assertEqual(resp.status_code, 500)

    @patch("api.routes.endpoints.map_to_cwe")
    @patch("api.routes.endpoints.analyze_method")
    def test_analyze_method(self, mock_analyze_method, mock_map_to_cwe):
        mock_analyze_method.return_value = {
            "sasd_detected": True, 
            "details": "Method analysis detail"
        }
        mock_map_to_cwe.return_value = {
            "cwe_mapping": "CWE-999: Dummy", 
            "details": "Successful CWE mapping"
        }
        payload = {
            "method_body": "public void test() { // TODO: improve security }"
        }
        response = self.client.post('/analyze/method', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertTrue(data["sasd_detected"])
        self.assertEqual(data["details"]["cwe_mapping"], "CWE-999: Dummy")
    
    def test_analyze_method_validation_error(self):
        resp = self.client.post('/analyze/method', json={})
        self.assertEqual(resp.status_code, 422)

    @patch("api.routes.endpoints.analyze_method", side_effect=Exception("NLP crash"))
    def test_analyze_method_exception(self, _):
        payload = {
            "method_body": "void function() {}"
        }
        resp = self.client.post('/analyze/method', json=payload)
        self.assertEqual(resp.status_code, 500)

    @patch("api.routes.endpoints.map_to_cwe")
    @patch("api.routes.endpoints.analyze_method")
    @patch("api.routes.endpoints.process_code")
    @patch("api.routes.endpoints.fetch_raw_code")
    def test_analyze_file(self, mock_fetch_raw_code, mock_process_code, mock_analyze_method, mock_map_to_cwe):
        mock_fetch_raw_code.return_value = "public void test() { // secure }"
        mock_process_code.return_value = [{
            "method_signature": "public void test()",
            "method_body": "public void test() { // secure }"
        }]
        mock_analyze_method.return_value = {
            "sasd_detected": False, 
            "details": "No SASD"
        }
        mock_map_to_cwe.return_value = {
            "cwe_mapping": None, 
            "details": "N/a"
        }
        payload = {
            "repo": "owner/repo", 
            "path": "src/test.java"
        }
        response = self.client.post('/analyze/file', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("code_analysis", data)
        self.assertIsInstance(data["code_analysis"], list)
        self.assertEqual(len(data["code_analysis"]), 1)

    def test_analyze_file_validation_error(self):
        resp = self.client.post('/analyze/file', json={})
        self.assertEqual(resp.status_code, 422)

    @patch("api.routes.endpoints.fetch_raw_code", side_effect=Exception("Mock failure"))
    def test_analyze_file_exception(self, _):
        payload = {
            "repo": "owner/repo", 
            "path": "some/file.java"
        }
        resp = self.client.post('/analyze/file', json=payload)
        self.assertEqual(resp.status_code, 500)

    @patch("api.routes.endpoints.fetch_commit_messages")
    @patch("api.routes.endpoints.analyze_messages")
    @patch("api.routes.endpoints.fetch_issue_messages")
    @patch("api.routes.endpoints.fetch_raw_files")
    @patch("api.routes.endpoints.process_code")
    @patch("api.routes.endpoints.analyze_method")
    @patch("api.routes.endpoints.map_to_cwe")
    def test_analyze_repo(self, mock_map_to_cwe, mock_analyze_method, mock_process_code, mock_fetch_raw_files, 
                          mock_fetch_issue_messages, mock_analyze_messages, mock_fetch_commit_messages):
        mock_fetch_commit_messages.return_value = ["Commit message 1"]
        mock_analyze_messages.side_effect = lambda msgs: [{
            "message": m, 
            "sasd_detected": False, 
            "details": "Detail"
        } for m in msgs ]
        mock_fetch_issue_messages.return_value = ["Issue 1"]
        mock_fetch_raw_files.return_value = [("src/test.java", "public void test() { // secure }")]
        mock_process_code.return_value = [{
            "method_signature": "public void test()",
            "method_body": "public void test() { // secure }"
        }]
        mock_analyze_method.return_value = {
            "sasd_detected": True, 
            "details": "SASD detail"
        }
        mock_map_to_cwe.return_value = {
            "cwe_mapping": "CWE-999: Dummy", 
            "details": "Successful CWE mapping"
        }
        payload = {
            "repo": "owner/repo"
        }
        response = self.client.post('/analyze/repo', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("commit_analysis", data)
        self.assertIn("issue_analysis", data)
        self.assertIn("code_analysis", data)
        self.assertEqual(len(data["commit_analysis"]), 1)
        self.assertEqual(len(data["issue_analysis"]), 1)
        self.assertGreater(len(data["code_analysis"]), 0)

    def test_analyze_repo_missing_repo(self):
        resp = self.client.post('/analyze/repo', json={})
        self.assertEqual(resp.status_code, 422)

    @patch("api.routes.endpoints.fetch_commit_messages", side_effect=Exception("Repo crash"))
    def test_analyze_repo_exception(self, _):
        resp = self.client.post('/analyze/repo', json={"repo": "owner/repo"})
        self.assertEqual(resp.status_code, 500)

    @patch("api.routes.endpoints.requests.get")
    def test_repo_structure(self, mock_get):
        root_response = [{
            "name": "folder", 
            "type": "dir", 
            "url": "http://dummy/folder"
        },
        {
            "name": "file.txt", 
            "type": "file", 
            "path": "file.txt"
        }]

        folder_response = []
        mock_resp_root = MagicMock()
        mock_resp_root.status_code = 200
        mock_resp_root.json.return_value = root_response

        mock_resp_folder = MagicMock()
        mock_resp_folder.status_code = 200
        mock_resp_folder.json.return_value = folder_response

        mock_get.side_effect = [mock_resp_root, mock_resp_folder]

        response = self.client.get('/repo/structure?repo_url=owner/repo')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("structure", data)
        self.assertEqual(len(data["structure"]), 2)

    @patch("api.routes.endpoints.fetch_raw_code")
    def test_file_content(self, mock_fetch_raw_code):
        mock_fetch_raw_code.return_value = "file content"
        payload = {
            "repo": "owner/repo", 
            "file_path": "file.txt"
        }
        response = self.client.post('/file/content', json=payload)
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("file_content", data)
        self.assertEqual(data["file_content"], "file content") 

if __name__ == "__main__":
    unittest.main(verbosity=2)
