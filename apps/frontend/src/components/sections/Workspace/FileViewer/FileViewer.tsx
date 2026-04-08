import styles from './FileViewer.module.css';

export default function FileViewer() {
    return (
        <div className={styles.fileViewer}>
            <h2>File Viewer</h2>
            <textarea
                readOnly
            />
        </div>
    );
}
