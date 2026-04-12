import useWorkspace from '@/hooks/useWorkspace';
import AnalysisActions from './AnalysisActions';
import FileViewer from './FileViewer';
import styles from './Workspace.module.css';
import LoadingSpinner from '@/components/ui/LoadingSpinner';
import AnalysisTabs from './AnalysisTabs';

export default function Workspace() {
    // hooks
    const {
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
    } = useWorkspace();

    return (
        <section className={styles.workspace}>
            <LoadingSpinner loading={loading} />
            <div>
                <AnalysisActions
                    onScanCommits={handleScanCommits}
                    onScanIssues={handleScanIssues}
                    onScanCodeComments={handleScanCodeComments}
                    onScanFileComments={handleScanFileComments}
                    onScanRepository={handleScanRepository}
                />
            </div>
            <div>
                { analysisResults ? (
                    <AnalysisTabs results={analysisResults} />
                ) : (
                    <FileViewer
                        fileContent={fileViewerContent}
                        onSelectionChange={setSelectedCode}
                    />
                )}
            </div>
        </section>
    );
}
