"""
tests/strategy/test_python_method_processor.py
"""
from unittest import TestCase

from src.exception import (
    NoCommentsFoundException,
    NoMethodFoundException,
    UnparsableMethodException
)
from src.strategy import PythonMethodProcessor


# pylint: disable=missing-function-docstring
class PythonMethodProcessorTest(TestCase):
    """
    Unit tests for `PythonMethodProcessor`
    """

    def setUp(self):
        self._processor = PythonMethodProcessor()

    def test_parse_succeeds(self):
        source_code = (
            "def add(a: int, b: int) -> int:\n"
            "    \"\"\"Add two numbers.\"\"\"\n"
            "    # simple addition\n"
            "    return a + b\n"
        )

        method = self._processor.parse(source_code)

        self.assertEqual(method.signature, "def add(a: int, b: int) -> int:")
        self.assertEqual(method.docstring, "Add two numbers.")
        self.assertEqual(method.comments, "simple addition")

    def test_parse_async_succeeds(self):
        source_code = (
            "async def fetch(a: int, b: int) -> int:\n"
            "    \"\"\"Fetch asynchronously.\"\"\"\n"
            "    # await something\n"
            "    return a + b\n"
        )

        method = self._processor.parse(source_code)

        self.assertEqual(method.signature, "async def fetch(a: int, b: int) -> int:")
        self.assertEqual(method.docstring, "Fetch asynchronously.")
        self.assertEqual(method.comments, "await something")

    def test_parse_comment_follows_signature(self):
        source_code = (
            "def add(a: int, b: int) -> int:  # inline comment\n"
            "    return a + b\n"
        )

        method = self._processor.parse(source_code)

        self.assertEqual(method.comments, "inline comment")

    def test_parse_throws_unparsable_method(self):
        source_code = "def foo(:\n    pass\n"

        with self.assertRaises(UnparsableMethodException):
            self._processor.parse(source_code)

    def test_parse_throws_no_method_found(self):
        source_code = "x = 1\ny = 2\n"

        with self.assertRaises(NoMethodFoundException):
            self._processor.parse(source_code)

    def test_parse_no_docstring(self):
        source_code = (
            "def subtract(a: int, b: int) -> int:\n"
            "    return a - b  # simple subtraction\n"
        )

        method = self._processor.parse(source_code)

        self.assertEqual(method.signature, "def subtract(a: int, b: int) -> int:")
        self.assertEqual(method.docstring, "")
        self.assertEqual(method.comments, "simple subtraction")

    def test_parse_no_comments(self):
        source_code = (
            "def divide(a: int, b: int) -> float:\n"
            "    \"\"\"Divide two numbers.\"\"\"\n"
            "    return a / b\n"
        )

        method = self._processor.parse(source_code)

        self.assertEqual(method.signature, "def divide(a: int, b: int) -> float:")
        self.assertEqual(method.docstring, "Divide two numbers.")
        self.assertEqual(method.comments, "")

    def test_parse_no_comments_no_docstring(self):
        source_code = (
            "def multiply(a: int, b: int) -> int:\n"
            "    return a * b\n"
        )

        with self.assertRaises(NoCommentsFoundException):
            self._processor.parse(source_code)
