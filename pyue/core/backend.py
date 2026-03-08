from enum import Enum
from typing import Any
from abc import ABC, abstractmethod

from pyue.core.page import Page


class BackendType(Enum):
    """Available backend frameworks"""

    Flask = 1
    FastAPI = 2


class Backend(ABC):
    """Abstract base class for HTTP server backends.

    This class defines the interface that all backend implementations
    must follow.
    """

    @property
    def router(self) -> Any:
        """
        Abstract property that returns the framework-specific router object.

        The router contains all registered frontend endpoints. For Flask,
        this is a Blueprint; for FastAPI, it would be an APIRouter.

        Returns:
            Any: The router instance containing the frontend routes.
        """
        raise NotImplementedError()

    @abstractmethod
    def add_page(self, page: Page, url: str, **kwargs) -> None:
        """
        Add a page to the backend's router.

        This method registers a new route for the given URL and associates it
        with the provided page. The page's content will be served when the URL
        is accessed.

        Args:
            page (Page): The page object containing template and content information.
            url (str): The URL path at which the page should be served.
            **kwargs: Additional framework-specific keyword arguments or context function.
        """
        raise NotImplementedError()

    @abstractmethod
    def mount(self, app, **kwargs) -> None:
        """
        Mount the backend's router onto the main application.

        This method integrates the router containing all frontend pages into
        the main application instance (e.g., a Flask or FastAPI app).

        Args:
            app: The main framework application instance.
            **kwargs: Additional framework-specific keyword arguments for mounting.
        """
        raise NotImplementedError()
