import styles from './FileViewer.module.css';

interface FileViewerProps {
    content: string;
}

export default function FileViewer({ content }: FileViewerProps) {
    return (
        <div className={styles.fileViewer}>
            <textarea
                readOnly
                value={content}
            />
        </div>
    );
}
