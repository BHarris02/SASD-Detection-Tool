/**
 * Module Name: myTreeDataProvider.ts
 * Description: This module exports the MyTreeDataProvider class which implements the
 *              vscode.TreeDataProvider interface. It creates a tree view for the extension,
 *              with a menu of commands. Each tree item is represented by the MyTreeItemData interface.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 *      - vscode
 *      - ./MyTreeItemData
 * Usage:
 *       Import this interface where tree item data structures are needed. E.g.:
 *          import { MyTreeItemData } from './myTreeItemData';
 */
import * as vscode from 'vscode';
import { MyTreeItemData } from './myTreeItemData';

/**
 * Provides a tree data provider interface for nodes of type MyTreeItemData
 */
export class MyTreeDataProvider implements vscode.TreeDataProvider<MyTreeItemData> {
    private _onDidChangeTreeData: vscode.EventEmitter<MyTreeItemData | null | undefined> = new vscode.EventEmitter<MyTreeItemData | null | undefined>();
    readonly onDidChangeTreeData: vscode.Event<MyTreeItemData | null | undefined> = this._onDidChangeTreeData.event;

    getTreeItem(element: MyTreeItemData): vscode.TreeItem | Thenable<vscode.TreeItem> {
        const treeItem = new vscode.TreeItem(element.label);
        if (element.commandId) {
            treeItem.command = {
                command: element.commandId,
                title: element.label,
                arguments: []
            };
        }
        return treeItem;
    }

    getChildren(element?: MyTreeItemData | undefined): Thenable<MyTreeItemData[]> {
        if (!element) {
            const items: MyTreeItemData[] = [
                {
                    label: "Analyze Selected Code",
                    commandId: "sasd.analyzeSelectedCode"
                },
                {
                    label: "Analyze Entire Document",
                    commandId: "sasd.analyzeEntireDocument"
                },
                {
                    label: "Analyze Repository Commit Messages",
                    commandId: "sasd.analyzeCommitMessages"
                },
                {
                    label: "Analyze Repository Issue Entries",
                    commandId: "sasd.analyzeIssueEntries"
                }
            ];
            return Promise.resolve(items);
        }
        return Promise.resolve([]);
    }
}

