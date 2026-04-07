import styles from './FileViewer.module.css';

interface FileViewerProps {
    content: string,
    setSelectedCode: (text: string) => void
}

export default function FileViewer({ content, setSelectedCode }: FileViewerProps) {
    // handlers
    const handleTextSelection = () => {
        const selection = window.getSelection();
        const selectedText = selection.toString();
        setSelectedCode(selectedText);
    }

    return (
        <div className={styles["file-viewer"]}>
            <h2>File Viewer</h2>
            <textarea 
                className={styles["file-viewer-textarea"]}
                readOnly
                value={content}
                onMouseUp={handleTextSelection}
            />
        </div>
    );
}