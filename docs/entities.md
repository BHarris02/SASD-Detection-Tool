# Entities

## VCS Entities Class Diagram

```mermaid
classDiagram
    namespace domain.entity.common {
        class Artefact {
            <<abstract>>
        }
    }

    namespace domain.entity.vcs {
        class CommitArtefact {
            - message: String
        }

        class IssueArtefact {
            - title: String
            - body: String
            - labels: ArtefactLabel[]
        }

        class CodeArtefact {
            - source_code: String
        }

        class PullRequestArtefact {
            - title: String
            - body: String
            - labels: ArtefactLabel[]
        }
    }

    namespace domain.valueobject.vcs {
        class ArtefactLabel {
            <<value>>
            - name: String
            - description: String
        }
    }

CommitArtefact --|> Artefact
IssueArtefact --|> Artefact
CodeArtefact --|> Artefact
PullRequestArtefact --|> Artefact

IssueArtefact *-- ArtefactLabel
PullRequestArtefact *-- ArtefactLabel

```

## NLP Entities Class Diagram

```mermaid
classDiagram
    class SasdAnalysisSeverity {
        <<enum>>
        LOW,
        MEDIUM,
        HIGH,
        CRITICAL
    }
    class SasdAnalysis {
        explanation: String
        severity: SasdAnalysisSeverity
    }
    class CweMapping {
        id: String
        title: String
        explanation: String
    }
    class Artefact {
        <<abstract>>
    }
    class NlpAnalysis {
        artefact: Artefact
        isSasd: boolean
        sasdAnalysis: SasdAnalysis
        cweMapping: CweMapping[]
    }

NlpAnalysis o-- SasdAnalysis
NlpAnalysis o-- CweMapping
NlpAnalysis o-- Artefact

SasdAnalysis *-- SasdAnalysisSeverity
```
