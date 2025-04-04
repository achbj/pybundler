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
