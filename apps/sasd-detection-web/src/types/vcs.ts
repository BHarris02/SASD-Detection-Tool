export interface FileTreeNode {
    type: 'file' | 'folder';
    name: string;
    path: string;
    children?: FileTreeNode[];
}

export interface ModalData {
    title: string;
    data: any
}