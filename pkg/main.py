import os
import re
import subprocess
import argparse

def get_pylint_score(filepath):
    args = [filepath]
    pylint_cmd = f"pylint {rcfile} {' '.join(args)}"
    process = subprocess.Popen(pylint_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()

    pattern = r"rated at (\d+\.\d+)/10"
    def print_bad_output(output):
        print("\033[91m{}\033[0m".format(output))  # Output in red

    def print_good_output(output):
        print("\033[92m{}\033[0m".format(output))  # Output in green

    # Extracting the pylint score from the output, printing the score and the pylint output
    for line in stdout.decode("utf-8").splitlines():
        if line.startswith("Your code has been rated at"):
            match = re.search(pattern, line)
            if match:
                score = float(match.group(1))
                if score < score_threshold:
                    print_bad_output(f"{args}: Pylint Score - {score} - [BLOCKED]")
                    print(stdout.decode("utf-8"))
                else:
                    print_good_output(f"{args}: Pylint Score - {score} - [PASSED]")
                return score
    return None

def main():
    exit_code = 0  # By default, set exit code to 0

    parser = argparse.ArgumentParser(description='Run Pylint on files in a folder and print scores.')
    parser.add_argument('src_folder', help='Path to the source folder to be analyzed.')
    parser.add_argument('--score_threshold', type=float, default=8.0, help='Score threshold for failing the check.')
    parser.add_argument('--rcfile', default='', help='Path to the custom .pylintrc')

    global src_folder, score_threshold, rcfile
    args = parser.parse_args()
    src_folder = args.src_folder
    score_threshold = args.score_threshold
    rcfile = args.rcfile

    # We pass the function through all the files .py in the directory
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                score = get_pylint_score(filepath)
                if score is not None and score < score_threshold:
                    exit_code = 1

    exit(exit_code)

if __name__ == "__main__":
    main()
