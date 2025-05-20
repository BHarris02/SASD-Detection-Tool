"""
Module Name: config.py
Description: This module manages the application's configuration settings by loading
            environment variables. It uses the dotenv package to load variable from a .env
            file when running in a development environment.
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - os
    - dotenv
Usage:
    Import the Config class into your application to configure Flask settings and access
    environment variables.
"""

import os
from dotenv import load_dotenv

if os.getenv("FLASK_ENV") == "development":
    load_dotenv()

GITHUB_API_URL = os.getenv("GITHUB_API_URL")
GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")

GITHUB_CLIENT_ID  = os.getenv("GITHUB_CLIENT_ID ")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")

GITHUB_ACCESS_TOKEN_URL = os.getenv("GITHUB_ACCESS_TOKEN_URL")
GITHUB_API_USER_URL = os.getenv("GITHUB_API_USER_URL")

OPENAI_MODEL = os.getenv("OPENAI_MODEL")
OPENAI_KEY = os.getenv("OPENAI_KEY")

class Config:
    SECRET_KEY = os.getenv("APP_SECRET_KEY", "default_secret_key")
    DEBUG = os.getenv("FLASK_ENV") == "development"
    TESTING = os.getenv("FLASK_ENV") == "testing"