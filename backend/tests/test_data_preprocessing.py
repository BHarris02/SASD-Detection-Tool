"""
Module Name: test_data_preprocessing.py
Description: This module contains unit test cases for functions in the data_preprocesing module.
            The tests verify the correctness of:
                - process_comments: ensuring comments are correctly extracted from source code blocks
                - process_code: ensuring method blocks are correctly identified and extracted
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - unittest
    - api.utils.data_preprocessing
Usage:
    Run the test suite from the command line:
        python -m unittest tests.test_data_preprocessing
"""
import unittest
from api.utils.data_preprocessing import process_code, process_comments

class TestDataPreprocessing(unittest.TestCase):

    def setUp(self):
        self.identifier = "//"
        self.dummy_code = """
            // test comment
            public static void testMethod() {
                // TODO: fix this code
                int a = 10;
            }
        """

    def test_process_comments(self):
        comments = process_comments(self.dummy_code, self.identifier)
        expected_comments = [
            "test comment",
            "TODO: fix this code"
        ]
        self.assertEqual(comments, expected_comments)
    
    def test_process_code(self):
        methods = process_code(self.dummy_code)
        self.assertIsInstance(methods, list)
        self.assertGreater(len(methods), 0)

        for method in methods:
            self.assertIn("method_signature", method)
            self.assertIn("method_body", method)

if __name__ == '__main__':
    unittest.main(verbosity=2)