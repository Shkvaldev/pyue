from enum import Enum
from typing import Any
from abc import ABC, abstractmethod

from pyue.core.page import Page


class BackendType(Enum):
    """Available backend frameworks"""

    Flask = 1
    FastAPI = 2


class Backend(ABC):
    """Represents http server for"""

    @property
    def router(self) -> Any:
        """Router with frontend endpoints"""
        raise NotImplementedError()

    @abstractmethod
    def add_page(self, page: Page, url: str, static_path: str, **kwargs) -> None:
        """Includes page into router (Blueprint for Flask, APIRouter for FastAPI) into app"""
        raise NotImplementedError()

    @abstractmethod
    def mount(self, app, **kwargs) -> None:
        """Registers router in backend app"""
        raise NotImplementedError()
