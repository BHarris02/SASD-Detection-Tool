# Entities

## VCS Entities Class Diagram

```mermaid
classDiagram
    class Artefact {
        <<abstract>>
    }
    class CommitArtefact {
        title: String
        body: String
    }
    class IssueArtefact {
        title: String
        description: String
        labels: ArtefactLabel[]
    }
    class ArtefactLabel {
        name: String
        description: String
    }
    class CodeArtefact {
        content: String
    }
    class PullRequestArtefact {
        title: String
        description: String
        labels: ArtefactLabel[]
    }
    
CommitArtefact --|> Artefact

IssueArtefact --|> Artefact
IssueArtefact *-- ArtefactLabel

CodeArtefact --|> Artefact

PullRequestArtefact --|> Artefact
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
