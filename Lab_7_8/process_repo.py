import os
import json
import pandas as pd

# Directory where Bandit JSON reports are stored
RESULTS_DIR = "results"

# Output CSV file
OUTPUT_FILE = "bandit_summary.csv"

# List of repositories to process
TARGET_REPOS = {"tqdm", "seaborn", "pydantic"}

# Prepare a list to store extracted data
data = []

# Loop through each target repository
for repo_name in TARGET_REPOS:
    repo_path = os.path.join(RESULTS_DIR, repo_name)

    if os.path.isdir(repo_path):
        print(f"Processing repository: {repo_name}")

        # Loop through JSON report files
        for report_file in os.listdir(repo_path):
            if report_file.endswith(".json"):
                report_path = os.path.join(repo_path, report_file)
                
                # Extract commit hash from filename
                commit_hash = report_file.replace("bandit_report_", "").replace(".json", "")

                with open(report_path, "r", encoding="utf-8") as file:
                    bandit_data = json.load(file)

                    # Extract confidence and severity counts
                    confidence_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
                    severity_counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
                    unique_cwes = set()  # Store unique CWE IDs

                    # Iterate through scanned files in metrics
                    for file_path, metrics in bandit_data.get("metrics", {}).items():
                        confidence_counts["HIGH"] += metrics.get("CONFIDENCE.HIGH", 0)
                        confidence_counts["MEDIUM"] += metrics.get("CONFIDENCE.MEDIUM", 0)
                        confidence_counts["LOW"] += metrics.get("CONFIDENCE.LOW", 0)

                        severity_counts["HIGH"] += metrics.get("SEVERITY.HIGH", 0)
                        severity_counts["MEDIUM"] += metrics.get("SEVERITY.MEDIUM", 0)
                        severity_counts["LOW"] += metrics.get("SEVERITY.LOW", 0)

                    # Extract CWE identifiers from the results section
                    for issue in bandit_data.get("results", []):
                        cwe_info = issue.get("issue_cwe", {})  # Get CWE dictionary
                        if isinstance(cwe_info, dict):  # Ensure it's a dictionary
                            cwe_id = cwe_info.get("id")  # Extract CWE ID
                            if cwe_id:
                                unique_cwes.add(f"CWE-{cwe_id}")  # Store formatted CWE ID

                    # Collect results
                    data.append({
                        "Repository": repo_name,
                        "Commit": commit_hash,
                        "High Confidence": confidence_counts["HIGH"],
                        "Medium Confidence": confidence_counts["MEDIUM"],
                        "Low Confidence": confidence_counts["LOW"],
                        "High Severity": severity_counts["HIGH"],
                        "Medium Severity": severity_counts["MEDIUM"],
                        "Low Severity": severity_counts["LOW"],
                        "Unique CWEs": ", ".join(unique_cwes) if unique_cwes else "None"
                    })

# Convert extracted data to a DataFrame and save to CSV
df = pd.DataFrame(data)
df.to_csv(OUTPUT_FILE, index=False)

print(f"Analysis complete! Results saved in {OUTPUT_FILE}")
