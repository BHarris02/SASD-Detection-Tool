"""
src/module/strategies.py
"""
from injector import Module, provider, singleton

from src.model import MethodLanguage
from src.strategy import MethodProcessorRegistry, PythonMethodProcessor


class StrategiesModule(Module):
    """
    Wire together and provide strategy singletons
    """

    @provider
    @singleton
    def provide_method_processor_registry(self) -> MethodProcessorRegistry:
        """
        Provide a configured `MethodProcessorRegistry`
        """
        registry = MethodProcessorRegistry()
        registry.register(MethodLanguage.PYTHON, PythonMethodProcessor())
        return registry
