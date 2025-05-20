import React, { useState } from "react";
import { getFileIcon, folderIcon } from "../utils/fileIcons";
import axios from "axios";

const RepoFileTree = ({ fileTree, repoUrl, setFileViewerContent, setLoading, onFileSelect, showTabs, setShowTabs }) => {
  const [selectedFilePath, setSelectedFilePath] = useState(null);

    const handleFileClick = (file) => {
      setLoading(true);
      setSelectedFilePath(file.path);
      if (onFileSelect) onFileSelect(file.path);

      axios
      .post("http://localhost:5000/api/file/content", { repo: repoUrl, file_path: file.path })
      .then((resp) => {
        if (showTabs) setShowTabs(false);
        setFileViewerContent(resp.data.file_content);
      })
      .catch((error) => {
        console.error("Failed to fetch file content:", error.response || error.message);
        setFileViewerContent("Failed to load file content. Check the console for details.");
      })
      .finally(() => {
        setLoading(false);
      });
    };

    const renderTree = (node) => {
      if (!node) return null;

      if (node.type === "folder") {
        return(
          <li key={node.name}>
          <div className="tree-item">
            {folderIcon} {node.name}
          </div>
          <ul>
            {node.children.map((child) => renderTree(child))}
          </ul>
        </li>
        );
      }
      else {
        return (
          <li
            key={node.name}
            className={`tree-item ${selectedFilePath === node.path ? "selected" : ""}`}
            onClick={() => handleFileClick(node)}
          >
            {getFileIcon(node.name)} {node.name}
          </li>
        );
      }
    };

    return (
      <div className="repo-file-tree">
        {fileTree ? (
          <ul>{fileTree.map((node) => renderTree(node))}</ul>
        ) : (
          <p>No repository loaded. Click "Load Repository" to fetch the file tree.</p>
        )}
      </div>
    );

};

export default RepoFileTree;