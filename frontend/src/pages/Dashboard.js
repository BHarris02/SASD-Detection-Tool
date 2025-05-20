import React, { useState } from "react";
import axios from "axios";
import RepoInput from "../components/RepoInput";
import RepoFileTree from "../components/RepoFileTree";
import FileViewer from "../components/FileViewer";
import BackendActions from "../components/BackendActions";
import LoadingSpinner from "../components/LoadingSpinner";
import Modal from "../components/Modal";
import Tabs from "../components/Tabs";
import CommitAnalysis from "../components/tabs/CommitAnalysis";
import IssueAnalysis from "../components/tabs/IssueAnalysis";
import CodeAnalysis from "../components/tabs/CodeAnalysis";

const Dashboard = () => {
  const [repoUrl, setRepoUrl] = useState("");
  const [fileTree, setFileTree] = useState(null);
  const [fileViewerContent, setFileViewerContent] = useState("// Select file to view its content.");
  const [loading, setLoading] = useState(false);
  const [selectedCode, setSelectedCode] = useState("");
  const [selectedFilePath, setSelectedFilePath] = useState(null);
  const [modalData, setModalData] = useState(null);
  const [showModal, setShowModal] = useState(false);
  const [showTabs, setShowTabs] = useState(false);
  const [scanResults, setScanResults] = useState(null);

  const fetchRepoStructure = (url) => {
    if (!url.trim()) {
      alert("Please enter a Repository URL");
      return;
    };

    setLoading(true);

    axios
    .get("http://localhost:5000/api/repo/structure", { params: { repo_url: url }, })
    .then((resp) => {
      setFileTree(resp.data.structure);
      setLoading(false);
    })
    .catch((error) => {
      console.error(`Failed to fetch repository structure: ${error}`);
      alert("Failed to load Repository Structure. Please check the URL");
      setLoading(false);
    });
  };

  const handleAnalysisResult = (title, data) => {
    setLoading(false);
    setModalData({ title, data });
    setShowModal(true);
  };

  const handleFullScanResults = (results) => {
    setScanResults(results);
    setShowTabs(true);
  };

  const handleFileContent = (content) => {
    setFileViewerContent(content);
    setShowTabs(false);
  };

  return (
    <div className="dashboard">
      <LoadingSpinner loading={loading} />
      <h1>Self-Admitted Security Debt Detection Tool: Web</h1>

      <RepoInput
        repoUrl={repoUrl}
        setRepoUrl={setRepoUrl}
        fetchRepoStructure={fetchRepoStructure}
       />

      <RepoFileTree 
        fileTree={fileTree}
        repoUrl={repoUrl}
        setFileViewerContent={setFileViewerContent}
        setLoading={setLoading}
        onFileSelect={setSelectedFilePath}
        showTabs={showTabs}
        setShowTabs={setShowTabs}
      />

      <div className="content-viewier">
        {showTabs && scanResults ? (
          <Tabs
          tabs={[
            {
              label: "Commit Message Analysis",
              content: <CommitAnalysis data={scanResults.commit_analysis} />
            },
            {
              label: "Issue Tracker Analysis",
              content: <IssueAnalysis data={scanResults.issue_analysis} />
            },
            {
              label: "Code Analysis",
              content: <CodeAnalysis data={scanResults.code_analysis} />

            },
          ]}
          />
        ) : (
          <FileViewer 
            content={fileViewerContent}
            setSelectedCode={setSelectedCode}
          />
        )}
      </div>

      <BackendActions
        repoUrl={repoUrl}
        setFileViewerContent={setFileViewerContent} 
        selectedCode={selectedCode}
        selectedFilePath={selectedFilePath}
        setAnalysisResult={handleAnalysisResult}
        setLoading={setLoading}
        handleFullScanResults={handleFullScanResults}
      />
      <Modal
        show={showModal}
        onClose={() => setShowModal(false)}
        title={modalData?.title || "Analysis Results"}
      >
      {modalData?.data?.code_analysis ? (
          Array.isArray(modalData.data.code_analysis) ? (
            <div style={{ textAlign: "left", whiteSpace: "pre-wrap" }}>
              {modalData.data.code_analysis.map((method, index) => (
                <div key={index}>
                  <p><strong>Method {index + 1}:</strong></p>
                  <p><strong>SASD Detected:</strong> {method.sasd_detected ? "Yes" : "No"}</p>
                  {method.method_signature && (
                    <p><strong>Method Signature:</strong> {method.method_signature}</p>
                  )}
                  <p><strong>Details:</strong> {method.details.details}</p>
                  {method.cwe_mapping && (
                    <>
                      <p><strong>CWE Mapping:</strong> {method.cwe_mapping.cwe_mapping}</p>
                      <p><strong>Mapping Details:</strong> {method.cwe_mapping.details}</p>
                    </>
                  )}
                  <hr />
                </div>
              ))}
            </div>
          ) : (
            <p>Unexpected response format.</p>
          )
        ) : modalData?.data?.sasd_detected !== undefined ? (
          <div style={{ textAlign: "left", whiteSpace: "pre-wrap" }}>
            <p><strong>SASD Detected:</strong> {modalData.data.sasd_detected ? "Yes" : "No"}</p>
            {modalData.data.method_signature && (
              <p><strong>Method Signature:</strong> {modalData.data.method_signature}</p>
            )}
            <p><strong>Details:</strong> {modalData.data.details.details}</p>
            {modalData.data.details.cwe_mapping && (
              <>
                <p><strong>CWE Mapping:</strong> {modalData.data.details.cwe_mapping}</p>
                <p><strong>Mapping Details:</strong> {modalData.data.details.details}</p>
              </>
            )}
          </div>
        ) : (
          <p>No Data available.</p>
        )}
      </Modal>
    </div>
  );
};

export default Dashboard;