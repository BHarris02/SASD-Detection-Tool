# ADR-0006: Artefact as the Unit of Analysis

**Date:**

**Status:**

## Context

The tool analyses developer-authored content for Self-admitted Security Debt (SASD). A decision was required on what
constitutes the atomic unit of input to the NLP analysis pipeline.

Candidates considered:

- **Repository** — analyse an entire repository as a single input.
- **File** — analyse each source file as a discrete unit.
- **Artefact** — analyse each discrete developer-authored item (e.g. a single commit message, a single code comment)
  as an independent unit.

## Decision

The **artefact** is the atomic unit of analysis. Each artefact represents a single, discrete developer-authored item
submitted to the NLP pipeline independently.

Artefact types include commit messages and inline code comments, as defined in [`entities.md`](../entities.md).

## Consequences

- **Granular results** &mdash; SASD classifications are associated with individual artefacts, enabling precise
  reporting.
- **NLP input size** &mdash; individual artefacts are typically short, keeping prompt size manageable and reducing LLM
  token cost per analysis call.
- **Parallelisable** &mdash; artefacts can be analysed independently, allowing concurrent NLP calls if required.
- **Consistency with the domain model** — `Artefact` is a first-class entity in the domain layer, as established
  in [`entities.md`](../entities.md).
- **Volume** &mdash; a repository may contain a large number of artefacts; throughput and rate limiting must be
  considered at the infrastructure layer.
