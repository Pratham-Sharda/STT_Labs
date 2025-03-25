import os
import json
import pandas as pd
from datetime import datetime, timezone
import subprocess

# Define directories
JSON_DIR = "json_backup"  # Folder with Bandit JSON reports per repository
REPO_DIR = "repo_copy"  # Folder with cloned repositories
OUTPUT_FILE = "final_bandit_analysis.csv"

def extract_vulnerability_data(json_file, commit_timestamp, commit_hash, repo):
    """Extracts all relevant vulnerability information from a Bandit JSON report."""
    print(f"Processing JSON file: {json_file}")
    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    high_confidence, medium_confidence, low_confidence = 0, 0, 0
    high_severity, medium_severity, low_severity = 0, 0, 0
    cwe_set = set()
    
    for issue in data.get("results", []):
        confidence = issue.get("issue_confidence", "N/A")
        severity = issue.get("issue_severity", "N/A")
        cwe = issue.get("issue_cwe", {}).get("id", "N/A")
        
        # Count confidence levels
        if confidence == "HIGH":
            high_confidence += 1
        elif confidence == "MEDIUM":
            medium_confidence += 1
        elif confidence == "LOW":
            low_confidence += 1
        
        # Count severity levels
        if severity == "HIGH":
            high_severity += 1
        elif severity == "MEDIUM":
            medium_severity += 1
        elif severity == "LOW":
            low_severity += 1
        
        # Collect unique CWEs (convert to string)
        if cwe != "N/A":
            cwe_set.add(str(cwe))  # ✅ Convert CWE IDs to strings before adding

    return {
        "repo": repo,
        "commit_hash": commit_hash,
        "commit_timestamp": commit_timestamp,
        "high_confidence": high_confidence,
        "medium_confidence": medium_confidence,
        "low_confidence": low_confidence,
        "high_severity": high_severity,
        "medium_severity": medium_severity,
        "low_severity": low_severity,
        "unique_cwes": ", ".join(cwe_set) if cwe_set else "None"  # ✅ Ensures strings
    }


def process_reports():
    """Processes all Bandit JSON reports and compiles data into a structured CSV file."""
    print("Starting processing of Bandit reports...")
    all_data = []
    
    for repo in os.listdir(JSON_DIR):
        repo_path = os.path.join(JSON_DIR, repo)
        repo_git_path = os.path.join(REPO_DIR, repo)  # Get Git history from cloned repo

        if not os.path.isdir(repo_path):
            print(f"Skipping missing JSON folder: {repo}")
            continue
        if not os.path.isdir(repo_git_path):
            print(f"⚠️ No Git repo found for {repo} in repo_copy/, skipping Git-based data...")
        
        for report in os.listdir(repo_path):
            if report.endswith(".json"):
                report_path = os.path.join(repo_path, report)
                commit_hash = report.replace("bandit_report_", "").replace(".json", "")
                print(f"Processing report: {report_path} (Commit: {commit_hash})")
                
                commit_timestamp = "Unknown"
                if os.path.isdir(repo_git_path):
                    commit_timestamp = get_commit_timestamp(repo_git_path, commit_hash)
                
                entry = extract_vulnerability_data(report_path, commit_timestamp, commit_hash, repo)
                all_data.append(entry)
    
    # Convert to DataFrame
    df = pd.DataFrame(all_data)
    
    # Track vulnerability introduction and fixes (RQ1)
    df.sort_values(by=["repo", "commit_timestamp"], inplace=True)
    df["is_fixed"] = df.duplicated(subset=["repo", "unique_cwes"], keep=False)
    
    # Aggregate severity trends over time (RQ2)
    severity_trends = df.groupby(["repo", "commit_timestamp"])[["high_severity", "medium_severity", "low_severity"]].sum()
    severity_trends.to_csv("severity_trends.csv")
    print("✅ Saved severity trends to severity_trends.csv")
    
    # Count and rank most frequent CWEs (RQ3)
    cwe_counts = df["unique_cwes"].explode().value_counts()
    cwe_counts.to_csv("cwe_frequencies.csv")
    print("✅ Saved CWE frequency analysis to cwe_frequencies.csv")
    
    # Save the detailed report
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n🎉 Summary saved to {OUTPUT_FILE}")

def get_commit_timestamp(repo_git_path, commit_hash):
    """Gets the timestamp of a given commit using Git from the cloned repository."""
    print(f"Fetching timestamp for commit: {commit_hash} in repo: {repo_git_path}")
    try:
        cmd = f"cd {repo_git_path} && git show -s --format=%ct {commit_hash}"
        timestamp = subprocess.check_output(cmd, shell=True, text=True).strip()
        if timestamp.isdigit():
            formatted_time = datetime.fromtimestamp(int(timestamp), timezone.utc).strftime('%Y-%m-%d %H:%M:%S')
            print(f"Timestamp for commit {commit_hash}: {formatted_time}")
            return formatted_time
        else:
            print(f"Invalid timestamp for commit {commit_hash}, setting to Unknown")
            return "Unknown"
    except subprocess.CalledProcessError:
        print(f"Failed to fetch timestamp for commit {commit_hash}, setting to Unknown")
        return "Unknown"

if __name__ == "__main__":
    process_reports()
