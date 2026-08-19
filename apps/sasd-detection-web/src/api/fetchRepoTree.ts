import type { FileNode, FolderNode, RepoNode } from "@/types/repo";

const GITHUB_API_BASE = "https://api.github.com";

interface GitHubRepoResponse {
    default_branch: string;
}

interface GitHubTreeItem {
    path: string;
    type: "blob" | "tree" | "commit";
}

interface GitHubTreeResponse {
    tree: GitHubTreeItem[];
    truncated: boolean;
}

// GitHub's tree API returns a flat, sorted list of paths; parents always precede their children.
function buildFileTree(items: GitHubTreeItem[]): RepoNode[] {
    const root: RepoNode[] = [];
    const folders = new Map<string, FolderNode>();

    for (const item of items) {
        const segments = item.path.split("/");
        const name = segments[segments.length - 1];
        const parentPath = segments.slice(0, -1).join("/");
        const siblings = parentPath ? folders.get(parentPath)?.children : root;

        if (!siblings) {
            continue;
        }

        if (item.type === "tree") {
            const folderNode: FolderNode = { type: "folder", name, children: [] };
            folders.set(item.path, folderNode);
            siblings.push(folderNode);
        } else if (item.type === "blob") {
            const fileNode: FileNode = { type: "file", name, path: item.path };
            siblings.push(fileNode);
        }
    }

    return root;
}

export async function fetchRepoTree(owner: string, repo: string): Promise<RepoNode[]> {
    const repoResponse = await fetch(`${GITHUB_API_BASE}/repos/${owner}/${repo}`);

    if (repoResponse.status === 404) {
        throw new Error(`Repository "${owner}/${repo}" was not found`);
    }
    if (!repoResponse.ok) {
        throw new Error(`Failed to load repository "${owner}/${repo}" (${repoResponse.status})`);
    }

    const { default_branch: defaultBranch } = (await repoResponse.json()) as GitHubRepoResponse;

    const treeResponse = await fetch(
        `${GITHUB_API_BASE}/repos/${owner}/${repo}/git/trees/${defaultBranch}?recursive=1`
    );

    if (!treeResponse.ok) {
        throw new Error(`Failed to load file tree for "${owner}/${repo}" (${treeResponse.status})`);
    }

    const { tree } = (await treeResponse.json()) as GitHubTreeResponse;

    return buildFileTree(tree);
}
