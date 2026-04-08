import type { FileTreeNode } from "@/types/vcs";
import type { ReactNode } from "react";

interface FileTreeFolderNodeProps {
    node: FileTreeNode;
    onRenderTree: (child: FileTreeNode) => ReactNode;
}

export function FileTreeFolderNode({ node, onRenderTree }: FileTreeFolderNodeProps) {
    return (
        <li key={node.name}>
            <div>
                { node.name }
            </div>
            <ul>
                { node.children.map((child) => onRenderTree(child))}
            </ul>
        </li>
    );
}
