import axios from "axios";
import React from "react";
import { analyzeCommits, analyzeIssues, analyzeFile, analyzeMethod, analyzeRepo } from "../utils/api";

const BackendActions = ({ repoUrl, setFileViewerContent, selectedCode, selectedFilePath, setAnalysisResult, setLoading, handleFullScanResults }) => {

    const handleScanCommits = async () => {
        if (!repoUrl) {
            alert("Enter Repository URL");
            return;
        }

        setLoading(true);

        try {
            const resp = await analyzeCommits(repoUrl);
            const analysis = resp.data.commit_analysis;
            const formattedAnalysis = analysis.map((commit, index) => 
                `\nCommit ${index + 1}: \nMessage: ${commit.message}\nSelf-Admitted Security Debt Detected: ${commit.sasd_detected}\nDetails: ${commit.details}\n`
            );
            setFileViewerContent(formattedAnalysis);
        }
        catch (error) {
            console.error("Failed to analyze commits:", error.response || error.message);
            alert("Failed to analyze commits. Check the console for details.");
        }
        finally {
            setLoading(false);
        }
    };

    const handleScanIssues = async () => {
        if (!repoUrl) {
            alert("Enter Repository URL");
            return;
        }

        setLoading(true);

        try {
            const resp = await analyzeIssues(repoUrl);
            const analysis = resp.data.issue_analysis;
            const formattedAnalysis = analysis.map((issue, index) =>
                `\nIssue ${index + 1}: \nMessage: ${issue.message}\nSelf-Admitted Security Debt Detected: ${issue.sasd_detected}\nDetails: ${issue.details}\n`
            );
            setFileViewerContent(formattedAnalysis);
        } 
        catch (error) {
            console.error("Failed to analyze issues:", error.response || error.message);
            alert("Failed to analyze issues. Check the console for details.");
        } 
        finally {
            setLoading(false);
        }
    };

    const handleScanMethod = async () => {
        if (!selectedCode || selectedCode.trim() === "") {
            alert("Please select a method to analyze.");
            return;
        }

        setLoading(true);

        try {
            const resp = await analyzeMethod(selectedCode);
            setAnalysisResult("Method Analysis", resp.data);
        } 
        catch (error) {
            console.error("Failed to analyze method:", error.response || error.message);
            alert("Failed to analyze the selected code. Check the console for details.");
        } 
        finally {
            setLoading(false);
        }
    };

    const handleFullFileScan = async () => {
        if (!selectedFilePath) {
            alert("Please select a file to analyze.");
            return;
        }

        setLoading(true);

        try {
            const resp = await analyzeFile(repoUrl, selectedFilePath);
            setAnalysisResult("Full file Analysis", resp.data);
        } 
        catch (error) {
            console.error("Failed to analyze file:", error.response || error.message);
            setAnalysisResult("Error", { error: "Failed to analyze the selected file." });
        } 
        finally {
            setLoading(false);
        }
    };

    const handleFullRepoScan = async () => {
        if (!repoUrl) {
            alert("Enter Repository URL");
            return;
        }

        setLoading(true);

        try {
            const resp = await analyzeRepo(repoUrl);
            handleFullScanResults(resp.data);
        } 
        catch (error) {
            console.error("Failed to perform full repository scan:", error.response || error.message);
            alert("Failed to perform full repository scan. Check the console for details.");
        } 
        finally {
            setLoading(false);
        }
    };

    return (
        <div className="backend-actions">
          <button onClick={handleScanCommits}>Scan Commit Messaegs</button>
          <button onClick={handleScanIssues}>Scan Issue Tracking Entries</button>
          <button onClick={handleScanMethod}>Scan Currently Selected Method</button>
          <button onClick={handleFullFileScan}>Scan Current File Comments</button>
          <button onClick={handleFullRepoScan}>Full Repository Scan</button>
        </div>
    );
};

export default BackendActions;