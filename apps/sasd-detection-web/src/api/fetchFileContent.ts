import { GITHUB_API_BASE } from './constants';

interface GitHubContentResponse {
    content: string;
    encoding: string;
}

export async function fetchFileContent(owner: string, repo: string, path: string): Promise<string> {
    const resp = await fetch(`${GITHUB_API_BASE}/repos/${owner}/${repo}/contents/${path}`);

    if (!resp.ok) {
        throw new Error(`Failed to load file "${path}" (${resp.status})`);
    }

    const { content, encoding } = (await resp.json()) as GitHubContentResponse;

    if (encoding !== "base64") {
        throw new Error(`Unsupported file encoding "${encoding}" for "${path}"`);
    }

    return atob(content.replace(/\n/g, ""));
}
