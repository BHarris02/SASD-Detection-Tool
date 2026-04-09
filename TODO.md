# TODO

> This file is used to generate GitHub Issues. Each ticket should be created using the Task issue template.

---

## Ticket 1: Complete backend refactor & remove legacy code

**Tasks:**
- Write REST endpoints for analysis and VCS actions
- Create Pydantic schemas for incoming requests and outgoing responses
- Delete legacy `backend/` folder from repo root

**Dependencies:** None

---

## Ticket 2: Complete frontend refactor & remove legacy code

**Tasks:**
- Complete `Workspace` component with `AnalysisActions` and `FileViewer` child components
- Create `useWorkspace` hook
- Rethink and rebuild `Tab` and `Modal` components for analysis results
- Remove redundant refactor reference components
- Delete legacy `frontend/` folder from repo root

**Dependencies:** None

---

## Ticket 3: Backend tests

**Tasks:**
- Write unit tests across all modules (data, di, domain, api)
- Write integration tests
- Write e2e tests by hitting live endpoints
- Framework: pytest
- Do not reference legacy tests

**Dependencies:** Ticket 1

---

## Ticket 4: Backend README

**Tasks:**
- Write a general README for the backend app
- Should cover: project overview, setup instructions, how to run, environment variables

**Dependencies:** Ticket 1

---

## Ticket 5: Per-module READMEs with dependency graphs

**Tasks:**
- Create a README for each module: data, di, domain, api
- Each README should include: title, purpose, module structure placeholder, Mermaid dependency graph
- Module Structure section should be left empty for manual completion
- READMEs live inside their respective module folders, not the backend root

**Dependencies:** Ticket 1

---

## Ticket 6: Infrastructure

**Tasks:**
- Write a Dockerfile for the backend
- Write a Dockerfile for the frontend
- Create per-app `.env.example` files for backend and frontend
- Remove root `.env.example`
- Create `infra/` folder at repo root
- Write Docker Compose file inside `infra/`
- Write a README for `infra/`

**Dependencies:** Ticket 1, Ticket 2

---

## Ticket 7: Frontend tests

**Tasks:**
- Write unit tests for components and hooks using Jest
- Write integration tests for sections
- No e2e tests
- All tests are new — no legacy reference material exists

**Dependencies:** Ticket 2

---

## Ticket 8: Frontend README

**Tasks:**
- Write a general README for the frontend app
- Should cover: project overview, setup instructions, how to run, environment variables

**Dependencies:** Ticket 2