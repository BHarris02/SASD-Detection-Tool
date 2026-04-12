import axios from "axios";

export async function analyzeCommits(repoUrl: string) {
    return axios.post('/api/analysis/commits', { repo_url: repoUrl });
}

export async function analyzeIssues(repoUrl: string) {
    return axios.post('/api/analysis/issues', { repo_url: repoUrl });
}

export async function analyzeCodeComments(sourceCode: string) {
    return axios.post('/api/analysis/code-comments', { source_code: sourceCode });
}

export async function analyzeFileComments(repoUrl: string, filePath: string) {
    return axios.post('/api/analysis/file-comments', { repo_url: repoUrl, file_path: filePath });
}

export async function analyzeRepository(repoUrl: string) {
    return axios.post('/api/analysis/repository', { repo_url: repoUrl });
}
