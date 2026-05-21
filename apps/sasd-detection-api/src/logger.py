"""
src/logger.py
"""

from logging.config import dictConfig


def configure_logging(level: str = "INFO"):
    """
    Application logging config
    """
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {"format": "[%(asctime)s] %(levelname)s %(name)s: %(message)s"}
            },
            "handlers": {"console": {"class": "logging.StreamHandler", "formatter": "default"}},
            "root": {"level": level, "handlers": ["console"]},
        }
    )
