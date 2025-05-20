# SASD Detection Tool

**This repository contains the final project for my Master of Engineering (MEng) in Software Engineering at Queen's University Belfast, completed in 2025.**

The tool was developed as part of my MEng dissertation and uses Natural Language Processing (NLP) to automate the detection and categorisation of Self-Admitted Security Debt (SASD) in software projects.

All code, experimental utilities, and supporting documents (Research Article, Software Development Report, and Presentation) are included for academic and demonstrative purposes.

**Disclaimer:**

My Research Article has not been published or independently reviewed. Thus, please do not cite it as an academic source.

## About the Project

As previously mentioned, this project was completed for my MEng final dissertation at Queen's University Belfast:

 **_Detecting Self-Admitted Security Debt in Software Projects using Natural Language Processing_**

It involved researching, designing, and implementing a tool to identify and categorise Self-Admitted Security Debt in software project artifacts using NLP techniques.

For more details on the project's background, methodologies used, and our findings, please see the included Research Article in the [`docs`](./docs/Research%20Article/) folder.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Experimental Utilities](#experimental-utilities)
- [Documentation](#documentation)
- [License](#license)
- [Contact](#contact)

## Project Overview

The SASD Detection Tool consists of four main components:

- **Backend (Flask API):**

    Provides RESTful endpoints for analysis and data retrieval. The backend fetches data from GitHub repositories—including commit messages, issue tracker entries, and source code files—preprocesses textual information, detects instances of SASD using NLP, and maps them to relevant Common Weakness Enumerations (CWEs) for vulnerability classification. Interactive API documentation is automatically generated.

- **Frontend (React):**

    Delivers a dynamic, web-based interface for users to explore and analyze SASD in repositories. The frontend allows users to input repository details, trigger various forms of analysis (commit messages, issues, file comments, and full repository scans), and review results through intuitive navigation and visualisation.

- **VSCode Extension:**

    Integrates SASD detection into the Visual Studio Code environment, allowing developers to analyze code, commits, issues, or highlighted segments directly within the IDE, streamlining the workflow and surfacing security debt insights without context-switching.

- **Experimental Utilities:**

    Contains scripts and tools used to conduct experiments supporting the research article, enabling replication or further investigation of the reported results.

The entire system is designed to be deployed easily using Docker Compose, enabling quick installation and integration of all components.

## Installation Guide

### Prerequisites

- Docker
- Docker Compose (if not bundled with Docker Desktop)
- Visual Studio Code (Optional, for VSCode Extension)

### Installation

### Clone the Repository

```bash
git clone https://gitlab.com/BHarris02/sasd-detection-tool.git
cd sasd-detection-tool
```

### Set Up Environment Variables

Copy the example environment file and update it with the required API keys, tokens, etc.

```bash
cp .env.example .env
```

### Build and Run the System

```bash
docker-compose up --build
```

- The **frontend** will be available at http://localhost:3000
- The **backend** will be available at http://localhost:5000

---

### VSCode Extension Installation

- After the system is built, the extension package (.vsix) can be found in the /vscode-extension/dict directory.

- To install the extension in VSCode:

    Go to **Extensions** > **...** **(three-dot menu)** > **Install from VSIX** ... and select the .vsix file.

---

### Shutting Down the System

To stop and remove the containers, press CTRL+C in your terminal and then run:

```bash
docker-compose down
```

---

### Troubleshooting

- Ensure all required environment variables are set in your .env file.

- If ports 3000 or 5000 are in use, stop other processes or change the ports in docker-compose.yml.

- For more details or issues, contact the project author.

---

## Usage

### Accessing the Application

- **Frontend Web Interface:**

    Open your browser and navigate to http://localhost:3000.

    Use the interface to enter a GitHub repository (e.g. user/repo), view the repository structure, select a file, and initiate various analyses (commits, issues, code files, full repository scan).

- **Backend API:**

    The API is available at http://localhost:5000

    Interactive API documentation is available at http://localhost:5000/docs.

---

### VSCode Extension

- After installing the VSCode extension, navigate to the extension in the sidebar.

- Analyse commit messages, issue tracker entries, active code file comments, or highlighted code comments directly within VSCode via extension commands.

- Results will be displayed in the VSCode UI.

---

### Example Workflow

**1.** Start the tool with Docker Compose.

**2.** Open the web UI, enter a public GitHub repository, select a file, and analyse for SASD.

**3.** (Optionally) Install and use the VSCode extension to analyse code from within your editor.

---

## Experimental Utilities

The /experiments directory contains scripts and tools use to conduct experiments and generate results for the accompanying Research Article. These utilities are provided to support replication of the study's findings and to enable further exploration or validation by reviewers.

- **Note:**

    The code in this directory is for experimental and research purposes only.

    It is not required for day-to-day use of the SASD Detection Tool.

For instructions on setting up and running these experiments, please refer to the [`experiments/README.md`](./experiments/README.md).

---

## Documentation

Comprehensive documentation and supporting materials for this project are included in the [`docs`](./docs/) directory:

- **Research Article:** Full academic report detailing the project background, methodology, experiments, and results.

- **Software Development Report:** Technical documentation describing the design, implementation, and architectural decisions of the tool.

- **Presentation Slides:** Materials used for the project presentation to an assessor.

**Disclaimer:**

The research article in this repository has not been peer-reviewed or formally published.

Is is included **for demonstration and reference purposes ONLY**, and should not be cited as an academic resource.

---

## License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE) for details.

---

## Contact

If you have any questions or would like to discuss this project, feel free to contact me:

- **Name:** Blake Harris
- **Email:** dev.blake.harris@gmail.com