"""
Module Name: nlp.py
Description: This module provide utility functions for analyzing GitHub artifacts to
            detect indicators of Self-Admitted Security Debt (SASD) using OpenAI's API.
            It provides:
                - Analyzing commit messages and issues
                - Analysing code comments
                - Mapping detected SASD instances to Common Weakness Enumerations (CWEs)
Author: Blake Harris (bharris06@qub.ac.uk)
Version: 1.0.0
License: MIT License
Dependencies:
    - openai
    - api.utils.config
Usage:
    Import the requred functions into your application. E.g.:
        from api.utils.nlp import analyze_messages, analyze_method, map_to_cwe
"""
import openai # type: ignore
from api.utils.config import (OPENAI_KEY, OPENAI_MODEL)

openai.api_key = OPENAI_KEY

"""
Pipeline repo commit messages/issues into model for analysis
:param list: a list of commit messages or issues
:return list: list of analysis per commit message/issue
"""
def analyze_messages(messages: list) -> list:
    nlp_analysis = []

    for msg in messages:
        prompt = f"""
            Analyze the following Github commit message/issue:
            "{msg}"
            Does it indicate Self-Admitted Security Debt (SASD)?
            Respond with 'Yes' or 'No'.
            If 'Yes', provide a brief explanation (max 3 lines).
        """

        try:
            resp = openai.ChatCompletion.create(
                model=OPENAI_MODEL or "gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": """You are an expert in analyzing Github commit messages for Self-Admitted Security Debt, 
                                    which is technical debt specifically related to security that a developer has explicity acknowledged."""
                    },
                    {"role": "user",
                     "content": prompt
                    }
                ]
            )

            response = resp["choices"][0]["message"]["content"].strip()
            sasd_detected = "Yes" in response

            entry = {
                "message": msg,
                "sasd_detected": sasd_detected,
                "details": response
            }

            # nlp_analysis.append({
            #     "message": msg,
            #     "sasd_detected": sasd_detected,
            #     "details": response
            # })

            if sasd_detected:
                entry["details"] += f"\n\n{map_to_cwe(response)}"
            
            nlp_analysis.append(entry)

        except Exception as e:
                nlp_analysis.append({
                    "message": msg,
                    "sasd_detected": "Exception",
                    "details": f"An Exception occured: {str(e)}"
                })
    
    return nlp_analysis

"""
Pipeline a single method into model for analysis
:param str: str method signature
:param str: str method body
:return dict: details for method analzed
"""
def analyze_method(method_body: str) -> dict:
    prompt = f"""
        Analyze the following method's COMMENTS ONLY for Self-Admitted Security Debt (SASD):
        Method Body: {method_body}
        Your task:
        1. Decide if the comments explicitly indicate the developer acknowledged a security weakness or deferred a security fix. 
        2. Respond with 'Yes' if the comments contain clear evidence of SASD, or 'No' if they don't.
        3. If you answer 'Yes', provide a brief explanation (no more than 3 lines) focusing solely on the explicit acknowledgment of security debt. Do not include generic security references.

        Be cautious and only answer 'Yes' when there is explicit evidence that security work is being deferred or acknowledged as suboptimal. Provide your answer along with a brief confidence level if possible.
    """

    try:
        resp = openai.ChatCompletion.create(
            model=OPENAI_MODEL or "gpt-3.5-turbo",
            messages=[
                {"role": "system", 
                 "content": "You are a highly skilled expert in analyzing code comments for Self-Admitted Security Debt (SASD). "
                 "You strictly focus on whether the comments indicate a developer explicitly acknowledged a security-related "
                 "weakness or deferred necessary security work, and ignore generic references to security that do not imply debt."},
                {"role": "user", "content": prompt}
            ]
        )

        response = resp["choices"][0]["message"]["content"].strip()
        sasd_detected = True if "Yes" in response else False

        return {
            "sasd_detected": sasd_detected,
            "details": response
            }
    except Exception as e:
        return {
            "sasd_detected": False,
            "details": f"An Exception occurred: {str(e)}"
        }  

"""
Pipeline models sasd response back into model for cwe mapping (if applicable)
:param str: str with models sasd response
:return str: models cwe mapping
"""
def map_to_cwe(model_response: str) -> str:
    prompt = f"""
        Analyze the following SASD analysis response:
        "{model_response}"
        Based on this analysis, which Common Weakness Enumeration(s) (CWE) best described the issue?
        Provide the exact CWE Number (e.g, CWE-100) and a brief description (max 3 lines).
    """

    try:
        resp = openai.ChatCompletion.create(
            model=OPENAI_MODEL or "gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert in mapping Self-Admitted Security Debt in code projects to Common Weakness Enumerations"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        response = resp["choices"][0]["message"]["content"].strip()

        return {
            "cwe_mapping": response,
            "details": "Successful CWE mapping"
        }

    except Exception as e:
        return {
            "cwe_mapping": None,
            "details": f"An Exception occurred: {str(e)}"
        }  
