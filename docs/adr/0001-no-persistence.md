# ADR-001: No Persistence of Artefacts or Analysis results

**Date:**

**Status:**

## Context

The tool is designed to analyse developer-authored artefacts (commits, issues, pull requests, and code comments) from a
VCS repository for Self-admitted Security Debt (SASD). A decision was required on whether to persist artefacts,
analysis results, or user session data between interactions.

Persisting data would introduce significant complexity: a database, a data access layer, data retention and privacy
concerns, and user account management. The tool's primary purpose is lightweight, on-demand analysis rather than
longitudinal tracking or audit history.

## Decision

No data will be persisted. The tool operates in a fully sessionless manner. Artefacts are fetched from the VCS at
analysis time, passed through the NLP pipeline, and the results are returned to the client within the same session.
Once the session ends, no artefact content or analysis output is retained.

This decision was reflected in the creation of `entities.md` rather than `schema.md`, as the domain model describes
in-memory entities rather than persisted records.

## Consequences

- **No database** is required at any layer of the system.
- **No user accounts or authentication** are needed.
- **Domain entities** are transient value objects; they carry no identity across sessions.
- **Repeated analysis** of the same repository will re-fetch and re-analyse artefacts from scratch each time.
- **Scalability of historical tracking** is out of scope; if required in the future, this ADR should be revisited and a
  persistence layer introduced.
- The system is simpler to deploy and operate with no stateful infrastructure dependencies.
- 