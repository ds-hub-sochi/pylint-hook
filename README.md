# Pylint-hook

This git hook runs a pylint check for each file in the arguments, reads its score and blocks the commit if the score is below the set value.

It requires an pylint to work, but must install it yourself (not tested)

## CLI usage

```
usage: pylint-hook [-h] [--score_threshold SCORE_THRESHOLD] [--rcfile RCFILE] file_paths [file_paths ...]

Run Pylint on files, print scores and blocks the commit if the score is below the set value.

positional arguments:
  file_paths            Path to the file to be checked with Pylint.

options:
  -h, --help            show this help message and exit
  --score_threshold     Score threshold for failing the check.
  --rcfile RCFILE       Path to the custom .pylintrc

```

## Pre-commit example

```

# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: check-docstring-first
      - id: check-merge-conflict
      - id: check-yaml
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: requirements-txt-fixer
  - repo: https://github.com/ds-hub-sochi/pylint-hook.git
    rev: v2.1.2
    hooks:
      - id: pylint-hook
        name: pylint-hook
        language: python
        types: [python]
        args:
          - "--score_threshold=7.0" # пороговое значение pylint
          - "--rcfile=.pylintrc" # путь к кастомному конфигу pylint, без него работает с дефолтным конфигом
        additional_dependencies: [open-metric-learning==0.4.4] # если возникает ошибка unable to import

```
