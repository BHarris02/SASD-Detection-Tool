import pandas as pd
from src.config import SASD_KEYWORDS, API_URL, NLP_MAPPING
import requests, json
from concurrent.futures import ThreadPoolExecutor, as_completed

"""
baseline keyword approach to detection
:param df: dataframe with augmented dataset
:return: dataframe with baseline results
"""
def detect_sasd_baseline(df: pd.DataFrame) -> pd.DataFrame:
    def contains_keywords(comment: str) -> bool:
        comment = comment.lower()
        return any(keyword in comment for keyword in SASD_KEYWORDS)
    
    baseline_df = df.copy()
    baseline_df["baseline_result"] = baseline_df["Comment"].apply(contains_keywords)
    return baseline_df[["id", "Comment", "baseline_result"]]

"""
nlp approach to detection
uses deployed endpoint for results
pipelines comments in parallel for efficiency
produces cwe mapping results as a by product - saved for later experiment
:param df: dataframe with augmented data
:return: dataframe with nlp results
""" 
def detect_sasd_nlp(df: pd.DataFrame) -> pd.DataFrame:
    results = []

    def process_comment(row: dict) -> tuple:
        uid = row["id"]
        comment = row["Comment"]

        try:
            resp = requests.post(API_URL, json = { "method_body": comment }, headers = { "Content-Type": "application/json" }, timeout=10)
            if resp.status_code == 200:
                data = resp.json()

                #byproduct of sasd detection
                cwe_details = data.get("details", {})
                cwe_details_str = json.dumps(cwe_details) if cwe_details else ""

                return uid, comment, data.get("sasd_detected", False), cwe_details_str
            else:
                return uid, comment, False, ""
        except Exception:
            return uid, comment, False, ""
    
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(process_comment, row) for _, row in df.iterrows()]
        for future in as_completed(futures):
            uid, comment, nlp_result, cwe_details = future.result()
            results.append({
                "id": uid,
                "Comment": comment,
                "nlp_result": nlp_result,
                "cwe_mapping_results": cwe_details
            })

    results_df = pd.DataFrame(results)
    results_df.sort_values(by="id", inplace=True)
    
    mapping_df = results_df[["Comment", "cwe_mapping_results"]].copy()
    mapping_df.to_csv(NLP_MAPPING, index=False)

    results_df.drop(columns=["cwe_mapping_results"], inplace=True)
    
    return results_df

