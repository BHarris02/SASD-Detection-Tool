"""
src/strategy/python.py
"""
import ast
from ast import FunctionDef, AsyncFunctionDef
from io import StringIO
from textwrap import dedent
from tokenize import generate_tokens, COMMENT

from src.exception import (
    NoCommentsFoundException,
    NoMethodFoundException,
    UnparsableMethodException
)
from src.model import Method
from src.strategy import MethodProcessor


class PythonMethodProcessor(MethodProcessor):
    """
    `MethodProcessor` implementation for Python source code
    """
    def parse(self, source_code: str) -> Method:
        # remove indentation
        source_code = dedent(source_code)

        # attemt to parse the source code
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            raise UnparsableMethodException from e

        # locate the method
        node = next(
            (n for n in tree.body if isinstance(n, (FunctionDef, AsyncFunctionDef))),
            None
        )

        if node is None:
            raise NoMethodFoundException()

        # split the code by line
        lines = source_code.splitlines()
        # locate the method signature
        signature = "\n".join(lines[node.lineno - 1:node.body[0].lineno - 1]).strip()

        docstring = ast.get_docstring(node) or ""
        comments = self._extract_comments(source_code)

        if not docstring and not comments:
            raise NoCommentsFoundException()

        return Method(
            a_id="1",
            signature=signature,
            docstring=docstring,
            comments=comments
        )

    def _extract_comments(self, source_code: str) -> str:
        tokens = generate_tokens(StringIO(source_code).readline)
        return "\n".join(
            tok.string.lstrip("#").strip()
            for tok in tokens
            if tok.type == COMMENT
        )
