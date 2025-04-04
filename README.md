# PyBundler

[![PyPI version](https://badge.fury.io/py/pybundler.svg)](https://badge.fury.io/py/pybundler) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) Pack and unpack Python project source code into a single, structured text file. Ideal for sharing, archiving snapshots, and interacting with Large Language Models (LLMs) like Gemini, Claude, or GPT.

## The Problem

Sharing multi-file codebases or providing them as context to LLMs can be cumbersome. You might need to zip archives, copy-paste multiple files, or struggle with context window limits. LLMs often work best when they can see the relevant code structure and content together.

## The Solution

`pybundler` traverses your project directory, reads the text-based source files, and concatenates them into one `.pybundle` file. Each file's content is clearly marked with its original path. It intelligently ignores files based on default patterns (like `.git`, `__pycache__`, `.venv`) and your project's `.gitignore` file (or a custom ignore file).

You can then easily share this single file or paste its content into an LLM prompt. `pybundler` can also unpack this bundle file back into the original directory structure.

**Key Features:**

- Packs relevant project files into a single text file (`.pybundle`).
- Unpacks a `.pybundle` file back into a directory structure.
- Uses `.gitignore` syntax for excluding files (reads `.gitignore` by default, supports custom ignore files).
- Includes sensible default ignores for common temporary files, caches, and VCS directories.
- Provides clear markers showing the original path of each file within the bundle.
- Skips likely binary files.
- Simple Command-Line Interface (CLI).
- Can also be used programmatically.

## Installation

```bash
pip install pybundler
```

## Usage

`pybundler` provides two main commands: `bundle` and `unbundle`.

### Bundling a Project (`bundle`)

This command packs a project directory into a single `.pybundle` file.

**Basic Syntax:**

```bash
pybundler bundle <source_directory> [options]
```

**Arguments:**

- `<source_directory>`: (Required) The path to the project directory you want to bundle. Use `.` for the current directory.

**Options:**

- `-o OUTPUT`, `--output OUTPUT`: Specifies the path for the output `.pybundle` file.
  - If omitted, the default is `<source_directory_name>.pybundle` in the current working directory (e.g., bundling `my_project/` creates `my_project.pybundle`).
  - If `<source_directory>` is `.`, the default output is `<current_directory_name>.pybundle`.
- `-i IGNORE`, `--ignore IGNORE`: Path to a custom `.gitignore`-style file. Patterns in this file are added to the patterns found in the standard `.gitignore` within the `source_directory` (if one exists).
- `-h`, `--help`: Show the help message for the `bundle` command.

**Examples:**

1.  **Bundle the current directory into the default output file:**

    ```bash
    pybundler bundle .
    # Creates 'pybundler.pybundle' (if run in the project root)
    ```

2.  **Bundle a specific project directory into a named output file:**

    ```bash
    pybundler bundle ./my_cool_project -o cool_project_bundle.pybundle
    ```

3.  **Bundle the current directory using an additional custom ignore file:**
    ```bash
    pybundler bundle . --ignore ./.custom_ignores
    ```

### Unbundling a Project (`unbundle`)

This command extracts the contents of a `.pybundle` file back into a directory structure.

**Basic Syntax:**

```bash
pybundler unbundle <bundle_file> -o <output_directory> [options]
```

**Arguments:**

- `<bundle_file>`: (Required) The path to the `.pybundle` file you want to unpack.

**Options:**

- `-o OUTPUT`, `--output OUTPUT`: (Required) The path to the target directory where the project structure will be created. The directory will be created if it doesn't exist.
- `-h`, `--help`: Show the help message for the `unbundle` command.

**Examples:**

1.  **Unpack a bundle into a new directory:**

    ```bash
    pybundler unbundle cool_project_bundle.pybundle -o ./unpacked_project
    # Creates ./unpacked_project/ and extracts the contents there
    ```

2.  **Unpack a bundle into an existing directory (will overwrite existing files with the same name):**
    ```bash
    pybundler unbundle project.pybundle -o ./existing_output_dir
    ```

## Programmatic Usage

You can also use `pybundler` directly within your Python code:

```python
from pybundler import pack, unpack
from pathlib import Path

# Define paths
source_dir = Path("./my_project")
bundle_file = Path("my_project.pybundle")
output_dir = Path("./unpacked_project")

try:
    # Pack the project
    pack(source_dir, bundle_file)
    print(f"Project packed into {bundle_file}")

    # Unpack the project
    unpack(bundle_file, output_dir)
    print(f"Project unpacked into {output_dir}")

except FileNotFoundError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```
