# ADR-0007: CWE as Classification Framework

**Date:**

**Status:**

## Context

The tool classifies artefacts for Self-admitted Security Debt (SASD). A decision was required on what taxonomy or
framework to use when categorising the type of security debt identified in an artefact.

Candidates considered:

- **No classification** &mdash; report only whether SASD is present, without categorising the type.
- **Custom taxonomy** &mdash; define a project-specific set of security debt categories.
- **CWE (Common Weakness Enumeration)** &mdash; use the industry-standard taxonomy maintained by MITRE for classifying
  software weaknesses.
- **OWASP Top 10** &mdash; use the OWASP Top 10 as a classification framework.

## Decision

The tool will use the **Common Weakness Enumeration (CWE)** as the classification framework for identified SASD.
Where an artefact is classified as containing SASD, the analysis result will include one or more associated CWE
identifiers.

The CWE identifier(s) are carried by the `AnalysisResult` entity defined in [`entities.md`](../entities.md).

## Consequences

- **Industry standard** &mdash; CWE is widely recognised and understood, making results meaningful to security
  practitioners without requiring familiarity with a custom taxonomy.
- **Interoperability** &mdash; CWE identifiers can be cross-referenced with other security tooling (e.g. SAST tools,
  vulnerability databases) that use the same taxonomy.
- **LLM suitability** &mdash; pre-trained LLMs have broad knowledge of CWE entries, making CWE-based classification a
  natural fit for prompt-driven analysis established in [ADR-0005](0005-pre-trained-llm.md).
- **Granularity** &mdash; CWE provides a large, hierarchical catalogue; prompt design must constrain the model to
  return relevant, specific entries rather than overly broad or hallucinated identifiers.
- **OWASP not selected** &mdash; the OWASP Top 10 is higher-level and better suited to risk prioritisation than precise
  weakness classification; CWE is more appropriate for artefact-level analysis.
- **No custom taxonomy** &mdash; avoids the overhead of defining and maintaining a bespoke classification scheme, and
  ensures results are portable beyond this tool.
