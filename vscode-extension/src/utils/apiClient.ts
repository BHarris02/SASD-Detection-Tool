/**
 * Module Name: apiClient.ts
 * Description: This module provides functions for interacting with the SASD Detection API.
 *              It includes functions to analyze method bodies, entire files, commit messages, and issue entries
 *              by sending HTTP POST requests using axios. The module abstracts API calls and returns the relevant
 *              response data.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *      - axios
 *      - config
 * Usage:
 *    Import the functions into your project and invoke them as needed. E.g.:
 *       import { analyzeMethod } from './apiService';
 *       const result = await analyzeMethod("public void myMethod() { ... }");
 */
import axios from "axios";
import config from "./config";

/**
 * Function to make a POST request to the analyze method endpoint in the backend
 * 
 * @param methodBody raw source code with comments
 * @returns response from the endpoint with analysis details
 */
export const analyzeMethod = async (methodBody: string) => {
    const apiUrl = `${config.BASE_API_URL}/analyze/method`;
    try {
        const resp = await axios.post(apiUrl, { method_body: methodBody });
        return resp.data;
    }
    catch (error) {
        throw error;
    }
};

/**
 * Function to make a POST request to the analyze file endpoint in the backend
 * 
 * @param repo repository url - `user/repository`
 * @param path the path in the repository to the file
 * @returns response from the API with file analysis details
 */
export const analyzeFile = async (repo: string, path: string) => {
    const apiUrl = `${config.BASE_API_URL}/analyze/file`;
    try {
        const resp = await axios.post(apiUrl, { repo, path });
        return resp.data;
    }
    catch (error) {
        throw error;
    }
};

/**
 * Function to make a POST request to the analyze commit endpoint in the backend
 * 
 * @param repo repository url - `user/repository`
 * @returns response from the API with commit message analysis details
 */
export const analyzeCommits = async (repo:string) => {
    const apiUrl = `${config.BASE_API_URL}/analyze/commits`;
    try {
        const resp = await axios.post(apiUrl, { repo });
        return resp.data.commit_analysis;
    }
    catch (error) {
        throw error;
    }
};

/**
 * Function to make a POST request to the analyze issues endpoint in the backend
 * 
 * @param repo repository url - `user/repository`
 * @returns response from the API with issue tracker entry analysis details
 */
export const analyzeIssues = async (repo: string) => {
    const apiUrl = `${config.BASE_API_URL}/analyze/issues`;
    try {
        const resp = await axios.post(apiUrl, { repo });
        return resp.data.issue_analysis;
    }
    catch (error) {
        throw error;
    }
}

