import useFileBrowser from '@/hooks/useFileBrowser';
import styles from './FileBrowser.module.css';
import FileTree from './FileTree';
import RepositoryInput from './RepositoryInput';
import LoadingSpinner from '@/components/ui/LoadingSpinner';

export default function FileBrowser() {
    // hooks
    const {
        // RepositoryInput props
        loading,
        repoUrl,
        setRepoUrl,
        loadRepoStructure,
        // FileTree props
        fileTree,
        selectedFilePath,
        loadFileContent
    } = useFileBrowser();

    return (
        <section className={styles.fileBrowser}>
            <LoadingSpinner loading={loading} />
            <div>
                <RepositoryInput
                    repoUrl={repoUrl}
                    setRepoUrl={setRepoUrl}
                    onLoadRepoStructure={loadRepoStructure}
                />
            </div>
            <div>
                <FileTree
                    tree={fileTree}
                    selectedFilePath={selectedFilePath}
                    onLoadFileContent={loadFileContent}
                />
            </div>
        </section>
    );
}
