/**
 * Module Name: extension.ts
 * Description: This module serves as the main entrypoint for the VSCode Extension.
 *              It loads environment variables, initializes the extension, and registers
 *              commands.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *    - vscode
 *    - dotenv
 *    - ./commands/analyzeSelectedCode
 *    - ./commands/analyzeEntireDocument
 *    - ./commands/analyzeCommitMessages
 *    - ./commands/analyzeIssueEntries
 *    - ./commands/myTreeDataProvider
 *    - ./utils/progressWrapper
 * Usage:
 *    The extension is activated when VSCode loads it. The `activate` function registers commands
 *    with command palette. Commands can be invoked by users to analyze code or repository artifacts
 *    for Self-Admitted Security Debt (SASD).
 *
 */
import * as vscode from 'vscode';
import * as dotenv from 'dotenv';
import { analyzeSelectedCode } from './commands/analyzeSelectedCode';
import { analyzeEntireDocument } from './commands/analyzeEntireDocument';
import { analyzeCommitMessages } from './commands/analyzeCommitMessages';
import { analyzeIssuesEntries } from './commands/analyzeIssueEntries';
import { MyTreeDataProvider } from './commands/myTreeDataProvider';
import { runWithProgress } from './utils/progressWrapper';

dotenv.config();

/**
 * Register commands for each function of the SASD Detection Tool
 * 
 * @param context VSCode Extension context
 */
export function activate(context: vscode.ExtensionContext) {
    console.log('SASD VSCode Extension Active');

    const treeDataProvider = new MyTreeDataProvider();
    vscode.window.registerTreeDataProvider("myView", treeDataProvider);

    const analyzeSelectedDisposable = vscode.commands.registerCommand('sasd.analyzeSelectedCode', async () => {
        await runWithProgress(
            "Analysing Selected Code...",
            analyzeSelectedCode,
            "Analysis complete."
        );
    });
    context.subscriptions.push(analyzeSelectedDisposable);

    const analyzeEntireDocumentDisposable = vscode.commands.registerCommand('sasd.analyzeEntireDocument', async () => {
        await runWithProgress(
            "Analysing Entire Active Document...",
            analyzeEntireDocument,
            "Analysis complete."
        );
    });
    context.subscriptions.push(analyzeEntireDocumentDisposable);

    const analyzeCommitMessagesDisposable = vscode.commands.registerCommand('sasd.analyzeCommitMessages', async () => {
        await runWithProgress(
            "Analysing Repository Commit Messages...",
            analyzeCommitMessages,
            "Analysis complete."
        );
    });
    context.subscriptions.push(analyzeCommitMessagesDisposable);

    const analyzeIssueEntriesDisposable = vscode.commands.registerCommand('sasd.analyzeIssueEntries', async () => {
        await runWithProgress(
            "Analysing Repository Issue Entries...",
            analyzeIssuesEntries,
            "Analysis complete."
        );
    });
    context.subscriptions.push(analyzeIssueEntriesDisposable);
}

export function deactivate(){}