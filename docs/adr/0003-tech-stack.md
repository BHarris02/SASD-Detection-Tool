# ADR-0003: Tech Stack

**Date:**

**Status:**

## Context

The project requires a backend capable of orchestrating NLP analysis and VCS integration, and a frontend for presenting
analysis results to the user. Decisions were required on the language, framework, and ecosystem for both.

## Decision

The backend will be written in **Kotlin** with **Spring Boot**, and the frontend will be written in **TypeScript** with
**React**.

| Layer    | Language   | Framework   | Rationale                                                                                                          |
|----------|------------|-------------|--------------------------------------------------------------------------------------------------------------------|
| Backend  | Kotlin     | Spring Boot | Concise JVM language with null safety, data classes, and full Spring ecosystem support.                            |
| Frontend | TypeScript | React       | Type safety over plain JavaScript; React's component model suits a results-driven, analysis display UI.            |

**Kotlin over Java** &mdash; Kotlin reduces boilerplate significantly (e.g. data classes replace POJOs), has built-in
null safety, and is fully interoperable with the Java ecosystem.

**Spring Boot over alternatives** &mdash; Spring Boot provides a mature, production-ready ecosystem for building REST
APIs, with strong support for dependency injection, which aligns with the Clean Architecture dependency inversion
principle established in [ADR-002](0002-architecture.md).

**TypeScript over JavaScript** &mdash; TypeScript's static typing reduces runtime errors and improves IDE support,
which is particularly valuable when modelling structured analysis result types returned from the backend.

**React over alternatives** &mdash; React's component model is well-suited to rendering structured, hierarchical
analysis results. Its ecosystem and community maturity reduce risk.

## Consequences

- **Kotlin data classes** map naturally to the domain value objects and entities defined in
  [`entities.md`](../entities.md).
- **Spring Boot DI** supports the wiring of Clean Architecture layers as established in [ADR-002](0002-architecture.md).
- **TypeScript interfaces** can be generated or manually kept in sync with backend response DTOs; a future ADR may
  address API contract sharing (e.g. OpenAPI).
- **Frontend and backend are developed as separate projects**, communicating over HTTP &mdash; see
  [ADR-0004](0004-nlp-gateway-abstraction.md).
- The team must be comfortable with both JVM (Kotlin) and JavaScript ecosystem (Node, npm/yarn) tooling.