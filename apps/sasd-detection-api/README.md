# sasd-detection-tool-api

![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/flask-3.1.3-black?logo=flask&logoColor=white)
[![CI](https://github.com/BHarris02/SASD-Detection-Tool/actions/workflows/sasd-detection-api-ci.yml/badge.svg)](https://github.com/BHarris02/SASD-Detection-Tool/actions/workflows/ci.yml)
[![License](https://img.shields.io/github/license/BHarris02/SASD-Detection-Tool)](https://github.com/BHarris02/SASD-Detection-Tool/blob/main/LICENSE)

## :clipboard: Overview

`sasd-detection-tool-api` is the Python Flask RESTful backend API for the SASD Detection Tool.

The API fetches artefacts from version control system repositories, including commit messages, issues, and source code. These artefacts are passed to a configurable LLM provider for natural language processing, where each artefact is analysed for instances of _Self-Admitted Security Debt_ (SASD). Any detected debt instances are mapped to a relevant entry in the [Common Weakness Enumerations](https://cwe.mitre.org/) (CWE).

---

## :rocket: Getting Started

### :gear: Pre-requisites

- Python 3.10+
- pip
- Docker (optional, for containerised runs)

### :inbox_tray: Installation

```bash
git clone git@github.com:BHarris02/SASD-Detection-Tool.git
cd SASD-Detection-Tool/apps/sasd-detection-api

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

### :key: Environment Variables

Configuration is managed via a `.env` file. To get started:

```bash
cp .env.example .env
```

Then populate `.env` with your values:

| **Variable**           | **Description**                                                     | **Required**       |
| ---------------------- | ------------------------------------------------------------------- | ------------------ |
| `GITHUB_API_URL`       | `https://api.github.com`                                            | :white_check_mark: |
| `GITHUB_API_TOKEN`     | Personal access token for API authentication                        | :white_check_mark: |
| `ANALYSIS_PROVIDER`    | LLM provider to use for analysis (`openai`, `anthropic`)            | :white_check_mark: |
| `ANALYSIS_MODEL_URL`   | Base URL for an LLM provider &mdash; not required for all providers | :warning:          |
| `ANALYSIS_MODEL_TOKEN` | API key for LLM provider                                            | :white_check_mark: |
| `ANALYSIS_MODEL`       | Model identifier for LLM provider                                   | :white_check_mark: |

### :arrow_forward: Running the API

Locally:

```bash
python main.py
```

The API is served at `http://localhost:5000`

With Docker:

```bash
# development
docker build -f Dockerfile.dev -t sasd-detection-api:dev .
docker run --rm -p 5000:5000 --env-file .env sasd-detection-api:dev

# production
docker build -f Dockerfile.prod -t sasd-detection-api:prod .
docker run --rm -p 5000:5000 --env-file .env sasd-detection-api:prod
```

### :test_tube: Running Tests

```bash
python -m unittest discover -v
```
---

## :satellite: API Reference

All endpoint URLs are prefixed by `/api/v1`.

### Health

| **Method** | **Endpoint** | **Description** |
| ---------- | ------------ | --------------- |
| `GET`      | `/health`    | Health check    |

### Analysis

| **Method** | **Endpoint** | **Description**                                      |
| ---------- | ------------ | ---------------------------------------------------- |
| `POST`     | `/commits`   | Analyse commits in a repository                      |
| `POST`     | `/issues`    | Analyse issues in a repository                       |
| `POST`     | `/file`      | Analyse a single file in a repository                |
| `POST`     | `/method`    | Analyse a user-provided source code methods comments |

---