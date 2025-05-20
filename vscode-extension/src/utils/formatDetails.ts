/**
 * Module Name: formatDetails.ts
 * Description: This module provides a utility function to format analysis details
 *              returned by the SASD Detection API.
 * Author: Blake Harris (bharris06@qub.ac.uk)
 * Version: 1.0.0
 * License: MIT License
 * Dependencies: 
 * Usage:
 *      Import this function whereever you need to use it:
 *          import { formatDetails } from '../utils/formatDetails';
 */

/**
 * Utility function to format analysis details returned from the API
 * 
 * @param details raw, unstructured JSON data from the API
 * @returns structured details string 
 */
export function formatDetails(details: string): string {
    if (details.trim() === "No") {
        return "No";
    }

    const lines = details.split('\n').map(line => line.trim()).filter(line => line !== "");
    
    if (lines[0] === "Yes") {
        lines.shift();
    }
    
    const jsonStartIndex = lines.findIndex(line => line.startsWith("{"));
    
    let messagePart = "";
    let jsonPart = "";
    
    if (jsonStartIndex !== -1) {
        messagePart = lines.slice(0, jsonStartIndex).join(" ");
        jsonPart = lines.slice(jsonStartIndex).join(" ");
    } 
    else {
        messagePart = lines.join(" ");
    }
    
    let formattedCweMapping = "";
    
    if (jsonPart) {
        const jsonCompatible = jsonPart.replace(/'/g, "\"");
        try {
            const jsonObj = JSON.parse(jsonCompatible);
            delete jsonObj.details;
            if (jsonObj.cwe_mapping) {
                let cweText = jsonObj.cwe_mapping;
                cweText = cweText.replace(/(\d+\.\s+)/g, "<br>$1").trim()
                formattedCweMapping = cweText;
            }
        } 
        catch (error) {
            formattedCweMapping = jsonPart;
        }
    }
    
    let formattedResult = messagePart;
    if (formattedCweMapping) {
        formattedResult += "<br><strong>CWE Mapping:</strong><br>" + formattedCweMapping;
    }
    return formattedResult;
}