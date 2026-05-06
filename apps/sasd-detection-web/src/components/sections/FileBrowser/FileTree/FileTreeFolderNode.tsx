import type { FileTreeNode } from "@/types/vcs";
import type { ReactNode } from "react";

interface FileTreeFolderNodeProps {
    node: FileTreeNode;
    renderTree: (child: FileTreeNode) => ReactNode;
}

export function FileTreeFolderNode({ node, renderTree }: FileTreeFolderNodeProps) {
    return (
        <li>
            <div>{ node.name }</div>
            <ul>
                { node.children.map((child) => renderTree(child))}
            </ul>
        </li>
    );
}
