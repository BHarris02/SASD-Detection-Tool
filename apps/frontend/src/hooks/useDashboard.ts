import { useState } from "react";
import type { FileTreeNode, ModalData } from '@/types/vcs';
import type { ScanResults } from "@/types/analysis";

export function useDashboard() {
    // state
    const [repoUrl, setRepoUrl] = useState<string>("");
    const [fileTree, setFileTree] = useState<FileTreeNode[] | null>(null);
    const [fileViewerContent, setFileViewerContent] = useState<String>("# Select a file to view its content.");
    const [loading, setLoading] = useState<boolean>(false);
    const [selectedCode, setSelectedCode] = useState<string>("");
    const [selectedFilePath, setSelectedFilePath] = useState<string>("");
    const [modalData, setModalData] = useState<ModalData | null>(null);
    const [showModal, setShowModal] = useState<boolean>(false);
    const [showTabs, setShowTabs] = useState<boolean>(false);
    const [scanResult, setScanResults] = useState<ScanResults | null>(null);

    // handlers

    return {
        repoUrl,
        fileTree,
        fileViewerContent,
        loading,
        selectedCode,
        selectedFilePath,
        modalData,
        showModal,
        showTabs,
        scanResult
    };
}