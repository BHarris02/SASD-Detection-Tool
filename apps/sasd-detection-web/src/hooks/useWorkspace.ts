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
        selectedFilePath,
        // errors
        setError
    } = useAppContext();
    // FileViewer
    const [selectedCode, setSelectedCode] = useState<string>("");
    // AnalysisTabs
    const [analysisResults, setAnalysisResults] = useState<string | null>(null);

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
            setAnalysisResults(formattedAnalysis);
        }
        catch (error) {
            console.error(error);
            setError("Failed to analyze commit messages. Please try again later.");
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
            setAnalysisResults(formattedAnalysis);
        }
        catch (error) {
            console.error(error);
            setError("Failed to analyze issues. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanCodeComments = async () => {
        if (!selectedCode.trim()) {
            setError("Please select code to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeCodeComments(selectedCode);
            const analysis = resp.data;
            setAnalysisResults(analysis);
        }
        catch (error) {
            console.error(error);
            setError("Failed to analyze code comments. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanFileComments = async () => {
        if (!validateRepoUrl()) return;
        if (!selectedFilePath || selectedCode.trim() === "") {
            setError("Please select a file to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeFileComments(repoUrl, selectedFilePath);
            const analysis = resp.data;
            setAnalysisResults(analysis);
        }
        catch (error) {
            console.error(error);
            setError("Failed to analyze file content. Please try again later.");
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
            setAnalysisResults(resp.data);
        }
        catch (error) {
            console.error(error);
            setError("Failed to analyze repository. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    // utils
    const validateRepoUrl = () => {
        if (!repoUrl.trim()) {
            setError("Please enter a repository URL.");
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
        handleScanRepository,
        // AnalysisTabs
        analysisResults
    }
}