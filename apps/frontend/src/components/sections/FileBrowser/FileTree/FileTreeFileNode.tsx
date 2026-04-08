import type { FileTreeNode } from "@/types/vcs";

interface FileTreeFileNodeProps {
    node: FileTreeNode
    onFileClick: (file: FileTreeNode) => void;
}

export function FileTreeFileNode({ node, onFileClick }: FileTreeFileNodeProps) {
    return (
        <li onClick={() => onFileClick(node)}>
            { node.name }
        </li>
    );
}
