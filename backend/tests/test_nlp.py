"""
Module Name: test_nlp.py
Description: This module contains unit test cases for functions in the nlp module.
            The tests verify the correctness of:
                - analyze_messages: ensures commit and issue messages are correctly procsesed to detected SASD
                - analyze_method: ensures method comments are correctly analyzed for SASD
                - map_to_cwe: ensures accurate mappings of SASD instances to CWEs
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - unittest
    - unittest.mock
    - api.utils.nlp
Usage:
    Run the test suite from the command line:
        python -m unittest tests.test_nlp
"""
import unittest
from unittest.mock import patch
from api.utils.nlp import analyze_messages, analyze_method, map_to_cwe

class TestNLPModule(unittest.TestCase):

    def setUp(self):
        self.commit_messages = [
            "Fix security issues in API",
            "Temporary fix for authentication bug",
            "Update README"
        ]
        self.method_body = """public void example() {
            //TODO: Refactor security logic
            int idNumber = 42; 
        }"""
        self.sasd_response = "Yes: This method contains a TODO comment indicating a need for refactoring"
        self.cwe_response = "CWE-798: Use of Hard-coded Credentials"


    @patch("api.utils.nlp.map_to_cwe", return_value="")
    @patch("api.utils.nlp.openai.ChatCompletion.create")
    def test_analyze_messages_mocked(self, mock_create, mock_map_to_cwe):
        mock_create.return_value = {
            "choices": [{
                "message": {"content": self.sasd_response}
            }]
        }
        res = analyze_messages(self.commit_messages)
        self.assertEqual(len(res), len(self.commit_messages))
        for result in res:
            self.assertIn("message", result)
            self.assertIn("sasd_detected", result)
            self.assertIn("details", result)
            self.assertTrue(result["sasd_detected"])
            self.assertEqual(result["details"].strip(), self.sasd_response)

    @patch("api.utils.nlp.openai.ChatCompletion.create", side_effect=Exception("Model error"))
    def test_analyze_messages_exception(self, _):
        res = analyze_messages(["Message 1"])
        self.assertEqual(len(res), 1)
        self.assertEqual(res[0]["sasd_detected"], "Exception")
        self.assertIn("An Exception occured:", res[0]["details"])

    @patch("api.utils.nlp.openai.ChatCompletion.create")
    def test_analyze_method_mocked(self, mock_create):
        mock_create.return_value = {
            "choices": [{
                "message": {"content": self.sasd_response}
            }]
        }
        res = analyze_method(self.method_body)
        self.assertIn("sasd_detected", res)
        self.assertIn("details", res)
        self.assertTrue(res["sasd_detected"])
        self.assertEqual(res["details"], self.sasd_response)

    @patch("api.utils.nlp.openai.ChatCompletion.create", side_effect=Exception("Crash"))
    def test_analyze_method_exception(self, _):
        res = analyze_method("def insecure(): pass")
        self.assertIn("sasd_detected", res)
        self.assertFalse(res["sasd_detected"])
        self.assertIn("An Exception occurred:", res["details"])

    @patch("api.utils.nlp.openai.ChatCompletion.create")
    def test_map_to_cwe_mocked(self, mock_create):
        mock_create.return_value = {
            "choices": [{
                "message": {"content": self.cwe_response}
            }]
        }
        res = map_to_cwe(self.sasd_response)
        self.assertIn("cwe_mapping", res)
        self.assertIn("details", res)
        self.assertEqual(res["cwe_mapping"], self.cwe_response)
        self.assertEqual(res["details"], "Successful CWE mapping")

    @patch("api.utils.nlp.openai.ChatCompletion.create", side_effect=Exception("Failure"))
    def test_map_to_cwe_exception(self, _):
        res = map_to_cwe("Yes: hardcoded password")
        self.assertIsNone(res["cwe_mapping"])
        self.assertIn("An Exception occurred:", res["details"])

    @patch("api.utils.nlp.map_to_cwe", return_value="Mapped CWE")
    @patch("api.utils.nlp.openai.ChatCompletion.create")
    def test_analyze_messages_with_sasd_detection(self, mock_create, _):
        mock_create.return_value = {
            "choices": [{
                "message": {
                    "content": "Yes: Detected SASD"
                }
            }]
        }
        res = analyze_messages(["Intentional SASD message"])
        self.assertEqual(len(res), 1)
        self.assertTrue(res[0]["sasd_detected"])
        self.assertIn("Mapped CWE", res[0]["details"])

if __name__ == "__main__":
    unittest.main(verbosity=2)
