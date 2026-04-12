import styles from './FileViewer.module.css';

interface FileViewerProps {
    fileContent: string;
    onSelectionChange: (selectedCode: string) => void;
}

export default function FileViewer({ fileContent, onSelectionChange }: FileViewerProps) {
    // handlers
    function handleTextSelection() {
        const selectedText = window.getSelection().toString() ?? "";
        onSelectionChange(selectedText);
    }

    return (
        <div className={styles.fileViewer}>
            <h2>File Viewer</h2>
            <textarea
                readOnly
                value={fileContent}
                onMouseUp={handleTextSelection}
            />
        </div>
    );
}
