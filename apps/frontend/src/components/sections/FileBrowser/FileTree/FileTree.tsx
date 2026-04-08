import type { FileTreeNode } from '@/types/vcs';
import styles from './FileTree.module.css';
import { FileTreeFolderNode } from './FileTreeFolderNode';
import { FileTreeFileNode } from './FileTreeFileNode';

interface FileTreeProps {
    tree: FileTreeNode[] | null;
}

export default function FileTree({ tree }: FileTreeProps) {
    // utils
    function renderTree(node: FileTreeNode) {
        if (!node) return null;

        if (node.type === "folder") {
            return <FileTreeFolderNode
                node={node}
                renderTree={renderTree}
            />
        }

        return <FileTreeFileNode
            node={node}
            onFileClick={null}  // temp
        />
    }

    return (
        <div className={styles.fileTree}>
            { tree? (
                <ul>{ tree.map((node) => renderTree(node)) }</ul>
            ) : (
                <p>No repository loaded.</p>
            )}
        </div>
    );
}
