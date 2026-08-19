import FileTree from './FileTree/FileTree';
import RepoEntry from './RepoEntry/RepoEntry';
import styles from './RepoTree.module.css';
import type { RepoNode } from '@/types/repo';

interface RepoTreeProps {
    repoInput: string;
    onRepoInputChange: (value: string) => void;
    fileTree: RepoNode[] | null;
    isLoading: boolean;
    onLoadRepo: () => void;
    onFileSelect: (path: string) => void;
}

export default function RepoTree({
    repoInput,
    onRepoInputChange,
    fileTree,
    isLoading,
    onLoadRepo,
    onFileSelect
}: RepoTreeProps) {
    return (
    <div className={styles.repoTree}>
        <RepoEntry
            value={repoInput}
            onValueChange={onRepoInputChange}
            onSubmit={onLoadRepo}
            isLoading={isLoading}
        />
        <FileTree
            nodes={fileTree}
            isLoading={isLoading}
            onFileSelect={onFileSelect}
        />
    </div>
    );
}
