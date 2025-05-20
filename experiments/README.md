# Detecting Self-Admitted Security Debt (SASD) in Software Projects Using Natural Language Processing (NLP) - Experiments

This repository contains the code used to conduct experiments and gather results detailed in the Results and Analysis section of the Research Article. This document will provide a guide to help you set up and replicate those results.

---

## Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
    - [Installing the Backend Flask API](#installing-the-backend-flask-api)
    - [Installing the Experimental Pipeline](#installing-the-experimental-pipeline)
- [Usage](#usage)
    - [Replication Guide](#replication-guide)
    - [Running the Experiments](#running-the-experiments)
        - [Detection Experiment](#detection-experiment)
        - [Mapping Experiment](#mapping-experiment)
    - [Generating Graphs](#generating-graphs)
- [Additional Information](#additional-info)
- [License](#license)
- [Support](#support)

---

## Prerequisites

- **Python 3.9 or higher**
- **pip (Python Package Installer)**
- **Git**
- **Backend Flask API**

---

## Installation

In order to run the Experimental Pipeline, the backend Flask API will need to be set up and running.

### Installing the Backend Flask API

If you have either the Flask API running as a standalone component, or have Dockerised the React frontend and Flask API into one unified deployment, you can skip this step.

1. **Clone the Repository:**

```bash
git clone https://gitlab.eeecs.qub.ac.uk/40323251/CSC4006-SASD-Detection-Tool.git
cd csc4006-sasd-detection-tool-backend
```

2. **Create a Virtual Environment:**

```bash
python -m venv venv
source venv/bin/activate    # Linux/MacOS
venv/scripts/activate       # Windows
```

3. **Install Dependencies:**

```bash
pip install -r requirements.txt
```

4. **Configuration**

Create a .env file in the project root directory. Use the following template:

```bash
FLASK_ENV=development

GITHUB_API_URL = "https://api.github.com"
GITHUB_API_TOKEN = <your_github_api_token>

GITHUB_CLIENT_ID = <your_github_client_id>
GITHUB_CLIENT_SECRET = <your_github_client_secret>

GITHUB_ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"
GITHUB_API_USER_URL = "https://api.github.com/user"

OPENAI_MODEL = "gpt-3.5-turbo"
OPENAI_KEY = <your_openai_key>
```

- **GITHUB_API_TOKEN:** A personal access token from GitHub for API calls.

- **GITHUB_CLIENT_ID:** Unique ID for the signed-in user.

- **GITHUB_CLIENT_SECRET:** Used to get an access token for the signed-in user.

- **OPENAI_KEY:** Your OpenAI API key to perform tasks using NLP.

<br>


5. **Start the Flask Server:**

```bash
python main.py
```

Your Flask API will be available at:

```http
http://127.0.0.1:5000
```
---

### Installing the Experimental Pipeline

Once you have the Flask API set up and running, you can proceed with installing the Experimental Pipeline.

1. **Clone the Repository:**

```bash
git clone https://gitlab.eeecs.qub.ac.uk/40323251/csc4006-sasd-detection-tool-experimental-utilities.git
cd csc4006-sasd-detection-tool-experimental-utilities
```

2. **Configuration:**

Please ensure the address and port of the **API_URL** in the *config.py* file is the same as your running Flask API:

```bash
API_URL = "http://127.0.0.1:5000/api/analyze/method"
```

---

## Usage

**Important Note** <br>
As outlined in the Limitations subsection of the Research Article, older Natural Language Processing models, such as GPT-3.5-Turbo, have a tendency to produce slightly different responses each time they are posed with the same query. Due to this, if you wish to see the results portrayed in the Research Article, you should **NOT** run the commands to execute the experiment, but rather only execute the **analyses** and **graph** commands. Running the experiment commands will override the data used in the Result and Analysis Section. If you wish to replicate the results from the Research Article follow the **Replication Guide** steps, otherwise proceed with the **Running the Experiments** steps.

---

### Replication Guide

1. **Detection Experiment Analysis:**

In order to see the raw metrics of the Detection Experiment, run the below command:

```bash
python main.py detection_analysis
```

2. **Mapping Experiment Analysis:**

In order to see the raw metrics of the Mapping Experiment, run the below command:

```bash
python main.py mapping_analysis
```

3. **Creating Experiment Results Graphs:**

In order to generate graphs based on the results, run the below command:

```bash
python main.py graphs
```

---

### Running the Experiments

Follow this series of steps in order to produce a new set of results:

1. **Dataset Creation:**

Ensure you have a folder named **data** in the root directory. Ensure the *technical_debt_dataset.csv* is inside this folder (You can ignore any other files). <br>

Run the **files** command to create a stratified, augmented sample of the dataset:

```bash
python main.py files
```

This should create (or replace) **three** files in the **data** folder:

- converted_dataset.py

- stratified_sample.csv

- stratified_sample_augmented.csv

---

#### Detection Experiment

Ensure your Flask API is running.

1. **Run the Detection Experiment:**

```bash
python main.py detection
```

This will take some time to run depending on your hardware. <br>

Once complete, you will need to do manual verification on the **10** sets of verification samples (30 samples total).

Each Verification Sample contains the following:

- **comment:** The source code comment, issue or commit message.

- **baseline_result:** Whether or not the keyword-based baseline detection method detected SASD (True or False).

- **nlp_result:** Whether or not the NLP detection method detected SASD (True or False).

- **sasd:** This is where you determine if the **comment** indicates SASD (True). By default this will be False for all comments.

<br>


2. **Detection Experiment Analysis:**

Once you have manually verified all 30 samples, to see the raw metrics of the Detection Experiment, run the below command:

```bash
python main.py detection_analysis
```

---

#### Mapping Experiment

Ensure you Flask API is running. <br>

In order to run the Mapping Experiment, please ensure you have **completed the Detection Experiment first**.

1. **Run the Mapping Experiment:**

```bash
python main.py mapping
```

This will create Verification samples.

2. **Run the Verification Command:**

In the *config.py* file you can find the *SYNTHETIC_SASD_COMMENTS_MAPPINGS* dictionary. If you wish to change the CWE mappings for each synthetic SASD comment in the dataset you can navigate here to do so before executing the Verification command.

```bash
python main.py mapping_verification
```

3. **Mapping Experiment Analysis:**

```bash
python main.py mapping_analysis
```

---

### Generating Graphs

After running both experiments, you can execute the following command to create graphs:

```bash
python main.py graphs
```

---

## Additional Information

For the experiments conducted to collect results for the Research Article the following seeds were used:

```bash
Detection Experiment Seeds:

Run 1: [42, 99, 123]
Run 2: [42, 99, 123]
Run 3: [271828, 314159, 161803]

Run 4: [42, 99, 123]
Run 5: [42, 99, 123]
Run 6: [123456, 789012, 345678]

Run 7: [42, 99, 123]
Run 8: [42, 99, 123]
Run 9: [202305, 987654, 135790]

Run 10: [42, 99, 123]
```

---

## License

This software is licensed under the MIT License. See the LICENSE file for details.

---

## Support

For support, questions, or to report issues, please contact the project maintainer directly:


- **Maintainer:** Blake Harris (bharris06@qub.ac.uk)

---

