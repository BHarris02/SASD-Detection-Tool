/**
 * Module Name: progressWrapper.ts
 * Description: This module provides a utility function that runs an asynchronous task while displaying
 *              progress notifications. It wraps any asynchronous function and displays a progress message, 
 *              and a completion message when the task finishes successfully. In case of errors, it displays 
 *              an error message.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *      - vscode
 * Usage:
 *    Import the functions into your project and invoke them as needed. E.g.:
 *      import { runWithProgress } from './progressWrapper';
 *      await runWithProgress("Executing Task", myAsyncTask, "Task complete");
 */
import * as vscode from 'vscode';

/**
 * A simple utility function to wrap asynchronous functions with progress updates
 * 
 * @param title name of the function or process being wrapped
 * @param task the registered VSCode command being ran
 * @param completeMessage an update message, or error, once the task has completed
 * @returns completeMessage
 */
export async function runWithProgress<T>(
    title: string,
    task: () => Promise<T>,
    completeMessage?: string
) : Promise<T> {
    return vscode.window.withProgress({
        location: vscode.ProgressLocation.Notification,
        title: title,
        cancellable: false
    }, async (progress) => {
        progress.report({ message: "Working, please wait..." });
        try {
            const res = await task();
            if (completeMessage) {
                vscode.window.showInformationMessage(completeMessage);
            }
            return res;
        }
        catch (error: any) {
            vscode.window.showErrorMessage(`An error occurred: ${error.message}`);
            throw error;
        }
    });
}