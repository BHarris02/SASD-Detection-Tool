import { useState } from "react";
import type { FileTreeNode, ModalData } from '@/types/vcs';
import type { ScanResults } from "@/types/analysis";
import { fetchFileContent, fetchRepoStructure } from "@/services/vcsApi";
import { analyzeCodeComments, analyzeCommits, analyzeFileComments, analyzeIssues, analyzeRepository } from "@/services/analysisApi";

export function useDashboard() {
    // state
    const [repoUrl, setRepoUrl] = useState<string>("");
    const [fileTree, setFileTree] = useState<FileTreeNode[] | null>(null);
    const [fileViewerContent, setFileViewerContent] = useState<string>("# Select a file to view its content.");
    const [loading, setLoading] = useState<boolean>(false);
    const [selectedCode, setSelectedCode] = useState<string>("");
    const [selectedFilePath, setSelectedFilePath] = useState<string>("");
    const [modalData, setModalData] = useState<ModalData | null>(null);
    const [showModal, setShowModal] = useState<boolean>(false);
    const [showTabs, setShowTabs] = useState<boolean>(false);
    const [scanResults, setScanResults] = useState<ScanResults | null>(null);

    // handlers
    const handleFetchRepoStructure = async(repoUrl: string) => {
        if (!repoUrl.trim()) {
            alert("Please enter a repository URL.");
            return;
        }
        setLoading(true);
        try {
            const resp = await fetchRepoStructure(repoUrl);
            setFileTree(resp.data.structure);
        }
        catch (error) {
            console.error(error);
            alert("Failed to load repository structure. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleFileClick = async(file: FileTreeNode) => {
        setLoading(true);
        setSelectedFilePath(file.path);
        setShowTabs(false);
        try {
            const resp = await fetchFileContent(repoUrl, file.path);
            setFileViewerContent(resp.data.file_content);
        }
        catch (error) {
            console.error(error);
            setFileViewerContent("Failed to fetch file content. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanCommits = async(repoUrl: string) => {
        if (!repoUrl) {
            alert("Please enter a repository URL.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeCommits(repoUrl);
            const commitsAnalysis = resp.data.commit_analysis;
            const formattedAnalysis = commitsAnalysis.map((commit, index) =>
                `\nCommit ${index+1}: 
                \nMessage: ${commit.message} 
                \nSASD Detected: ${commit.sasd_detected}
                \nDetails: ${commit.details}
                `
            );
            setFileViewerContent(formattedAnalysis);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze commit messages. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanIssues = async(repoUrl: string) => {
        if (!repoUrl) {
            alert("Please enter a repository URL.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeIssues(repoUrl);
            const issueAnalysis = resp.data.commit_analysis;
            const formattedAnalysis = issueAnalysis.map((issue, index) =>
                `\Issue ${index+1}: 
                \nMessage: ${issue.message} 
                \nSASD Detected: ${issue.sasd_detected}
                \nDetails: ${issue.details}
                `
            );
            setFileViewerContent(formattedAnalysis);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze issue messages. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanMethodComments = async(sourceCode: string) => {
        if (!sourceCode || sourceCode.trim() === "") {
            alert("Please enter a method to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeCodeComments(sourceCode);
            const title = "Method Comment Analysis";
            const data = resp.data;
            setModalData({ title, data });
            setShowModal(true);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze selected code. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanFileComments = async(repoUrl: string, filePath: string) => {
        if (!filePath) {
            alert("Please enter a file to analyze.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeFileComments(repoUrl, filePath);
            const title = "File Comment Analysis";
            const data = resp.data;
            setModalData({ title, data });
            setShowModal(true);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze selected file. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleScanRepository = async(repoUrl: string) => {
        if (!repoUrl) {
            alert("Please enter a repository URL.");
            return;
        }
        setLoading(true);
        try {
            const resp = await analyzeRepository(repoUrl);
            setScanResults(resp.data)
            setShowModal(true);
        }
        catch (error) {
            console.error(error);
            alert("Failed to analyze repository. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const handleAnalysisResult = (title, data) => {
        setModalData({ title, data });
        setShowModal(true);
    }

    const handleFullScanResults = (results) => {
        setScanResults(results);
        setShowTabs(true);
    }

    const handleFileContent = (content) => {
        setFileViewerContent(content);
        setShowTabs(false);
    }

    return {
        loading,
        repoUrl,
        setRepoUrl,
        handleFetchRepoStructure,
        fileTree,
        handleFileClick,
        fileViewerContent,
        setSelectedCode,
        selectedCode,
        selectedFilePath,
        modalData,
        showModal,
        setShowModal,
        showTabs,
        scanResults,
        handleScanCommits,
        handleScanIssues,
        handleScanMethodComments,
        handleScanFileComments,
        handleScanRepository
    };
}