# Automating Python Projects with Pip, PyPI & Scripting

## Overview

This project demonstrates Python scripting, file handling, dependency management, and automated testing. It implements a reusable log-generation function that creates timestamped text files from a list of log entries.

The project applies Python fundamentals to build a simple, maintainable, and reusable automation tool.

## Features

- Generates timestamped log files using the format `log_YYYYMMDD.txt`.
- Writes each log entry on a separate line.
- Validates input and raises a `ValueError` when the input is not a list.
- Supports empty lists by creating valid empty log files.
- Prints a confirmation message after generating a log file.
- Uses Python functions for modular and reusable code.
- Tracks project dependencies using `requirements.txt`.

## Technologies Used

- Python
- pip and PyPI
- pytest
- Python File I/O
- Git and GitHub

## Project Structure

```text
course-7-module-6-pip-pypi-scripting-lab/
├── generate_log.py
├── lib/
│   └── generate_log.py
├── testing/
├── requirements.txt
├── Pipfile
├── Pipfile.lock
├── pytest
