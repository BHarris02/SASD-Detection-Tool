# ADR-0005: Pre-trained LLM

**Date:**

**Status:**

## Context

The tool requires an NLP model capable of classifying developer-authored artefacts (e.g. code comments, commit
messages) for Self-admitted Security Debt (SASD). A decision was required on whether to train a model from scratch,
fine-tune an existing model, or use a pre-trained model directly via a hosted API.

Candidates considered:

- **Train from scratch** &mdash; build and train a custom model on a labelled SASD dataset.
- **Fine-tune a pre-trained model** &mdash; adapt an existing model to the SASD classification task using a labelled
  dataset.
- **Pre-trained LLM via API** &mdash; use an existing large language model (e.g. OpenAI GPT, Google Gemini) via a
  hosted API, prompting it to perform SASD classification without task-specific training.

## Decision

The tool will use a **pre-trained LLM accessed via a hosted API**, prompted to classify artefacts for SASD.

The concrete provider is encapsulated behind the `NlpGateway` interface established in
[ADR-0004](0004-nlp-gateway-abstraction.md), meaning the choice of LLM can be changed without architectural impact.

## Consequences

- **No training data required** &mdash; eliminates the need to curate, label, and maintain a task-specific dataset,
  which is a significant undertaking for a project of this scope.
- **Rapid iteration** &mdash; prompt engineering can be adjusted quickly without retraining or redeploying a model.
- **Provider lock-in is mitigated** &mdash; the `NlpGateway` abstraction means the LLM provider can be swapped by
  replacing the `infra` implementation only.
- **Dependency on external API** &mdash; the tool's analysis capability depends on the availability and pricing of a
  third-party API; this introduces operational risk.
- **Output non-determinism** &mdash; LLM responses are probabilistic; the same input may produce different outputs
  across calls. Prompt design and response parsing must account for this.
- **No fine-tuning** &mdash; the model has no task-specific training on SASD examples, which may limit classification
  accuracy compared to a fine-tuned approach; this is an accepted trade-off at this stage.
