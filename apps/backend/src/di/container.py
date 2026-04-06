"""
Application container for wiring together dependencies.
"""
from di.module.data import DataModule
from di.module.usecase import UsecaseModule

class AppContainer:
    """
    AppContainer.
    """
    modules = [DataModule(), UsecaseModule()]
