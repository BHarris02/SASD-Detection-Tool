/**
 * Module Name: myTreeItemData.ts
 * Description: Defines an interface that represents the data structure for a tree view item.
 *              This interface includes a label for display and commandId to associate a command with the tree item.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 * Usage:
 *       Import this interface where tree item data structures are needed. E.g.:
 *          import { MyTreeItemData } from './myTreeItemData';
 */

/**
 * Represents a single item in the tree view
 *
 * @property label - The display label of the tree item
 * @property commandId - The identifier for the command to execute
 */
export interface MyTreeItemData {
    label: string;
    commandId?: string;
}