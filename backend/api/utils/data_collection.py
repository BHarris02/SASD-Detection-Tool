"""
Module Name: data_collection.py
Description: This module provides utility functions for fetching GitHub repository data via GitHub API.
            It includes methods to :
                - Fetch commit messages
                - Fetch issue messages
                - Fetch raw code from a specific file
                - Recursively fetch raw code from all files
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - requests
    - json
    - base64
    - api.utils.config
Usage:
    Import the requred functions into your application. E.g.:
        from api.utils.data_collection import fetch_commit_messages, fetch_raw_code
"""
import requests, json
import base64
from api.utils.config import (GITHUB_API_URL, GITHUB_API_TOKEN)

headers = {
    "Authorization": f"token {GITHUB_API_TOKEN}"
    }

"""
Fetch all commit messages from a provided repo
:param repo: str in format 'owner/repo'
:return: List containing commit messages
"""
def fetch_commit_messages(repo: str) -> list:
    repo_url: str = f"{GITHUB_API_URL}/repos/{repo}/commits"
    resp = requests.get(repo_url, headers=headers)
    commits = resp.json()
    return [commit['commit']['message'] for commit in commits]

"""
Fetch all issues messages from a repo
:param repo: str in format 'owner/repo'
:return: list with issues messages
"""
def fetch_issue_messages(repo: str) -> list:
    repo_url: str = f"{GITHUB_API_URL}/repos/{repo}/issues"
    resp = requests.get(repo_url, headers=headers)
    issues = resp.json()
    return [f"{issue['title']}: {issue['body']}" for issue in issues]

"""
Fetch raw code from a specific file in a repo
:param repo: str in format 'owner/repo'
:file_path: str of path to file
:return: str with contents of code file
"""
def fetch_raw_code(repo: str, file_path: str) -> list:
    repo_url: str = f"{GITHUB_API_URL}/repos/{repo}/contents/{file_path}"
    resp = requests.get(repo_url, headers=headers)
    comments = resp.json()
    return base64.b64decode(comments["content"]).decode("utf-8")

"""
Fetch raw code from all files in a repo
:param repo: str in format 'owner/repo'
:path: str of path to repo
:return: list with contents of each file
"""
def fetch_raw_files(repo: str, path: str) -> list:
    repo_url: str = f"{GITHUB_API_URL}/repos/{repo}/contents/{path}"
    resp = requests.get(repo_url, headers=headers)
    files: json = resp.json()
    all_files: list = []
    for file in files:
        if file["type"] == "file":
            content: list = fetch_raw_code(repo, file["path"])
            all_files.append((file["path"], content))
        elif file["type"] == "dir":
            all_files.extend(fetch_raw_files(repo, file["path"]))
    return all_files

