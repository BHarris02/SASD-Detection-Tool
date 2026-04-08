import styles from './RepoFileTree.module.css';
import type { FileTreeNode } from '@/types/vcs';

interface RepoFileTreeProps {
    fileTree: FileTreeNode[] | null;
    selectedFilePath: string | null;
    onFileClick: (file: FileTreeNode) => void;
}

export default function RepoFileTree({ fileTree, selectedFilePath, onFileClick }: RepoFileTreeProps) {
    // utils
    const renderTree = (node: FileTreeNode) => {
        if (!node)
            return null;
        if (node.type === 'folder') {
            return (
                <li key={node.name}>
                    <div className={styles["tree-item"]}>
                        { node.name }
                    </div>
                    <ul>
                        { node.children.map((child) => renderTree(child)) }
                    </ul>
                </li>
            );
        }
        else if (node.type === 'file') {
            return (
                <li
                    key={node.name}
                    className={`styles["tree-item"] ${selectedFilePath === node.path ? styles["selected"]: ""}`}
                    onClick={() => onFileClick(node)}
                >
                </li>
            );
        }
    }
    return (
        <div className={styles["repo-file-tree"]}>
            { fileTree? (
                <ul>{ fileTree.map((node) => renderTree(node)) }</ul>
            ) : (
                <p>No repository loaded.</p>
            )}
        </div>
    );
}