# ADR-0004: NLP Gateway Abstraction

**Date:**

**Status:**

## Context

The core function of the tool is to analyse developer-authored artefacts for Self-admitted Security Debt (SASD). This
analysis is performed by an NLP model. A decision was required on how to integrate NLP capabilities into the backend
without coupling the domain or application logic to a specific provider or implementation.

## Decision

NLP capabilities will be accessed exclusively through a **gateway interface** (`NlpGateway`) defined in the `domain`
layer. The `infra` layer provides the concrete implementation, which may delegate to a local model, a remote API, or
any other provider.

The `interactor` layer calls only the `NlpGateway` interface; it has no knowledge of the underlying provider.

## Consequences

- **Provider independence** &mdash; the NLP provider can be swapped (e.g. from a local model to a remote API) by
  replacing the `infra` implementation without touching the `domain` or `interactor` layers.
- **Testability** &mdash; the `NlpGateway` interface can be mocked in unit tests for use cases, removing any dependency
  on a live NLP service during testing.
- **Consistency with ADR-002** &mdash; this decision directly realises the dependency inversion principle described in
  [ADR-002](0002-architecture.md); `NlpGateway` is one of the domain-defined interfaces that `infra` implements.
- **Single integration point** &mdash; all NLP calls are routed through the gateway, making it straightforward to add
  cross-cutting concerns such as logging, error handling, or rate limiting at the infrastructure boundary.
- **Future flexibility** &mdash; if multiple NLP providers or models are required (e.g. for comparison or fallback),
  the gateway interface can be extended or decorated without architectural change.
