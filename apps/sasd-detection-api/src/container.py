"""
src/container.py
"""

from injector import Module

from src.module import ClientsModule, ServicesModule


def get_modules() -> list[Module]:
    """
    Return modules for DI
    """
    return [ClientsModule(), ServicesModule()]
