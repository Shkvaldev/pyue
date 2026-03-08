import os
from typing import Any
from loguru import logger

from pyue.core.backend import BackendType
from pyue.core.page import Page
from pyue.core.errors import UnsupportedBackendError
from pyue.backend.flask import FlaskBackend


class Pyue:
    """Master of WEB UI"""

    def __init__(
        self,
        backend_type: BackendType,
        static_path: str | None = "static",
        template_path: str | None = "templates",
        logger=logger,
    ) -> None:
        """
        Initialize the Pyue application.

        Args:
            backend_type (BackendType): The type of backend to use (e.g., Flask).
            static_path (str | None, optional): Path to the static files directory.
                Defaults to "static".
            template_path (str | None, optional): Path to the templates directory.
                Defaults to "templates".
            logger: Logger instance for logging messages. Defaults to the loguru logger.

        Raises:
            UnsupportedBackendError: If the provided backend_type is not supported.
        """
        self.logger = logger

        # Creating backend
        if not isinstance(backend_type, BackendType):
            self.logger.error(
                f"Failed to create app with backend type `{backend_type}`"
            )
            raise UnsupportedBackendError(backend_type)

        if backend_type == BackendType.Flask:
            self._backend = FlaskBackend(
                static_path=static_path, template_path=template_path, logger=self.logger
            )
        elif backend_type == BackendType.FastAPI:
            raise NotImplementedError()

        self.static_path = static_path
        self.template_path = template_path

    @property
    def router(self) -> Any:
        """
        Returns the framework-specific router object.

        For Flask backend, this is a Blueprint. For other backends, it will be the
        corresponding router object (e.g., APIRouter for FastAPI).

        Returns:
            Any: The router object from the underlying backend.
        """
        return self._backend.router

    def add_page(self, page: Page, url: str, **kwargs) -> None:
        """
        Add a page to the application and write its template file.

        This method registers the page with the backend's router and writes the
        page's content to a file in the template directory.

        Args:
            page (Page): The page object containing the template content and filename.
            url (str): The URL rule for the page (e.g., '/' or '/about').
            **kwargs: Additional keyword arguments passed to the backend's add_page method,
                such as context_func.
        """
        self._backend.add_page(page=page, url=url, **kwargs)
        page.to_file(os.path.join(self.template_path, page.filename))
        self.logger.debug(
            f"Page `{page.filename}` ({page.title[:50]}) successfully built"
        )

    def mount(self, app, **kwargs):
        """
        Mount the backend's router onto the given framework application.

        This method delegates to the underlying backend's mount method to integrate
        the router with the main application instance (e.g., a Flask app).

        Args:
            app: The framework application instance (e.g., Flask, FastAPI).
            **kwargs: Additional keyword arguments passed to the backend's mount method.
        """
        self._backend.mount(app, **kwargs)
