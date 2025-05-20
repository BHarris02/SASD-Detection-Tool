import csv, os
from src.config import INPUT_FILE, OUTPUT_FILE

"""
Function to read in Maldonado dataset and convert into Python file
with all lines being comments
Collapses multi-line comments
"""
def convert_file() -> None:
    with open(INPUT_FILE, newline="", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
            for row in reader:
                if len(row) < 3:
                    continue

                project, classification, comment = row[0], row[1], row[2]
                collapsed_comment = " ".join(comment.splitlines())

                file.write(f"# Project: {project}\n")
                file.write(f"# Classification: {classification}\n")
                file.write(f"# {collapsed_comment}\n\n")
    
    print(f"Dataset converted - Stored in {OUTPUT_FILE}")

"""
Function to write metrics to single csv file
"""
def write_detection_metrics(metrics: dict, file: str) -> None:
    baseline = metrics.get("baseline_metrics", {})
    nlp = metrics.get("nlp_metrics", {})
    
    row = {
        "baseline_precision": baseline.get("precision"),
        "baseline_false_detection_rate": baseline.get("false_detection_rate"),
        "baseline_recall": baseline.get("recall"),
        "baseline_specificity": baseline.get("specificity"),
        "baseline_accuracy": baseline.get("accuracy"),
        "baseline_f1": baseline.get("f1"),
        "nlp_precision": nlp.get("precision"),
        "nlp_false_detection_rate": nlp.get("false_detection_rate"),
        "nlp_recall": nlp.get("recall"),
        "nlp_specificity": nlp.get("specificity"),
        "nlp_accuracy": nlp.get("accuracy"),
        "nlp_f1": nlp.get("f1"),
        "detection_improvement_rate": metrics.get("detection_improvement_rate")
    }
    
    file_exists = os.path.isfile(file)
    with open(file, mode='a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)

def write_mapping_metrics(baseline_results: dict, nlp_results: dict, file: str) -> None:
    combined_results = {}
    combined_results["baseline_total_mapped_instances"] = baseline_results.get("total_mapped_instances")
    combined_results["baseline_correct_mapping"] = baseline_results.get("correct_mapping")
    combined_results["baseline_mapping_accuracy"] = baseline_results.get("mapping_accuracy")
    combined_results["nlp_total_mapped_instances"] = nlp_results.get("total_mapped_instances")
    combined_results["nlp_correct_mapping"] = nlp_results.get("correct_mapping")
    combined_results["nlp_mapping_accuracy"] = nlp_results.get("mapping_accuracy")

    file_exists = os.path.exists(file)
    with open(file, mode='a', newline='') as csvfile:
        fieldnames = list(combined_results.keys())
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(combined_results)