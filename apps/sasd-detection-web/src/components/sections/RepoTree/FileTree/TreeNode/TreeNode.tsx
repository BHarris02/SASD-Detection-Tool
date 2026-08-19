import { FaFolder, FaFileAlt } from 'react-icons/fa';
import type { RepoNode } from "@/types/repo";
import styles from './TreeNode.module.css';

interface TreeNodeProps {
    node: RepoNode;
    onFileSelect: (path: string) => void;
}

export default function TreeNode({ node, onFileSelect }: TreeNodeProps) {
    if (node.type === "folder") {
        return (
            <li>
                <div className={styles.treeNode}>
                    <FaFolder />
                    { node.name }
                </div>
                <ul className={styles.childList}>
                    {node.children.map((child) => 
                        <TreeNode key={child.name} node={child} onFileSelect={onFileSelect}/>
                    )}
                </ul>
            </li>
        );
    }

    return (
        <li className={styles.treeNode} onClick={() => onFileSelect(node.path)}>
            <FaFileAlt />
            { node.name }
        </li>
    );
}
