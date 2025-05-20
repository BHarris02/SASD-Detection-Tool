/**
 * Module Name: analyzeSelectedCode.ts
 * Description: Exports a function that analyzes the selected code in the active VSCode editor.
 *              The function retrieves the user's code selection, sends the selection to an API to 
 *              detect SASD, and then displays a corresponding message and decoration within the editor 
 *              based on the analysis results.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *      - vscode
 *      - ../utils/apiClient
 * Usage:
 *       Import this interface where tree item data structures are needed. E.g.:
 *          import { MyTreeItemData } from './myTreeItemData';
 */
import * as vscode from 'vscode';
import { analyzeMethod } from '../utils/apiClient';

/**
 * Function to analyze user-selected code. Problematic code is highlighted in red
 * 
 * @returns None
 */
export const analyzeSelectedCode = async () => {
    const editor = vscode.window.activeTextEditor;

    if (!editor) {
        vscode.window.showErrorMessage('No active editor found.');
        return; 
    }

    const selection = editor.selection;

    if (selection.isEmpty) {
        vscode.window.showErrorMessage('No code selected. Highlight a method and try again.');
        return; 
    }

    const methodBody = editor.document.getText(selection);

    try {
        const res = await analyzeMethod(methodBody);
        console.log(res);

        if (res.sasd_detected) {
            const msg = `SASD Detected: ${res.details}.\n\n CWE Mapping: ${res.details.cwe_mapping}`;
            vscode.window.showInformationMessage(msg);

            const decorationType = vscode.window.createTextEditorDecorationType({
                backgroundColor: "rgba(255,0,0,0.3)",
            });

            const decorationOptions: vscode.DecorationOptions[] = [{
                    range: selection,
                    hoverMessage: new vscode.MarkdownString(msg),
                }];

            editor.setDecorations(decorationType, decorationOptions);
        }
        else {
            vscode.window.showInformationMessage("No SASD Detected");
        }
    }
    catch (error: any) {
        vscode.window.showErrorMessage(`Failed to analyze method: ${error.message}`);
    }
};