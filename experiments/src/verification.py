import pandas as pd
import json
import re
from src.config import SYNTHETIC_SASD_COMMENTS_MAPPINGS

def verify_cwe_mappings(filepath: str) -> None:
    df = pd.read_csv(filepath)

    def verify_cwe(row):
        comment = row["Comment"].strip()
        if comment in SYNTHETIC_SASD_COMMENTS_MAPPINGS:
            expected_cwes = SYNTHETIC_SASD_COMMENTS_MAPPINGS[comment]
            try:
                mapping_data = json.loads(row["cwe_mapping_results"])
            except json.JSONDecodeError:
                return False
            
            mapping_text = mapping_data.get("cwe_mapping", "")
            match = re.search(r"CWE-\d+", mapping_text)
            extracted_cwe = match.group(0) if match else None
            return extracted_cwe in expected_cwes
        return row["correct"]
    
    df["correct"] = df.apply(verify_cwe, axis=1)
    df.to_csv(filepath, index=False)