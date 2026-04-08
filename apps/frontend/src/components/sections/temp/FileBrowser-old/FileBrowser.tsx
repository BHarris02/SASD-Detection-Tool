import LoadingSpinner from "@/components/ui/LoadingSpinner";
import useFileBrowser from "@/hooks/useFileBrowser";
import RepoFileTree from "../RepoFileTree";
import FileViewer from "@/components/sections/FileBrowser-old/FileViewer";

interface FileBrowserProps {
    repoUrl: string;
    onSelectionChange: (selectedText: string) => void;
}

export default function FileBrowser({ repoUrl, onSelectionChange }: FileBrowserProps) {
    const {
        fileTree,
        filePath,
        fileViewerContent,
        loading,
        handleFileClick
    } = useFileBrowser(repoUrl);

    return (
        <>
            <LoadingSpinner loading={loading} />
            <RepoFileTree
                fileTree={fileTree}
                selectedFilePath={filePath}
                onFileClick={handleFileClick}
            />
            <FileViewer
                content={fileViewerContent}
                onSelectionChange={onSelectionChange}
            />
        </>
    );
}
