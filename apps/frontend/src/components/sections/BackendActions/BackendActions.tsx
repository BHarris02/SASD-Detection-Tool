import styles from './BackendActions.module.css';

export default function BackendActions() {
    return (
        <div className={styles["backend-actions"]}>
            <button>Scan Commits</button>
            <button>Scan Issues</button>
            <button>Scan Selected Code</button>
            <button>Scan Current File</button>
            <button>Scan Entire Repository</button>
        </div>
    );
}