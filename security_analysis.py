import subprocess
import csv

def run_bandit(file_path):
    try:
        result = subprocess.check_output(['bandit', '-f', 'csv', '-o', 'report.csv', file_path], stderr=subprocess.STDOUT)
        print(result.decode())
    except subprocess.CalledProcessError as e:
        print(e.output.decode())

if __name__ == "__main__":
    # Assuming the file path is provided as a command-line argument
    import sys
    if len(sys.argv) != 2:
        print("Usage: python security_analysis.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    run_bandit(file_path)
