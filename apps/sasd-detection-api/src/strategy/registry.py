"""
src/strategy/registry.py
"""
from src.exception import UnsupportedLanguageException
from src.model import MethodLanguage
from src.strategy.api import MethodProcessor


class MethodProcessorRegistry:
    """
    Registry that maps a `CodeLanguage` to its `MethodProcessor`
    """
    def __init__(self):
        self._processors: dict[MethodLanguage, MethodProcessor] = {}

    def register(self, language: MethodLanguage, processor: MethodProcessor) -> None:
        """
        Register a `MethodProcessor` for its given `CodeLanguage`

        :param language: The `MethodLanguage`
        :param processor: The associated `MethodProcessor`
        """
        self._processors[language] = processor

    def get(self, language: MethodLanguage) -> MethodProcessor:
        """
        Retrieve a `MethodProcessor` registered for a language

        :param language: The `MethodLanguage` processor to retrieve

        :raises UnsupportedLanguageException:
        """
        try:
            return self._processors[language]
        except KeyError as e:
            raise UnsupportedLanguageException from e
