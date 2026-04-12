import axios from 'axios';

export async function fetchRepoStructure(repoUrl: string) {
    return axios.get('/api/vcs/repository-structure', { params: { repo_url: repoUrl }});
}

export async function fetchFileContent(repoUrl: string, filePath: string) {
    return axios.get('/api/vcs/file-content', { params: { repo_url: repoUrl, file_path: filePath }});
}
