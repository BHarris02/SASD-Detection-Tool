import pandas as pd
from src.config import SASD_KEYWORDS, CWE_MAPPING

"""
baseline approach to cwe mapping using keyword comparisons
:param comment: string commenttext from the dataset
:return: string with CWE or N/a
"""
def baseline_cwe_mapping(comment: str) -> str:
    comment = comment.lower()
    for keyword in SASD_KEYWORDS:
        if keyword in comment:
            return CWE_MAPPING.get(keyword, "N/a")
    return "N/a"
