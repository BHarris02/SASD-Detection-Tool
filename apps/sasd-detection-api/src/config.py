"""
src/config.py
"""


class Config:
    """
    Base config class
    """

    DEBUG = False
    TESTING = False
    CORS_ORIGINS = []


class DevelopmentConfig(Config):
    """
    Development
    """

    DEBUG = True
    CORS_ORIGINS = ["http://localhost:5173"]


class TestingConfig(Config):
    """
    Testing
    """

    TESTING = True


class ProductionConfig(Config):
    """
    Production
    """

    DEBUG = False


config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
