import axios from "axios";

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

export const analyzeCommits = (repo) => 
    axios.post(`${API_BASE_URL}/analyze/commits`, { repo });

export const analyzeIssues = (repo) =>
    axios.post(`${API_BASE_URL}/analyze/issues`, { repo });
  

export const analyzeMethod = (methodBody) =>
    axios.post(`${API_BASE_URL}/analyze/method`, { method_body: methodBody });
  

export const analyzeFile = (repo, path) =>
    axios.post(`${API_BASE_URL}/analyze/file`, { repo, path });
  

export const analyzeRepo = (repo) =>
    axios.post(`${API_BASE_URL}/analyze/repo`, { repo });

