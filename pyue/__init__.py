"""Pyue is simple component-based Web UI generator in Python (Inspired by Vue JS and Flutter)"""

from pathlib import Path

from pyue.core.app import App
from pyue.core.backend import Backend, BackendType
from pyue.core.page import Page

__version__ = "0.0.1"
__root__ = Path(__file__).resolve().parent
