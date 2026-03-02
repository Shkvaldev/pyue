"""
Main entry point for the package when executed with python -m my_project
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
