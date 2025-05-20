import pandas as pd
import matplotlib.pyplot as plt

DETECTION_DF = pd.read_csv("results/detection_metrics.csv")
MAPPING_DF = pd.read_csv("results/mapping_metrics.csv")

def detection_bar_chart() -> None:
    baseline_recall_mean = DETECTION_DF["baseline_recall"].mean() * 100
    nlp_recall_mean = DETECTION_DF["nlp_recall"].mean() * 100

    baseline_f1_mean = DETECTION_DF["baseline_f1"].mean() * 100
    nlp_f1_mean = DETECTION_DF["nlp_f1"].mean() * 100

    metrics = ["Recall", "F1-Score"]
    baseline_vals = [baseline_recall_mean, baseline_f1_mean]
    nlp_vals = [nlp_recall_mean, nlp_f1_mean]

    x = range(len(metrics))
    width = 0.35

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar([p - width / 2 for p in x], baseline_vals, width, label="Baseline")
    ax.bar([p + width / 2 for p in x], nlp_vals, width, label="NLP")
    ax.set_ylabel("Percentage (%)")
    ax.set_title("Detection Experiment: Recall and F1-Score")
    ax.set_xticks(x)
    ax.set_xticklabels(metrics)
    ax.legend()

    plt.tight_layout()
    plt.savefig("results/graphs/detection_bar_chart.png", format="png", bbox_inches="tight")
    plt.show()

def detection_line_charts() -> None:
    runs = list(range(1, len(DETECTION_DF) + 1))

    baseline_recall = DETECTION_DF["baseline_recall"] * 100
    nlp_recall = DETECTION_DF["nlp_recall"] * 100
    baseline_f1 = DETECTION_DF["baseline_f1"] * 100
    nlp_f1 = DETECTION_DF["nlp_f1"] * 100

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

    ax1.plot(runs, baseline_recall, marker='o', linestyle='-', label="Baseline Recall")
    ax1.plot(runs, nlp_recall, marker='o', linestyle='-', label="NLP Recall")
    ax1.set_xlabel("Run")
    ax1.set_ylabel("Recall (%)")
    ax1.set_title("Detection Recall Across 10 Runs")
    ax1.set_xticks(runs)
    ax1.legend()
    ax1.grid(True, linestyle='--', alpha=0.5)

    ax2.plot(runs, baseline_f1, marker='o', linestyle='-', label="Baseline F1-Score")
    ax2.plot(runs, nlp_f1, marker='o', linestyle='-', label="NLP F1-Score")
    ax2.set_xlabel("Run")
    ax2.set_ylabel("F1-Score (%)")
    ax2.set_title("Detection F1-Score Across 10 Runs")
    ax2.set_xticks(runs)
    ax2.legend()
    ax2.grid(True, linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("results/graphs/detection_line_charts.png", format="png", bbox_inches="tight")
    plt.show()

def mapping_bar_chart() -> None:
    baseline_acc = MAPPING_DF["baseline_mapping_accuracy"].mean()
    nlp_acc = MAPPING_DF["nlp_mapping_accuracy"].mean()

    methods = ["Baseline", "NLP"]
    mapping_acc = [baseline_acc, nlp_acc]

    fig, ax = plt.subplots(figsize=(4,4))
    bars = ax.bar(methods, mapping_acc, color=["skyblue", "salmon"])    
    ax.set_ylabel("Mapping Accuracy (%)")
    ax.set_title("Mapping Experiment: Mapping Accuracy")

    for bar in bars:
        height = bar.get_height()
        ax.annotate (f"{height:.1f}%", xy=(bar.get_x() + bar.get_width() / 2, height), xytext=(0,3), textcoords="offset points", ha="center", va="bottom")
    
    plt.tight_layout()
    plt.savefig("results/graphs/mapping_bar_chart.png", format="png", bbox_inches="tight")
    plt.show()

def mapping_line_chart() -> None:
    runs = list(range(1, len(MAPPING_DF) + 1))

    baseline_mapping_accuracy = MAPPING_DF["baseline_mapping_accuracy"]
    nlp_mapping_accuracy = MAPPING_DF["nlp_mapping_accuracy"]

    plt.figure(figsize=(7, 5))
    plt.plot(runs, baseline_mapping_accuracy, marker='o', linestyle='-', label="Baseline Mapping Accuracy")
    plt.plot(runs, nlp_mapping_accuracy, marker='o', linestyle='-', label="NLP Mapping Accuracy")
    plt.xlabel("Run")
    plt.ylabel("Mapping Accuracy (%)")
    plt.title("Mapping Accuracy Across 10 Runs")
    plt.xticks(runs)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    plt.savefig("results/graphs/mapping_line_charts.png", format="png", bbox_inches="tight")
    plt.show()