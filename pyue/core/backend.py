from typing import Any
from abc import ABC, abstractmethod

from pyue.core.page import Page


class Backend(ABC):
    """Represents http server for"""

    @abstractmethod
    def add_page(self, page: Page, *args, **kwargs):
        """Includes page into router (Blueprint for Flask, APIRouter for FastAPI) into app"""
        pass

    @abstractmethod
    def include_static(self, path: str, url: str, *args, **kwargs):
        """Includes static files"""
        pass
