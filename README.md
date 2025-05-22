# Hello World Python Project

## Description

This project demonstrates a basic Python setup using `uv` for package management, `ruff` for linting and formatting, and `pytest` for testing. The main script prints a "hello world" message. This project serves as a template for modern Python development workflows.

## Prerequisites

-   **Python**: Python 3.12+ is recommended (this project was set up with Python 3.12).
-   **`uv`**: A fast Python package installer and resolver, written in Rust. If you don't have it, you can install it via pip: `pip install uv`.

## Setup Instructions

1.  **Clone the repository** (if you haven't already):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create/Activate Virtual Environment and Install Dependencies**:

    This project is configured to use `uv`. The virtual environment should ideally be created and managed by `uv`.

    ```bash
    # Create a virtual environment named .venv using Python 3.12 (if not already present)
    # If you used `uv init` to start, this might have been done or a .python-version file created.
    # To explicitly create or ensure it's set up with a specific Python version:
    uv venv .venv --python 3.12 

    # Activate the virtual environment
    # On macOS/Linux:
    source .venv/bin/activate
    # On Windows (Git Bash or WSL):
    # source .venv/Scripts/activate
    # On Windows (Command Prompt):
    # .venv\Scripts\activate.bat
    # On Windows (PowerShell):
    # .venv\Scripts\Activate.ps1
    ```

    Once the virtual environment is activated, install the dependencies (including development tools like `pytest` and `ruff`) using `uv`:

    ```bash
    # Install dependencies defined in pyproject.toml (including the 'dev' extras)
    uv pip install .[dev]
    ```
    This command installs all dependencies listed under `[project.dependencies]` and `[project.optional-dependencies.dev]` in the `pyproject.toml` file.

## How to Run the Code

Ensure your virtual environment is activated.

To run the main application:
```bash
python main.py
```
Or, to be explicit about using the virtual environment's Python interpreter:
```bash
.venv/bin/python main.py
```
This will execute `main.py` and print "hello world" to the console.

## How to Run Tests

Ensure your virtual environment is activated and development dependencies (like `pytest`) are installed.

To run the test suite:
```bash
pytest
```
Or, explicitly using the virtual environment's Python interpreter to run `pytest` as a module:
```bash
.venv/bin/python -m pytest
```
This will discover and run all tests defined in the `tests` directory.

## How to Run Linter/Formatter

Ensure your virtual environment is activated and development dependencies (like `ruff`) are installed.

**Check for linting issues:**
```bash
ruff check .
```
Or, explicitly:
```bash
.venv/bin/python -m ruff check .
```

**Format files automatically:**
```bash
ruff format .
```
Or, explicitly:
```bash
.venv/bin/python -m ruff format .
```
This will format your code according to the rules defined in `pyproject.toml` (under `[tool.ruff]`).

---

This README provides the essential steps to get the project running and to utilize the development tools integrated into it.
