/**
 * Module Name: analyzeIssueEntries.ts
 * Description: This module exports a function, which analyzes GitHub issue entries for SASD using 
 *              the SASD Detection API. It retrieves repository details via the Git extension, invokes the 
 *              issues analysis API, and renders the analysis results in a webview.
 *              The function uses the helper function `formatDetails` to format detailed analysis information for display.
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
import { analyzeIssues } from '../utils/apiClient';
import { gitRepoDetails } from '../utils/gitUtils';
import { formatDetails } from '../utils/formatDetails';

/**
 * Function to analyze issue tracker entries in current active Git repository
 * 
 * @returns formatted HTML with analysis details
 */
export async function analyzeIssuesEntries() {
    const repoDetails = await gitRepoDetails();

    if (!repoDetails) {
        vscode.window.showErrorMessage('Git repository is required for analyzing issues.');
        return;
    }

    const { ownerRepo } = repoDetails;

    try {
        const res = await analyzeIssues(ownerRepo);

        if (res && res.length > 0) {
            const panel = vscode.window.createWebviewPanel(
                'sasdIssuesAnalysis',
                'SASD Analysis: Issues',
                vscode.ViewColumn.One,
                {}
            );

            const detailsHtml = res.map((result: any) => 
                `
                <li>
                    <strong>Message:</strong> ${result.message}<br>
                    <strong>SASD Detected:</strong> ${result.sasd_detected ? 'Yes' : 'No'}<br>
                    <strong>Details:</strong> ${formatDetails(result.details)}<br><br>
                </li>
                `
            ).join('');

            panel.webview.html = `
                <html>
                <body>
                    <h2>SASD Analysis: Issues</h2>
                    <ul>${detailsHtml}</ul>
                </body>
                </html>
            `;
        } 
        else {
            vscode.window.showInformationMessage('No SASD detected in issue comments.');
        }
    } 
    catch (error: any) {
        vscode.window.showErrorMessage(`Failed to analyze issues: ${error.message}`);
    }
}
