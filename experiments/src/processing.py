from src.config import SYNTHETIC_SASD_COMMENTS, DATASET, STRATIFIED_SAMPLE, AUGMENTED_DATA, COMBINED_OUTPUT
import pandas as pd
import glob
import os

"""
takes a stratified sample of the converted Maldonado dataset (1%)
"""
def stratify_sample() -> None:
    with open(DATASET, "r", encoding="utf-8") as file:
        data = file.read().strip()

    entries = [entry for entry in data.split("\n\n") if entry.strip()]
    records = []

    for entry in entries:
        lines = entry.strip().splitlines()
        if len(lines) < 3:
            continue
        project = lines[0].replace("# Project: ", "").strip()
        classification = lines[1].replace("# Classification: ", "").strip()
        comment = lines[2].lstrip("# ").strip()

        records.append({
            "Project": project,
            "Classification": classification,
            "Comment": comment
        })

    df = pd.DataFrame(records)
    total_entries = len(df)

    target_sample = max(1, int(total_entries * 0.01))

    sampled_rows = []

    for classification, group in df.groupby("Classification"):
        group_count = len(group)
        sample_count = round((group_count / total_entries) * target_sample)
        sample_count = min(group_count, sample_count)

        if sample_count > 0:
            sampled = group.sample(n=sample_count, random_state=42)
            sampled_rows.append(sampled)

    if sampled_rows:
        sample_df = pd.concat(sampled_rows)
    else:
        sample_df = pd.DataFrame(columns=df.columns)

    sample_df.to_csv(STRATIFIED_SAMPLE, index=False)

    print(f"Stratified Sample Taken")
    print(f"Total entries: {total_entries}")
    print(f"Target sample: {target_sample}")
    print(f"Sampled rows: {len(sample_df)}")

"""
adds synthetic SASD data to the stratified sample dataset
"""
def synthetic_data_augmentation() -> None:
    sample_df = pd.read_csv(STRATIFIED_SAMPLE)
    synthetic_data = {
        "Project": ["Synthetic_Project"] * len(SYNTHETIC_SASD_COMMENTS),
        "Classification": ["SYNTHETIC_SECURITY"] * len(SYNTHETIC_SASD_COMMENTS),
        "Comment": SYNTHETIC_SASD_COMMENTS
    }
    synthetic_df = pd.DataFrame(synthetic_data)
    augmented_df = pd.concat([sample_df, synthetic_df], ignore_index=True)
    augmented_df.to_csv(AUGMENTED_DATA, index=False)

    print(f"Synthetic Data Augmentation complete - Stored in {AUGMENTED_DATA}")

"""
extracts three sample dataset from detection experiment results for manual verification
"""
def create_verification_samples(seeds: list = [42,99,123]) -> None:
    synthetic_set = set(SYNTHETIC_SASD_COMMENTS)

    combined_df = pd.read_csv(COMBINED_OUTPUT, dtype={'comment': str})

    synthetic_df = combined_df[combined_df["Comment"].isin(synthetic_set)].copy()
    non_synthetic_df = combined_df[~combined_df["Comment"].isin(synthetic_set)].copy()

    synthetic_df = synthetic_df.sort_values(by="Comment").reset_index(drop=True)

    num_synthetic = len(synthetic_df)
    if num_synthetic != 20:
        allocation = [round(num_synthetic / 3)] * 3
        allocation[-1] = num_synthetic - sum(allocation[:-1])
    else:
        allocation = [7,7,6]

    synthetic_groups = []
    start = 0
    for count in allocation:
        synthetic_groups.append(synthetic_df.iloc[start:start+count])
        start += count
    
    total_rows = len(combined_df)
    target_sample_size = max(1, int(total_rows * 0.1))

    for i, seed in enumerate(seeds):
        synthetic_count = allocation[i]
        
        non_synthetic_sample_count = max(1, target_sample_size - synthetic_count)
        non_synthetic_sample = non_synthetic_df.sample(n=non_synthetic_sample_count,
                                                       random_state=seed)
        sample_df = pd.concat([synthetic_groups[i], non_synthetic_sample], ignore_index=True)
        sample_df = sample_df.sample(frac=1, random_state=seed).reset_index(drop=True)

        sample_file = f"results/verification/manual_verification_sample_{seed}_detection.csv"
        sample_df.to_csv(sample_file, index=False)
        print(f"Sample for seed {seed} saved as '{sample_file}'.")

"""
extracts three sample dataset from cwe mapping experiments for manual verification
three from both baseline and nlp results
:param result_file: str file path for sample to be stored
:param file_suffix: str suffix for identifying file
:param seeds: list of seeds for reproduciblity
"""
def create_verification_samples_mapping(detection_dir: str, baseline_mapping_file: str, nlp_mapping_file: str, save_to_dir: str) -> None:
    manually_verified_detection_files = glob.glob(os.path.join(detection_dir, "*.csv"))

    verified_comments = []
    for file in manually_verified_detection_files:
        df = pd.read_csv(file, dtype={"Comment": str})
        verified = df[df["sasd"] == True]["Comment"]
        verified_comments.extend(verified.tolist())
    
    verified_comments_set = set(verified_comments)

    baseline_df = pd.read_csv(baseline_mapping_file, dtype={"Comment": str})
    baseline_verified = baseline_df[baseline_df["Comment"].isin(verified_comments_set)].copy()
    baseline_verified["correct"] = False
    baseline_verified.to_csv(f"{save_to_dir}/manual_verification_baseline_mapping.csv", index=False)

    nlp_df = pd.read_csv(nlp_mapping_file, dtype={"Comment": str})
    nlp_verified = nlp_df[nlp_df["Comment"].isin(verified_comments_set)].copy()
    nlp_verified["correct"] = False
    nlp_verified.to_csv(f"{save_to_dir}/manual_verification_nlp_mapping.csv", index=False)




