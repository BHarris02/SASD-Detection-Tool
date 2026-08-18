import { FaFolder, FaFileAlt } from 'react-icons/fa';
import type { RepoNode } from "@/types/repo";
import styles from './TreeNode.module.css';

interface TreeNodeProps {
    node: RepoNode;
}

export default function TreeNode({ node }: TreeNodeProps) {
    if (node.type === "folder") {
        return (
            <li>
                <div className={styles.treeNode}>
                    <FaFolder />
                    { node.name }
                </div>
                <ul className={styles.childList}>
                    {node.children.map((child) => 
                        <TreeNode key={child.name} node={child} />
                    )}
                </ul>
            </li>
        );
    }

    return (
        <li className={styles.treeNode}>
            <FaFileAlt />
            { node.name }
        </li>
    );
}
