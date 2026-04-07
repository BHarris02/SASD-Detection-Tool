import styles from './FileViewer.module.css';

export default function FileViewer() {
    return (
        <div className={styles["file-viewer"]}>
            <h2>File Viewer</h2>
            <textarea 
                className={styles["file-viewer-textarea"]}
                readOnly
            />
        </div>
    );
}