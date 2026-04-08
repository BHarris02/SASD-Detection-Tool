import { useAppContext } from "@/context/AppContext";
import { fetchFileContent, fetchRepoStructure } from "@/services/vcsApi";
import type { FileTreeNode } from "@/types/vcs";
import { useState } from "react"

export default function useFileBrowser() {
    // state
    // RepositoryInput
    const [loading, setLoading] = useState<boolean>(false);
    const [repoUrl, setRepoUrl] = useState<string>("");
    // FileTree
    const [fileTree, setFileTree] = useState<FileTreeNode[] | null>(null);
    const [selectedFilePath, setSelectedFilePath] = useState<string | null>(null);
    // global
    const { setFileViewerContent } = useAppContext();

    // handlers
    const loadRepoStructure = async () => {
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
            alert("Failed to fetch repository. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    const loadFileContent = async (file: FileTreeNode) => {
        setSelectedFilePath(file.path);
        setLoading(true);
        try {
            const resp = await fetchFileContent(repoUrl, selectedFilePath);
            setFileViewerContent(resp.data.file_content);
        }
        catch (error) {
            console.error(error);
            alert("Failed to fetch file content. Please try again later.");
        }
        finally {
            setLoading(false);
        }
    }

    return {
        // RepositoryInput
        loading,
        repoUrl,
        setRepoUrl,
        loadRepoStructure,
        // FileTree
        fileTree,
        selectedFilePath,
        loadFileContent
    }
}
