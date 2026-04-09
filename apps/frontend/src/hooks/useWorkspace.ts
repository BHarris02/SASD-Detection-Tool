import { useAppContext } from "@/context/AppContext"
import { analyzeCodeComments, analyzeCommits, analyzeFileComments, analyzeIssues, analyzeRepository } from "@/services/analysisApi";
import { useState } from "react";

export default function useWorkspace() {
    // state
    const [loading, setLoading] = useState<boolean>(false);
    const {
        // FileViewer
        fileViewerContent,
        // AnalysisActions
        repoUrl,
        selectedFilePath
    } = useAppContext();
    // FileViewer
    const [selectedCode, setSelectedCode] = useState<string>("");

    // handlers
    const handleScanCommits = async () => {
        if (!validateRepoUrl()) return;
        setLoading(true);
        try {
            const resp = await analyzeCommits(repoUrl);
            const analysis = resp.data.commit_analysis;
            const formattedAnalysis = analysis.map((commit, index) => 
                `
                \nCommit ${index+1}:
                \nMessage: ${commit.message}
                \nSASD Detected: ${commit.sasd_detected}
                \nDetails: ${commit.details}
                `
            );
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze commit messages. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanIssues = async () => {
        if (!validateRepoUrl()) return;
        setLoading(true);
        try {
            const resp = await analyzeIssues(repoUrl);
            const analysis = resp.data.issue_analysis;
            const formattedAnalysis = analysis.map((issue, index) =>
                `
                \nIssue ${index+1}:
                \nMessage: ${issue.message}
                \nSASD Detected: ${issue.sasd_detected}
                \nDetails: ${issue.details}
                `
            );
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze issues. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanCodeComments = async () => {
        if (!selectedCode.trim()) {
            alert("Please select code to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeCodeComments(selectedCode);
            const analysis = resp.data;
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze code comments. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanFileComments = async () => {
        if (!validateRepoUrl()) return;
        if (!selectedFilePath || selectedCode.trim() === "") {
            alert("Please select a file to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeFileComments(repoUrl, selectedFilePath);
            const analysis = resp.data;
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze file content. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanRepository = async () => {
        if (!validateRepoUrl()) return;
        setLoading(true);
        try {
            const resp = await analyzeRepository(repoUrl);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze repository. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    // utils
    const validateRepoUrl = () => {
        if (!repoUrl.trim()) {
            alert("Please enter a repository URL.");
            return false;
        }
        return true;
    }

    return {
        loading,
        // FileViewer
        fileViewerContent,
        setSelectedCode,
        // AnalysisActions
        handleScanCommits,
        handleScanIssues,
        handleScanCodeComments,
        handleScanFileComments,
        handleScanRepository
    }
}