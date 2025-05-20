from src.detection import *
from src.mapping import *
from src.config import AUGMENTED_DATA, COMBINED_OUTPUT, MAPPING_DATA

"""
detection experiment
reads augmented data and runs baseline and nlp approaches
results are merged based on temporary uid
combined results saved to csv file
"""
def run_detection_experiment() -> None:
    df = pd.read_csv(AUGMENTED_DATA, dtype={"Comment": str})
    df["id"] = df.index

    baseline_df = detect_sasd_baseline(df)
    nlp_df = detect_sasd_nlp(df)

    combined_df = pd.merge(baseline_df, nlp_df, on=["id", "Comment"], how="outer")
    combined_df["sasd"] = False

    combined_df.sort_values(by="id", inplace=True)
    combined_df.drop(columns=["id"], inplace=True)
    
    combined_df = combined_df[["Comment", "baseline_result", "nlp_result", "sasd"]]
    combined_df.to_csv(COMBINED_OUTPUT, index=False)
    print(f"Combined results dataset cerated - Stored in {COMBINED_OUTPUT}")

"""
Reads in baseline and nlp detection results from the combined files
Takes the baseline instances and maps them
Stored to mapping/run_i
"""
def run_cwe_mapping_experiment(combined_detection_results: str, mapping_results_output: str) -> None:
    df = pd.read_csv(combined_detection_results, dtype={"Comment": str})
    df["cwe_mapping"] = df.apply(lambda row: baseline_cwe_mapping(row["Comment"]) if row.get("baseline_result", False) else "N/a", axis=1)

    final_columns = ["Comment", "cwe_mapping"]
    df = df[final_columns]
    df.to_csv(mapping_results_output, index=False)
