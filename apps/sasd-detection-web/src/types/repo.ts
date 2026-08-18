export interface FileNode {
    type: "file";
    name: string;
    path: string;
}

export interface FolderNode {
    type: "folder";
    name: string;
    children: RepoNode[];
}

export type RepoNode = FileNode | FolderNode;
