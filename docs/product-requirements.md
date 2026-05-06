# Product Requirements

## Background & Motivation

In software development, the metaphor of _Technical Debt_ (TD) is used to describe trade-offs between short-term
productivity and long-term code quality. _Security Debt_, a subset of Technical Debt, refers to deferred
security-related tasks to accelerate development timelines, thus potentially leaving systems vulnerable to attack.
Security Debt encapsulates both known and unknown security issues that are unaddressed, compromising software security.

Developers sometimes acknowledge their trade-offs explicitly in code comments, commit messages, issues, and pull
requests; known as _Self-admitted Technical Debt_ (SATD). In the realm of security, this is referred to as
_Self-admitted Security Debt_ (SASD). Despite the criticality of security, existing tools focus primarily on detecting
and logging general Technical Debt, and fail to address security-related concerns specifically. This gap motivates the
need for a dedicated, automated solution.

## Problem Statement

Detecting SASD is often challenging due to the large, unorganised nature of modern codebases and the unstructured
textual data found across project artefacts (commits, code comments, issues, and pull requests). As AI agents become
increasingly integrated into everyday development workflows, the volume and velocity of code being produced &mdash; and
the debt being introduced &mdash; continues to grow, making manual detection increasingly impractical.

Although tools exist to address general code quality issues, they lack the mechanisms to automatically detect and
classify security-related debt at scale. Without explicit categorisation of SASD, security and development teams are
unable to prioritise and remediate issues efficiently. Furthermore, no existing solutions map SASD findings to 
established vulnerability frameworks, such as _Common Weakness Enumerations_ (CWE), which are widely recognised in the 
domain of software security. This absence of structured, actionable output means SASD frequently goes unresolved,
leaving software vulnerable to exploitation.

This tool targets **security engineers, project maintainers, and SecOps teams** who require an automated,
NLP-driven solution to detect, analyse, and categorise SASD &mdash; and map findings to recognised vulnerability
frameworks &mdash; at a scale that manual processes cannot achieve.

## Success Criteria

1. **Artefact Ingestion:** The tool successfully ingests project artefacts from developer-provided sources
2. **SASD Detection:** The tool identifies instances of SASD within the provided artefacts, achieving a minimum F1 
   Score of **80%** against a labelled benchmark dataset
3. **Categorisation:** Detected SASD instances are classified by type and severity
4. **CWE Mapping:** Each detected instance is mapped to one or more relevant _Common Weakness Enumerations_ (CWE)
   where applicable
5. **Structured Output:** The model returns findings as a valid **JSON response**, which is deserialised into domain
   entities and surfaced to the user via a RESTful API
6. **Actionable Reporting:** The frontend presents results in a human-readable format that enables security engineers
   and maintainers to prioritise and remediate findings
7. **Scalability:** The pipeline handles codebases of varying sizes without significant degradation in performance
   or accuracy

## Scope

### In Scope

- A **RESTful API** responsible for artefact ingestion, model orchestration, and returning structured findings
- A **React web client** for submitted artefacts and viewing analysis results in a human-readable format
- A **VS Code extension** providing an in-editor interface to the API, allowing developers to trigger analysis without
  leaving their IDE
- Integration with one or more pre-trained LLMs via API for SASD detection and CWE mapping of findings
- Structured JSON output deserialised into domain entities

### Out of Scope

- **No bespoke model training** &mdash; The tool will not involve training or fine-tuning a custom model from scratch;
  detection, categorisation, and analysis will rely on existing pre-trained large language models, with prompt
  engineering and/or retrieval augmentation used to tailor outputs to the SASD domain
- Remediation of detected SASD &mdash; the tool surfaces and prioritises findings only; it does not auto-fix issues
- Support for artefact sources beyond those explicitly defined
- Persistent storage of artefacts or analysis beyond a single session
- Private repositories &mdash; no integration with GitHub OAuth for access to private repositories (MVP Only)

## User Journeys

### 1. Developer wants to analyse repository commit messages

**Persona:** Developer or security engineer reviewing commit history for SASD

**Precondition:** User has access to the web client

- User enters repository URL and clicks **"Load Repository"**
- User clicks **"Analyse Commits"**
- System fetches commits from the remote VCS, maps raw responses to `CommitArtefact` domain entities, passes them to
  `NlpGateway` to get per-artefact analysis, and returns a list of `Analysis` results
- User views per-commit analysis on the web client

**Alternative Considerations:**

| Scenario                                           | Expected Behaviour                                     |
|----------------------------------------------------|--------------------------------------------------------|
| No repository URL provided                         | Validation error (client)                              |
| "Analyse Commits" clicked before "Load Repository" | Validation error (client) &mdash; no repository loaded |
| Invalid URL format                                 | Validation error (client) &mdash; invalid URL format   |
| URL does not exist or is unreachable               | Error (API) &mdash; `400 Bad Request`                  |
| Repository has no commits                          | Success &mdash; 204 No Content`                        |

### 2. Developer wants to analyse repository issues

**Persona:** Developer or security engineer reviewing open issues for SASD

**Precondition:** User has access to the web client

- User enters repository URL and clicks **"Load Repository"**
- User clicks **"Analyse Issues"**
- System fetches issues from the remote VCS, maps raw responses to `IssueArtefact` domain entities, passes them to
  `NlpGateway` to get per-artefact analysis, and returns a list of `Analysis` results
- User views per-issue analysis on the web client

**Alternative Considerations:**

| Scenario                                          | Expected Behaviour                                     |
|---------------------------------------------------|--------------------------------------------------------|
| No repository URL provided                        | Validation error (client) &mdash; no URL provided      |
| "Analyse Issues" clicked before "Load Repository" | Validation error (client) &mdash; no repository loaded |
| Invalid URL format                                | Validation error (client) &mdash; invalid URL format   |
| URL does not exist or is unreachable              | Error (API) &mdash; `400 Bad Request`                  |
| Repository has no issues                          | Success &mdash; `204 No Content`                       |

### 3. Developer wants to analyse a provided code snippet

**Persona:** Developer or security manager writing and analysing code simultaneously

**Precondition:** Developer has the VS Code extension installed

- User is working in an active Git repository in VS Code
- User highlights a segment of code, navigates to the extension in the sidebar, and clicks "Analyse Code Snippet"
- System receives the code snippet, maps it to a `CodeArtefact` domain entity, passes it to the `NlpGateway` to get
  analysis and returns an `Analysis` result
- User views the analysis in VS Code with highlighting over problematic code

**Alternative Considerations:**

| Scenario                               | Expected Behaviour                                            |
|----------------------------------------|---------------------------------------------------------------|
| No code highlighted in editor          | Validation error (client) &mdash; no code highlighted         |
| User is not working in a Git directory | Validation error (client) &mdash; not an active Git directory |
| Provided code contains no comments     | Validation error (client) &mdash; no code comments            |

### 4. Developer wants to analyse an _uploaded_ source code file via web client

**Persona:** Developer or security manager reviewing or writing code

**Precondition:** Developer has access to the web client

- User clicks "Analyse Uploaded Code File"
- User is prompted with a file explorer where they can upload a source code file
- The system retrieves the source code from the selected file and:
  - populates a `FileViewer` component
  - maps it to a `CodeArtefact` domain entity, passes it to the `NlpGateway` for analysis and returns an `Analysis` 
    result
- The user views the analysis on the web client with in-line highlighting.

**Alternative Considerations:**

| Scenario                                      | Expected Behaviour                                        |
|-----------------------------------------------|-----------------------------------------------------------|
| User does not upload a valid source code file | Validation error (client) &mdash; Invalid file type       |
| User uploads an empty source code file        | Validation error (client) &mdash; Empty source code file  |
| The source code file contains no comments     | Validation error (client) &mdash; No source code comments |

### 5. Developer wants to analyse a _provided_ source code file via web client

**Persona:** Developer or security manager reviewing or writing code

**Precondition:** User has access to the web client

- User enters a repository URL and clicks "Load Repository"
- The system fetches the repository tree and loads it into a `FileBrowser` component (Each file is a button that
  retrieves the file's content on click)
- The user clicks a file to retrieve it's content, which outputs the content to a `FileViewer` component
- The user clicks "Analyse Active Code File"
- The system takes the entire `FileViewer` content and maps it to `CodeArtefact`, passes it to `NlpGateway` for
  analysis, and returns an `Analysis` result
- The user views the analysis on the web client with in-line highlighting

**Alternative Considerations:**

| Scenario                                                    | Expected Behaviour                                     |
|-------------------------------------------------------------|--------------------------------------------------------|
| No repository URL provided                                  | Validation error (client) &mdash; no URL provided      |
| "Analyse Active Code File" clicked before "Load Repository" | Validation error (client) &mdash; no repository loaded |
| Invalid URL format                                          | Validation error (client) &mdash; invalid URL format   |
| URL does not exist or is unreachable                        | Error (API) &mdash; `400 Bad Request`                  |
| Repository is empty &mdash; contains no code files          | Success &mdash; `204 No Content`                       |
| The active code file has no content                         | Validation error (client) &mdash; no file content      |
| The active code file contains no comments                   | Validation error (client) &mdash; no code comments     |

### 6. Developer wants to analyse a _provided_ source code file via VS Code

**Persona:** Developer or security manager reviewing or writing code

**Precondition:** The user has the VS Code extension installed

- User is working in a Git directory in VS Code, and has a source code file open and in-focus
- The user clicks "Analyse Active Code File'
- The system receives the source code and maps it to `CodeArtefact`, passes it to `NlpGateway` for analysis, and
  returns an `Analysis` result
- The user views the `Analysis` result in VS Code with in-line highlighting over problematic code

**Alternative Considerations:**

| Scenario                                        | Expected Behaviour                                       |
|-------------------------------------------------|----------------------------------------------------------|
| The user is not in a Git directory              | Validation error (client) &mdash; not a Git directory    |
| "Analyse Active Code File" before file opened   | Validation error (client) &mdash; no code file opened    |
| "Analyse Active Code File" while file unfocused | Validation error (client) &mdash; code file not in-focus |
| The code file is empty                          | Validation error (client) &mdash; empty code file        |
| The code file contains no comments              | Validation error (client) &mdash; no code comments       |

### 7. Developer wants to analyse open pull requests via web client

**Persona:** Developer or security manager reviewing open pull requests

**Precondition:** The user has access to the web client

- User enters repository URL and clicks "Load Repository"
- User clicks "Analyse Open Pull Requests"
- The system retrieves open pull requests from the VCS data source, maps them into `PullRequestArtefact`, and passes
  them to `NlpGateway` for analysis, then returns `Analysis` results
- The user views the per-PR analysis in the web client

**Alternative Considerations:**

| Scenario                                                      | Expected Behaviour                                     |
|---------------------------------------------------------------|--------------------------------------------------------|
| No repository URL provided                                    | Validation error (client) &mdash; no URL provided      |
| "Analyse Open Pull Requests" clicked before "Load Repository" | Validation error (client) &mdash; no repository loaded |
| Invalid URL format                                            | Validation error (client) &mdash; invalid URL format   |
| URL does not exist or is unreachable                          | Error (API) &mdash; `400 Bad Request`                  |
| Repository contains no open pull requests                     | Success &mdash; `204 No Content`                       |

### 8. Developer wants to analyse all repository artefacts via web client

**Persona:** Developer or security manager reviewing the entire codebase

**Precondition:** User has access to the web client

- User enters repository URL and clicks "Load Repository"
- User clicks "Analyse All Artefacts"
- The system retrieves all commits, issues, code file contents, and open pull requests and maps them to relevant
  `Artefact` (`CommitArtefact`, `IssueArtefact`, `CodeArtefact`, `PullRequestArtefact`), and passes them to
  `NlpGateway` for analysis, then returns `Analysis` per artefact
- The user views all analyses in the web client

**Alternative Considerations:**

| Scenario                                                 | Expected Behaviour                                                                                            |
|----------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| No repository URL provided                               | Validation error (client) &mdash; no URL provided                                                             |
| "Analyse All Artefacts" clicked before "Load Repository" | Validation error (client) &mdash; no repository loaded                                                        |
| Invalid URL format                                       | Validation error (client) &mdash; invalid URL format                                                          |
| URL does not exist or is unreachable                     | Error (API) &mdash; `400 Bad Request`                                                                         |
| Repository contains no artefacts                         | `204 No Content`                                                                                              | 
| Partial failure &mdash; e.g. fails to fetch commits      | `200 OK` for successful parts, error messages for failed parts; failed parts should not block other processes |

## Questions & Assumptions

### Artefact Ingestion Strategy:

Should artefacts be embedded into a vector store and retrieved via similarity search (RAG) at inference time, or
included directly in the model prompt (Prompt Stuffing)? These are not equivalent approaches: Direct inclusion passes the full artefact
text to the model within its context window, whereas RAG uses embeddings as a *retrieval mechanism* to select the most
relevant chunks for inclusion in the prompt — the model still operates on text either way. Direct inclusion is simpler
and avoids retrieval failures (where a security-relevant chunk is never surfaced to the model), but will not scale to
large repositories due to context window limits. An ephemeral vector store (e.g., ChromaDB, built in-memory
per session) would satisfy the scalability criterion but introduces retrieval risk and additional architectural
complexity. *Recommended approach for MVP: direct prompt inclusion on scoped inputs, with the ingestion layer designed
to be swappable for a RAG pipeline as repository size grows.*

