import styles from './FileViewer.module.css';

interface FileViewerProps {
    content: string;
    onSelectionChange: (selectedText: string) => void;
}

export default function FileViewer({ content, onSelectionChange }: FileViewerProps) {
    // handlers
    const handleTextSelection = () => {
        const selection = window.getSelection();
        const selectedText = selection.toString();
        onSelectionChange(selectedText);
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
