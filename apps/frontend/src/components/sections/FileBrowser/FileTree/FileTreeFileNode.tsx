import type { FileTreeNode } from "@/types/vcs";

interface FileTreeFileNodeProps {
    node: FileTreeNode
    onFileClick: (file: FileTreeNode) => void;
}

export function FileTreeFileNode({ node, onFileClick }: FileTreeFileNodeProps) {
    return (
        <li
            key={node.name}
            onClick={() => onFileClick(node)}
        />
    );
}
