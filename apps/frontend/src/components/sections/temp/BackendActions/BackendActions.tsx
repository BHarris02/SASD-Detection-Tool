import styles from './BackendActions.module.css';

interface BackendActionsProps {
    onScanCommits: () => void;
    onScanIssues: () => void;
    onScanCodeComments: () => void;
    onScanFileComments: () => void;
    onScanRepository: () => void;
}

export default function BackendActions({ 
    onScanCommits, 
    onScanIssues, 
    onScanCodeComments, 
    onScanFileComments, 
    onScanRepository
}: BackendActionsProps) {
    return (
        <div className={styles["backend-actions"]}>
            <button onClick={onScanCommits}>Scan Commits</button>
            <button onClick={onScanIssues}>Scan Issues</button>
            <button onClick={onScanCodeComments}>Scan Selected Code</button>
            <button onClick={onScanFileComments}>Scan Current File</button>
            <button onClick={onScanRepository}>Scan Entire Repository</button>
        </div>
    );
}