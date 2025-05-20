import pandas as pd
import glob
import os
from src.config import AUGMENTED_DATA
from sklearn.metrics import confusion_matrix, classification_report

"""
calculate confusion matrix using prediction and ground truth columns
:param df: df with dataset
:param prediction_col: string prediction column name from dataset
:param ground_truth_col: string ground truth column name (default = sasd)
:return: tuple of confusion matrix metrics
"""
def calculate_confusion_matrix(df: pd.DataFrame, prediction_col: str, ground_truth_col: str = "sasd") -> tuple:
    tp = ((df[prediction_col] == True) & (df[ground_truth_col] == True)).sum()
    fp = ((df[prediction_col] == True) & (df[ground_truth_col] == False)).sum()
    fn = ((df[prediction_col] == False) & (df[ground_truth_col] == True)).sum()
    tn = ((df[prediction_col] == False) & (df[ground_truth_col] == False)).sum()

    return tp, fp, fn, tn

"""
calculate metrics
:param tp: num true-positives
:param fp: num false-positives
:param fn: num false-negatives
:param tn: num true-negatives
:return: tuple of metrics
"""
def compute_metrics(tp: int, fp: int, fn: int, tn: int) -> tuple:
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0
    accuracy = (tp + fn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0
    f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    return precision, recall, specificity, accuracy, f1_score

"""
calculates metrics and extrapolates results to full dataset for baseline and nlp approaches
:param str: string path to directory of results
:return: dict of aggregated metrics
"""
def detection_experiment_analysis(dir: str) -> dict:
    files = glob.glob(os.path.join(dir, "*_detection.csv"))
    dfs = [pd.read_csv(file) for file in files]
    df = pd.concat(dfs, ignore_index=True)

    sample_size = len(df)
    total_dataset_size = len(pd.read_csv(AUGMENTED_DATA))
    scale_factor = total_dataset_size / sample_size

    bl_tp, bl_fp, bl_fn, bl_tn = calculate_confusion_matrix(df, "baseline_result")
    nlp_tp, nlp_fp, nlp_fn, nlp_tn = calculate_confusion_matrix(df, "nlp_result")

    bl_prec, bl_recall, bl_spec, bl_acc, bl_f1 = compute_metrics(bl_tp, bl_fp, bl_fn, bl_tn)
    nlp_prec, nlp_recall, nlp_spec, nlp_acc, nlp_f1 = compute_metrics(nlp_tp, nlp_fp, nlp_fn, nlp_tn)

    detection_rate_baseline = bl_prec * 100
    false_detection_rate_baseline = (bl_fp / (bl_tp + bl_fp) * 100) if (bl_tp + bl_fp) > 0 else 0

    detection_rate_nlp = nlp_prec * 100
    false_detection_rate_nlp = (nlp_fp / (nlp_tp + nlp_fp) * 100) if (nlp_tp + nlp_fp) > 0 else 0

    detection_improvement_rate = ((nlp_acc - bl_acc) / bl_acc * 100) if bl_acc > 0 else None

    print("Aggregated Detection Experiment Metrics (from manual verification samples):\n")

    print("Aggregated Sample Metrics (Baseline):")
    print(f"Detection Rate (Precision): {detection_rate_baseline:.2f}%")
    print(f"False Detection Rate: {false_detection_rate_baseline:.2f}%")
    print(f"Recall (Sensitivity): {bl_recall*100:.2f}%")
    print(f"Specificity: {bl_spec*100:.2f}%")
    print(f"Accuracy: {bl_acc*100:.2f}%")
    print(f"F1-Score: {bl_f1*100:.2f}%\n")
    
    print("Aggregated Sample Metrics (NLP):")
    print(f"Detection Rate (Precision): {detection_rate_nlp:.2f}%")
    print(f"False Detection Rate: {false_detection_rate_nlp:.2f}%")
    print(f"Recall (Sensitivity): {nlp_recall*100:.2f}%")
    print(f"Specificity: {nlp_spec*100:.2f}%")
    print(f"Accuracy: {nlp_acc*100:.2f}%")
    print(f"F1-Score: {nlp_f1*100:.2f}%\n")

    if detection_improvement_rate is not None:
        print(f"Detection Improvement Rate: {detection_improvement_rate:.2f}%")
    else:
        print("Detection Improvement Rate: N/A")


    bl_tp_ex = bl_tp * scale_factor
    bl_fp_ex = bl_fp * scale_factor
    bl_fn_ex = bl_fn * scale_factor
    bl_tn_ex = bl_tn * scale_factor
    nlp_tp_ex = nlp_tp * scale_factor
    nlp_fp_ex = nlp_fp * scale_factor
    nlp_fn_ex = nlp_fn * scale_factor
    nlp_tn_ex = nlp_tn * scale_factor

    bl_prec_ex, bl_recall_ex, bl_spec_ex, bl_acc_ex, bl_f1_ex = compute_metrics(bl_tp_ex, bl_fp_ex, bl_fn_ex, bl_tn_ex)
    nlp_prec_ex, nlp_recall_ex, nlp_spec_ex, nlp_acc_ex, nlp_f1_ex = compute_metrics(nlp_tp_ex, nlp_fp_ex, nlp_fn_ex, nlp_tn_ex)
    
    detection_rate_baseline_ex = bl_prec_ex * 100
    false_detection_rate_baseline_ex = (bl_fp_ex / (bl_tp_ex + bl_fp_ex) * 100) if (bl_tp_ex + bl_fp_ex) > 0 else 0
    detection_rate_nlp_ex = nlp_prec_ex * 100
    false_detection_rate_nlp_ex = (nlp_fp_ex / (nlp_tp_ex + nlp_fp_ex) * 100) if (nlp_tp_ex + nlp_fp_ex) > 0 else 0
    detection_improvement_rate_ex = ((nlp_acc_ex - bl_acc_ex) / bl_acc_ex * 100) if bl_acc_ex > 0 else None

    print("\nExtrapolated Metrics (Full Dataset Estimates):\n")
    print("Baseline:")
    print(f"Detection Rate (Precision): {detection_rate_baseline_ex:.2f}%")
    print(f"False Detection Rate: {false_detection_rate_baseline_ex:.2f}%")
    print(f"Recall (Sensitivity): {bl_recall_ex*100:.2f}%")
    print(f"Specificity: {bl_spec_ex*100:.2f}%")
    print(f"Accuracy: {bl_acc_ex*100:.2f}%")
    print(f"F1-Score: {bl_f1_ex*100:.2f}%\n")
    
    print("NLP:")
    print(f"Detection Rate (Precision): {detection_rate_nlp_ex:.2f}%")
    print(f"False Detection Rate: {false_detection_rate_nlp_ex:.2f}%")
    print(f"Recall (Sensitivity): {nlp_recall_ex*100:.2f}%")
    print(f"Specificity: {nlp_spec_ex*100:.2f}%")
    print(f"Accuracy: {nlp_acc_ex*100:.2f}%")
    print(f"F1-Score: {nlp_f1_ex*100:.2f}%\n")

    print(f"Detection Improvement Rate: {detection_improvement_rate_ex:.2f}%")

    return {
        "baseline_metrics": {
            "precision": bl_prec,
            "false_detection_rate": false_detection_rate_baseline,
            "recall": bl_recall,
            "specificity": bl_spec,
            "accuracy": bl_acc,
            "f1": bl_f1,
        },
        "nlp_metrics": {
            "precision": nlp_prec,
            "false_detection_rate": false_detection_rate_nlp,
            "recall": nlp_recall,
            "specificity": nlp_spec,
            "accuracy": nlp_acc,
            "f1": nlp_f1,
        },
        "detection_improvement_rate": detection_improvement_rate
    }


def mapping_experiment_analysis(mapping_file: str, total_mapped_size: int = 645) -> dict:
    df = pd.read_csv(mapping_file)
    total_mapped = len(df)

    correct_mappings = df["correct"].sum()
    mapping_accuracy = (correct_mappings / total_mapped) * 100 if total_mapped > 0 else 0

    print(f"Total Mapped Instances (manual sample): {total_mapped}")
    print(f"Correct CWE Assignments: {correct_mappings}")
    print(f"CWE Mapping Accuracy: {mapping_accuracy:.2f}%")

    y_true = df["correct"]
    conf_matrix = confusion_matrix(y_true, y_true, labels=[True, False])
    print("Confusion Matrix (manual verification):")
    print(conf_matrix)

    print("Classification Report:")
    print(classification_report(y_true, y_true, labels=[True, False]))

    scale_factor = total_mapped_size / total_mapped if total_mapped > 0 else 0
    extrapolated_correct = correct_mappings * scale_factor
    print(f"Extrapolated Correct Mappings (for full dataset): {round(extrapolated_correct)}")

    return {
        "total_mapped_instances": total_mapped,
        "correct_mapping": correct_mappings,
        "mapping_accuracy": mapping_accuracy
    }

