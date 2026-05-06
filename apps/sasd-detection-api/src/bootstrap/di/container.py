"""
Container to hold modules
"""
from src.bootstrap.di.module.application import ApplicationModule
from src.bootstrap.di.module.infrastructure import InfrastructureModule

class Container:
    """
    Dependency container
    """
    modules = [ApplicationModule(), InfrastructureModule()]
