/**
 * Module Name: gitUtils.ts
 * Description: This module provides utility functions to interact with the Git extension in VSCode.
 *              It retrieves repository details and checks if a Git repository exists in the current workspace.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *      - vscode
 * Usage:
 *    Import the functions into your project and invoke them as needed. E.g.:
 *      import { gitRepoDetails, isGitRepo } from './gitUtils';
 *      const details = await gitRepoDetails();
 */
import * as vscode from 'vscode';

/**
 * Function that uses the VSCode Git extension to ensure the working directory is a Git repository
 * If so, the repository URL and owner are set for later use
 * 
 * @returns repository owner and repository URL
 */
export async function gitRepoDetails() {
    const gitExt = vscode.extensions.getExtension('vscode.git');

    if (!gitExt) {
        vscode.window.showErrorMessage('Git extension is not available. Ensure Git is installed and enabled.');
        return null;
    }

    const git = gitExt.exports.getAPI(1);
    const repos = git.repositories;

    if (repos.length === 0) {
        vscode.window.showErrorMessage('No Git repositories found in the current workspace.');
        return null;
    }

    const repo = repos[0];
    const repoPath = repo.rootUri.fsPath;

    const remoteUrl = repo.state.remotes[0]?.fetchUrl || '';
    const match = remoteUrl.match(/github\.com[:/](.+?)\/(.+?)(\.git)?$/);

    if (!match) {
        vscode.window.showErrorMessage('Failed to extract owner/repo from the Git remote URL.');
        return null;
    }

    const ownerRepo = `${match[1]}/${match[2]}`

    return { ownerRepo, repoPath };
}

/**
 * Simple utility function to check if the current working directory is a Git repository
 * 
 * @returns repository owner and URL
 */
export async function isGitRepo() {
    const repoDetails = await gitRepoDetails();
    return repoDetails !== null;
}