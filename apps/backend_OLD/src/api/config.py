"""
Application configuration classes.
"""
from os import getenv

class AppConfig:
    """
    Base config class.
    """
    SECRET_KEY = getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False

class DevelopmentConfig(AppConfig):
    """
    Development config class.
    """
    DEBUG = True

class TestingConfig(AppConfig):
    """
    Testing config class.
    """
    TESTING = True

class ProductionConfig(AppConfig):
    """
    Production config class.
    """

CONFIG_MAP = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
