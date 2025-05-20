"""
Module Name: data_preprocessing.py
Description: This module provides utility functions for preprocessing source code. It provides:
                - process_comments: To extract comments from given code using a specific comment identifier
                - process_code: To identify and extract specific individual method blocks from raw code
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - re
Usage:
    Import the requred functions into your application. E.g.:
        from api.utils.data_preprocessing import process_comments, process_code
"""
import re

"""
Extracts comments from a code body given a specified identifer
:param code: str containing a method body
:param identifier: str with comment identifier
:return: list of extracted comments
"""
def process_comments(code: str, identifier: str) -> list:
    lines: str = code.splitlines()
    comments: list = [line.strip() for line in lines if line.strip().startswith(identifier)]
    processed_comments: list = [line[len(identifier):].strip() for line in comments]
    return processed_comments

"""
Identifies each method with its code body and comments.
:param code: str containing raw code content
:return: List of dictionaries with method signature, code body, and comments
"""
def process_code(code: str) -> list:
    methods = []
    lines = code.splitlines()
    current_method = None
    current_code_block = []
    inside_method = False

    # Refined pattern to capture a wide range of Java method signatures
    # Supports methods with/without access modifiers, return types, generic types, etc.
    method_pattern = re.compile(r"^\s*(public|protected|private|static|\s)*[\w<>\[\]]+\s+\w+\s*\(.*\)\s*[{]?$")

    for line in lines:
        # Check if the line matches a method signature pattern
        if method_pattern.match(line):
            # Save the previous method if any
            if current_method:
                methods.append({
                    'method_signature': current_method,
                    'method_body': "\n".join(current_code_block)
                })
            
            # Start a new method block
            current_method = line.strip()
            current_code_block = [current_method]
            inside_method = True
        elif inside_method:
            # Add lines to the current method's code block, including indented lines
            current_code_block.append(line)
            # End method if a closing brace '}' is encountered, typical in Java
            if line.strip() == '}':
                inside_method = False
                # Finalize the current method block
                methods.append({
                    'method_signature': current_method,
                    'method_body': "\n".join(current_code_block)
                })
                current_method = None
                current_code_block = []
    
    # Add the last method if any
    if current_method:
        methods.append({
            'method_signature': current_method,
            'method_body': "\n".join(current_code_block)
        })
    
    return methods
