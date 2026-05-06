# ADR-002: Clean Architecture and Domain-driven Design

**Date:**

**Status:**

## Context

The backend requires a structural and design approach that supports long-term maintainability, testability, and the
ability to swap out external dependencies (such as the NLP provider or VCS integration) without affecting core business
logic.

Two complementary approaches were evaluated:

- **Clean Architecture** &mdash; a layered architectural pattern that enforces a strict dependency rule: outer layers
  depend on inner layers, never the reverse.
- **Domain-Driven Design (DDD)** &mdash; a design philosophy centred on modelling the core domain explicitly, using
  entities, value objects, and domain services to reflect the ubiquitous language of the problem space.

## Decision

The backend will be structured using **Clean Architecture** with **DDD** applied within the domain layer.

The layers are defined as follows:

| Layer          | Responsibility                                                                                                      |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| **API**        | HTTP controllers, request/response DTOs, global exception handling.                                                 |
| **App**        | Spring Boot application entrypoint, DI configuration, and wiring of all other layers. Depends on all other layers.  |
| **Domain**     | Core entities, value objects, domain logic, and interfaces that outer layers must implement (dependency inversion). |
| **Infra**      | Concrete implementations of domain-defined interfaces, including VCS and NLP gateway adapters.                      |
| **Interactor** | Application business logic in the form of use cases. Depends only on the domain layer.                              |

DDD concepts applied include:

- **Entities** and **Value Objects** as defined in [`entities.md`](../entities.md)
- **Ubiquitous language** aligned with the glossary in [`glossary.md`](../glossary.md)
- **Domain services** for logic that does not naturally belong to a single entity (e.g. SASD analysis orchestration)

## Consequences

- **Framework isolation** &mdash; Spring Boot and other infrastructure concerns are confined to the `infra` and `api`
  layers; the domain layer has no knowledge of them.
- **Dependency inversion** &mdash; the `domain` layer defines the interfaces (e.g. `NlpGateway`, `VcsGateway`) that
  `infra` implements, ensuring the domain is never coupled to external providers.
- **Testability** &mdash; the `domain` and `interactor` layers can be unit tested without standing up any Spring
  context or external service.
- **NLP and VCS gateway abstractions** are defined as interfaces in the `domain` layer and implemented in the `infra`
  layer, supporting provider substitution.
- **Increased initial scaffolding** &mdash; Clean Architecture requires more upfront structure than a simple layered
  MVC approach.
- **Consistency with entities.md** &mdash; domain entities are defined code-first in the `domain` layer, consistent
  with the non-persistent, in-memory model established in [ADR-001](0001-no-persistence.md).
- 