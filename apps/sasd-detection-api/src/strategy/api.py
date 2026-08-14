"""
src/strategy/api.py
"""
from abc import ABC, abstractmethod

from src.model import Method


class MethodProcessor(ABC):
    """
    Abstract base class for language-specific method parsers
    """
    @abstractmethod
    def parse(self, source_code: str) -> Method:
        """
        Parse the source code of a single method into a `Method`

        :param source_code: The string method body with its docstring and comments

        :returns Method: A parsed method
        """
