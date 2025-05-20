import React from "react";

const FileViewer = ({ content, setSelectedCode }) => {

    const handleTextSelection = () => {
        const selection = window.getSelection();
        const selctedText = selection.toString();
        setSelectedCode(selctedText);
    };

    return (
    <div className="file-viewer">
        <h2>File Viewer</h2>
            <textarea
                readOnly
                value={content}
                className="file-viewer-textarea"
                onMouseUp={handleTextSelection}
            />
    </div>
    );
};

export default FileViewer;