import os
import subprocess
import time

# Define test configurations
commands = {
    "pytest_n1_dist_load": "pytest -n 1 --dist load",
    "pytest_n_auto_dist_load": "pytest -n auto --dist load",
    
    "pytest_n1_dist_no": "pytest -n 1 --dist no",
    "pytest_n_auto_dist_no": "pytest -n auto --dist no",
    
    "pytest_parallel_threads_1": "pytest --parallel-threads 1",
    "pytest_parallel_threads_auto": "pytest --parallel-threads auto",
    
    "pytest_n1_dist_load_parallel_1": "pytest -n 1 --dist load --parallel-threads 1",
    "pytest_n1_dist_load_parallel_auto": "pytest -n 1 --dist load --parallel-threads auto",
    
    "pytest_n_auto_dist_load_parallel_1": "pytest -n auto --dist load --parallel-threads 1",
    "pytest_n_auto_dist_load_parallel_auto": "pytest -n auto --dist load --parallel-threads auto",
    
    "pytest_n1_dist_no_parallel_1": "pytest -n 1 --dist no --parallel-threads 1",
    "pytest_n1_dist_no_parallel_auto": "pytest -n 1 --dist no --parallel-threads auto",
    
    "pytest_n_auto_dist_no_parallel_1": "pytest -n auto --dist no --parallel-threads 1",
    "pytest_n_auto_dist_no_parallel_auto": "pytest -n auto --dist no --parallel-threads auto",
}

# Define the main folder
main_folder = "main_folder_parallel"
os.makedirs(main_folder, exist_ok=True)

# Run each command 3 times and store logs
for test_name, command in commands.items():
    test_folder = os.path.join(main_folder, test_name)
    os.makedirs(test_folder, exist_ok=True)

    execution_times = []
    failure_counts = []

    print(f"Running: {test_name}")
    
    for i in range(1, 4):
        log_file = os.path.join(test_folder, f"run_{i}.log")

        # Start time
        start_time = time.time()

        # Run the test and capture output
        with open(log_file, "w") as f:
            process = subprocess.run(command, shell=True, stdout=f, stderr=subprocess.STDOUT)

        # End time
        end_time = time.time()
        execution_time = end_time - start_time
        execution_times.append(execution_time)

        # Count failures
        with open(log_file, "r") as f:
            log_content = f.read()
            failed_tests = log_content.count("FAILED ")
            failure_counts.append(failed_tests)

    # Generate summary file
    summary_file = os.path.join(test_folder, "summary.log")
    with open(summary_file, "w") as f:
        f.write(f"Test Configuration: {test_name}\n")
        f.write(f"Command: {command}\n\n")
        
        for i, (time_taken, failures) in enumerate(zip(execution_times, failure_counts), start=1):
            f.write(f"Run {i}: Time = {time_taken:.2f}s, Failures = {failures}\n")
        
        avg_time = sum(execution_times) / 3
        avg_failures = sum(failure_counts) / 3

        f.write(f"\nAverage Execution Time: {avg_time:.2f}s\n")
        f.write(f"Average Failures: {avg_failures:.2f}\n")

print("All test executions completed. Check 'main_folder' for logs.")
