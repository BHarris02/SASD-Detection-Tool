import styles from './AnalysisActions.module.css';

interface AnalysisActionsProps {
    onScanCommits: () => void;
    onScanIssues: () => void;
    onScanCodeComments: () => void;
    onScanFileComments: () => void;
    onScanRepository: () => void
}

export default function AnalysisActions({ 
    onScanCommits,
    onScanIssues,
    onScanCodeComments,
    onScanFileComments,
    onScanRepository 
}: AnalysisActionsProps) {
    return (
        <div className={styles.analysisActionsButtons}>
            <button onClick={onScanCommits}>Scan Commits</button>
            <button onClick={onScanIssues}>Scan Issues</button>
            <button onClick={onScanCodeComments}>Scan Selected Code</button>
            <button onClick={onScanFileComments}>Scan Current File</button>
            <button onClick={onScanRepository}>Scan Repository</button>
        </div>
    );
}
