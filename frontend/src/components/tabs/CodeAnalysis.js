import React, { useState } from "react";

const CodeAnalysis = ({ data }) => {
  const [selectedFile, setSelectedFile] = useState(null);

  return (
    <div className="code-file-analysis">
      <h3>Code File Analysis</h3>
      <div className="file-list">
        {data.map((file, index) => (
          <button
            key={index}
            onClick={() => setSelectedFile(file)}
            className="file-button"
          >
            {file.file_path}
          </button>
        ))}
      </div>
      {selectedFile && (
        <div className="file-details">
          <h4>File: {selectedFile.file_path}</h4>
            {selectedFile.method_signature && (
                <p>
                <strong>Method Signature:</strong> {selectedFile.method_signature}
                </p>
            )}
          <p>
            <strong>SASD Detected:</strong>{" "}
            {selectedFile.sasd_detected ? "Yes" : "No"}
          </p>
          <p>
            <strong>Details:</strong> {selectedFile.details}
          </p>
          <p>
            <strong>CWE Mapping:</strong>{" "}
            {selectedFile.cwe_mapping?.cwe_mapping || "N/A"}
          </p>
        </div>
      )}
    </div>
  );
};

export default CodeAnalysis;
