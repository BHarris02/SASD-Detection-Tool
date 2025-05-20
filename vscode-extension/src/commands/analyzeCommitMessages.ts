/**
 * Module Name: analyzeCommitMessages.ts
 * Description: This module exports a function, which analyzes commit messages for
 *              SASD in a Git repository. It retrieves repository details using the Git
 *              extension, calls the SASD detection API via the `analyzeCommits` function, 
 *              and presents the formatted results in a VS Code webview panel. The function 
 *              uses the helper `formatDetails` to format the analysis output.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *    - vscode
 *    - ../utils/apiClient
 *    - ../utils/gitUtils
 *    - ../utils/formatDetails
 * Usage:
 *    This function is intended to be registered as a command. When executed,
 *    it analyzes issues associated with the current Git repository and 
 *    displays a formatted webview panel with the results.
 *
 */
import * as vscode from 'vscode';
import { analyzeCommits } from '../utils/apiClient';
import { gitRepoDetails } from '../utils/gitUtils';
import { formatDetails } from '../utils/formatDetails';

/**
 * Function to analyze commit messages:
 *      - ensures the current working directory is a Git repository
 *      - sends the repository information to the helper function to make a POST request
 *      - formats the API response and makes the HTML to display the results
 * 
 * @returns HTML panel with analysis results
 */
export async function analyzeCommitMessages() {
    const repoDetails = await gitRepoDetails();

    if (!repoDetails) {
        vscode.window.showErrorMessage('Git repository is required for analyzing commits.');
        return;
    }

    const { ownerRepo } = repoDetails;

    try {
        const res = await analyzeCommits(ownerRepo);
        if (res && res.length > 0) {
            const panel = vscode.window.createWebviewPanel(
                'sasdCommitsAnalysis',
                'SASD Analysis: Commits',
                vscode.ViewColumn.One,
                {}
            );

            const detailsHtml = res.map((result: any) => 
                `
                <li>
                    <strong>Commit Message:</strong> ${result.message}<br>
                    <strong>SASD Detected:</strong> ${result.sasd_detected ? 'Yes' : 'No'}<br>
                    <strong>Details:</strong> ${formatDetails(result.details)}<br><br>
                </li>
                `
            ).join('');

            panel.webview.html = 
            `
                <html>
                <body>
                    <h2>SASD Analysis: Commit Messages</h2>
                    <ul>${detailsHtml}</ul>
                </body>
                </html>
            `;
        } 
        else {
            vscode.window.showInformationMessage('No SASD detected in commit messages.');
        }
    } 
    catch (error: any) {
        vscode.window.showErrorMessage(`Failed to analyze commits: ${error.message}`);
    }
}
