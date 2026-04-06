"""
Application container for wiring together dependencies.
"""
from apps.backend.src.di.module.data import DataModule
from apps.backend.src.di.module.usecase import UsecaseModule

class AppContainer:
    """
    AppContainer.
    """
    modules = [DataModule(), UsecaseModule()]
