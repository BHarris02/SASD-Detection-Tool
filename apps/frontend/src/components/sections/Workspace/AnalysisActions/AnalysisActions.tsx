import styles from './AnalysisActions.module.css';

export default function AnalysisActions() {
    return (
        <div className={styles.analysisActionsButtons}>
            <button>Scan Commits</button>
            <button>Scan Issues</button>
            <button>Scan Selected Code</button>
            <button>Scan Current File</button>
            <button>Scan Repository</button>
        </div>
    );
}
