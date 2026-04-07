import LoadingSpinner from "@/components/ui/LoadingSpinner";
import RepoInput from "@/components/sections/RepoInput";
import RepoFileTree from "@/components/sections/RepoFileTree";
import Tab from "@/components/ui/Tab";
import FileViewer from "@/components/ui/FileViewer";
import BackendActions from "@/components/sections/BackendActions";
import Modal from "@/components/ui/Modal";
import { useDashboard } from "@/hooks/useDashboard";

export default function Dashboard() {
    const {
        loading,
        repoUrl,
        setRepoUrl,
        handleFetchRepoStructure,
        fileTree,
        selectedFilePath,
        handleFileClick,
        showTabs,
        scanResults,
        fileViewerContent,
        setSelectedCode,
        handleScanIssues,
        handleScanRepository,
        handleScanCommits,
        handleScanFileComments,
        handleScanMethodComments,
        showModal,
        setShowModal
    } = useDashboard();

    return (
        <div className="dashboard">
            <LoadingSpinner loading={loading} />

            <h1>SASD Detection Tool: Web</h1>

            <RepoInput
                repoUrl={repoUrl}
                setRepoUrl={setRepoUrl}
                fetchRepoStructure={handleFetchRepoStructure}
            />
            <RepoFileTree
                fileTree={fileTree}
                selectedFilePath={selectedFilePath}
                onFileClick={handleFileClick}
            />

            <div>
                { showTabs && scanResults ? (
                    <Tab
                        tabs={[
                            {
                                label: "Commit Analysis",
                                content: null
                            },
                            {
                                label: "Issue Analysis",
                                content: null
                            },
                            {
                                label: "Code Analysis",
                                content: null
                            }
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
                onScanCommits={() => handleScanCommits}
                onScanIssues={() => handleScanIssues}
                onScanCodeComments={() => handleScanMethodComments}
                onScanFileComments={() => handleScanFileComments}
                onScanRepository={() => handleScanRepository(repoUrl)}
            />
            <Modal
                show={showModal}
                onClose={() => setShowModal(false)}
                title="Analysis Result"
            >
                <p>No available data.</p>
            </Modal>
        </div>
    );
}