from typing import Any
from loguru import logger

from pyue.core.backend import BackendType
from pyue.core.page import Page
from pyue.core.errors import UnsupportedBackendError
from pyue.backend.flask import FlaskBackend


class App:
    """Master of web app"""

    def __init__(
        self, backend_type: BackendType, static_path: str, logger=logger
    ) -> None:
        self.logger = logger

        # Creating backend
        if not isinstance(backend_type, BackendType):
            self.logger.error(
                f"Failed to create app with backend type `{backend_type}`"
            )
            raise UnsupportedBackendError(backend_type)
        if backend_type == BackendType.Flask:
            self._backend = FlaskBackend(static_path=static_path, logger=self.logger)
        elif backend_type == BackendType.FastAPI:
            raise NotImplementedError()

        self.logger.debug("App is ready!")

    @property
    def router(self) -> Any:
        return self._backend.router

    def add_page(self, page: Page, url: str, **kwargs) -> None:
        """Includes page into router"""
        self._backend.add_page(page=page, url=url, **kwargs)

    def mount(self, app, **kwargs):
        """Registers router in Flask"""
        self._backend.mount(app, **kwargs)
