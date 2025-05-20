/**
 * Module Name: analyzeEntireDocument.ts
 * Description: This module exports a function, which analyzes the entirety of the active
 *              text document in VSCode for SASD. It retrieves the active file's path,
 *              verifies the existence of a Git repository using the Git extension, and sends the file for analysis via
 *              the `analyzeFile` API. Upon receiving the analysis results, it highlights affected methods in the document
 *              and displays details (including CWE mappings) through editor decorations.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *    - vscode
 *    - ../utils/apiClient
 *    - ../utils/gitUtils
 * Usage:
 *    This function is intended to be registered as a command. When executed,
 *    it analyzes the curerntly opened file in the current Git repository and 
 *    displays a formatted webview panel with the results.
 *
 */
import * as vscode from 'vscode';
import { analyzeFile } from '../utils/apiClient';
import { gitRepoDetails } from '../utils/gitUtils';

/**
 * Function to initiate the process to analyze all functions comments in the current active file
 * 
 * @returns formatted HTML with analysis details
 */
export const analyzeEntireDocument = async () => {
    const editor = vscode.window.activeTextEditor;

    if (!editor) {
        vscode.window.showErrorMessage('No active editor found.');
        return;
    }

    const filePath = editor.document.uri.fsPath;
    const relativePath = vscode.workspace.asRelativePath(editor.document.uri);

    const repoDetails = await gitRepoDetails();

    if (!repoDetails) {
        vscode.window.showErrorMessage('This functionality requires a Git repository. Please open a Git-enabled workspace.');
        return;
    }

    const { ownerRepo } = repoDetails;

    try {
        const res = await analyzeFile(ownerRepo, relativePath);

        if (res.code_analysis && res.code_analysis.length > 0) {
            vscode.window.showInformationMessage(`SASD Detected in ${res.code_analysis.length} methods.`);

            const decorationType = vscode.window.createTextEditorDecorationType({
                backgroundColor: "rgba(255,0,0,0.3)",
                border: "1px solid red"
            });

            const doc = editor.document;
            const decorationOptions: vscode.DecorationOptions[] = [];

            res.code_analysis.forEach((analysis: any) => {
                const signature: string = analysis.method_signature;
                const fullText = doc.getText();
                const index = fullText.indexOf(signature);

                if (index !== -1) {
                    const startPos = doc.positionAt(index);
                    const endPos = doc.positionAt(index + signature.length);

                    const formattedDetails = typeof analysis.details === "object" ? JSON.stringify(analysis.details, null, 2) : analysis.details;
                    const formattedCweMapping = typeof analysis.cwe_mapping === "object" ? JSON.stringify(analysis.cwe_mapping, null, 2) : analysis.cwe_mapping;

                    decorationOptions.push({
                        range: new vscode.Range(startPos, endPos),
                        hoverMessage: new vscode.MarkdownString(
                            `**SASD Detected**\n\n` +
                            `**Details:**\n\n\`\`\`json\n${formattedDetails}\n\`\`\`\n\n` +
                            `**CWE Mapping:**\n\n\`\`\`json\n${formattedCweMapping}\n\`\`\``
                        )
                    });

                } 
                else {
                    console.warn(`Could not locate signature: ${signature} in the document.`);
                }
            });

            editor.setDecorations(decorationType, decorationOptions);
        }
        else {
            vscode.window.showInformationMessage('No SASD Detected in the current file.');
        }
    }
    catch (error: any) {
        vscode.window.showErrorMessage(`Failed to analyze file: ${error.message}`);
    }

}