# Pylint-hook

This git hook runs a pylint check for each file in the selected directory, reads its score and blocks the commit if the score is below the set value.

It requires an pylint to work.

## Usage

```
usage: pylint-hook [-h] [--score_threshold SCORE_THRESHOLD] [--rcfile RCFILE] src_folder

Run Pylint on files in a folder and print scores.

positional arguments:
  src_folder            Path to the source folder to be analyzed.

options:
  -h, --help            show this help message and exit
  --score_threshold SCORE_THRESHOLD
                        Score threshold for failing the check.
  --rcfile RCFILE       Path to the custom .pylintrc
  
```