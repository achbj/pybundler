# src/pybundler/__init__.py
"""
PyBundler: A tool to pack and unpack Python projects into a single file
for easy sharing and LLM interaction.
"""
__version__ = "0.1.0" # Initial version

from .bundler import pack
from .unbundler import unpack

__all__ = ["pack", "unpack", "__version__"]