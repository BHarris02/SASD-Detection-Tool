import argparse
from src.dataset_conversion import *
from src.processing import *
from src.experiments import *
from src.analysis import *
from src.verification import verify_cwe_mappings
from src.graphs import *
from src.tables import *

def file_functions(args):
    convert_file()
    stratify_sample()
    synthetic_data_augmentation()

def detection_experiment(args):
    run_detection_experiment()
    print("Detection Experiment Finished")
    create_verification_samples()
    print("Manual Verification Samples Created")
    
def mapping_experiment(args):
    for i in range(1, 11):
        run_cwe_mapping_experiment(
            combined_detection_results=f"results/detection/run_{i}/combined_detection_results.csv",
            mapping_results_output=f"results/mapping/run_{i}/baseline_mapping_results.csv"
        )
    print("Mapping Experiment Finished")
    
    for i in range(1, 11):
        create_verification_samples_mapping(
            detection_dir=f"results/verification/run_{i}",
            baseline_mapping_file=f"results/mapping/run_{i}/baseline_mapping_results.csv",
            nlp_mapping_file=f"results/mapping/run_{i}/nlp_mapping_results.csv",
            save_to_dir=f"results/verification/run_{i}"
        )
    print("Manual Verification Samples Created")

def mapping_verification(args):
    for i in range(1, 11):
        verify_cwe_mappings(f"results/verification/run_{i}/manual_verification_nlp_mapping.csv")

def detection_analysis(args):
    for i in range(1, 11):
        results: dict = detection_experiment_analysis(f"results/verification/run_{i}")
        write_detection_metrics(results, "results/detection_metrics.csv")

def mapping_analysis(args):
    for i in range(1, 11):
        baseline_results = mapping_experiment_analysis(f"results/verification/run_{i}/manual_verification_baseline_mapping.csv")
        nlp_results = mapping_experiment_analysis(f"results/verification/run_{i}/manual_verification_nlp_mapping.csv")
        write_mapping_metrics(baseline_results, nlp_results, file="results/mapping_metrics.csv")

def analyses_graphs(args):
    detection_bar_chart()
    detection_line_charts()
    mapping_bar_chart()
    mapping_line_chart()

def analyses_tables(args):
    create_baseline_performance_table()
    create_nlp_performance_table()

def main():
    parser = argparse.ArgumentParser(description = "Experiment Task Executor")
    subparsers = parser.add_subparsers(dest="task", required=True)

    parser_files = subparsers.add_parser("files", help="Run File Functions")
    parser_files.set_defaults(func=file_functions)

    parser_detection = subparsers.add_parser("detection", help="Run detection experiment")
    parser_detection.set_defaults(func=detection_experiment)

    parser_mapping = subparsers.add_parser("mapping", help="Run mapping experiment")
    parser_mapping.set_defaults(func=mapping_experiment)

    parser_mapping_verification = subparsers.add_parser("mapping_verification", help="Verify CWE mappings")
    parser_mapping_verification.set_defaults(func=mapping_verification)

    parser_detection_analysis = subparsers.add_parser("detection_analysis", help="Run detection analysis")
    #parser_detection_analysis.add_argument("--dir", type=str, required=True, help="Manual verification files location")
    parser_detection_analysis.set_defaults(func=detection_analysis)

    parser_mapping_analysis = subparsers.add_parser("mapping_analysis", help="Run mapping analysis")
    parser_mapping_analysis.set_defaults(func=mapping_analysis)

    parser_graph = subparsers.add_parser("graphs", help="Show analysis graphs")
    parser_graph.set_defaults(func=analyses_graphs)

    parser_table = subparsers.add_parser("tables", help="Create performance and metrics tables")
    parser_table.set_defaults(func=analyses_tables)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
