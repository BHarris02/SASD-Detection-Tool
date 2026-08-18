import styles from './FileTree.module.css';
import type { RepoNode } from '@/types/repo';
import TreeNode from './TreeNode/TreeNode';

interface FileTreeProps {
    nodes: RepoNode[];
}

export default function FileTree({ nodes }: FileTreeProps) {
    return (
        <div className={styles.fileTree}>
            {nodes ? (
                <ul>{ nodes.map((node) => TreeNode({ node })) }</ul>
            ) : (
                <p>No repository loaded.</p>
            )}
        </div>
    );
}
