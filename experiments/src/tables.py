import pandas as pd

DETECTION_METRICS = "results/detection_metrics.csv"
detection_df = pd.read_csv(DETECTION_METRICS)

def create_baseline_performance_table() -> None:
    baseline_cols = [
        'baseline_precision', 'baseline_false_detection_rate',
        'baseline_recall', 'baseline_specificity',
        'baseline_accuracy', 'baseline_f1'  
    ]

    baseline_performance = detection_df[baseline_cols]

    baseline_latex = baseline_performance.to_latex(
        index=False,
        caption="Baseline Detection Performance",
        label="tab:baseline_detection_performance"
    )

    with open("results/tex/baseline_detection_performance.tex", "w") as file:
        file.write(baseline_latex)

def create_nlp_performance_table() -> None:
    nlp_cols = [
        'nlp_precision', 'nlp_false_detection_rate',
        'nlp_recall', 'nlp_specificity',
        'nlp_accuracy', 'nlp_f1'  
    ]

    nlp_performance = detection_df[nlp_cols]

    nlp_latex = nlp_performance.to_latex(
        index=False,
        caption="NLP Detection Performance",
        label="tab:nlp_detection_performance"
    )

    with open("results/tex/nlp_detection_performance.tex", "w") as file:
        file.write(nlp_latex)