import styles from './FileTree.module.css';
import type { RepoNode } from '@/types/repo';
import TreeNode from './TreeNode/TreeNode';
import LoadingSpinner from '@/components/ui/LoadingSpinner';

interface FileTreeProps {
    nodes: RepoNode[] | null;
    isLoading?: boolean;
    onFileSelect: (path: string) => void;
}

export default function FileTree({ nodes, isLoading, onFileSelect }: FileTreeProps) {
    return (
        <div className={styles.fileTree}>
            {isLoading ? (
                <LoadingSpinner />
            ) : nodes && nodes.length > 0 ? (
                <ul>
                    { nodes.map((node) => (
                        <TreeNode key={node.name} node={node} onFileSelect={onFileSelect}/>
                     ))}
                </ul>
            ) : (
                <p>No repository loaded.</p>
            )}
        </div>
    );
}
