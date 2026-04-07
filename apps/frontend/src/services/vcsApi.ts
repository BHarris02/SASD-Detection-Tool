import axios from 'axios';

export async function fetchRepoStructure(repoUrl: string) {
    return axios.get('/api/vcs/repository-structure', { params: { repo_url: repoUrl }, });
}