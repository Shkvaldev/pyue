import traceback
from loguru import logger

from pyue.core.backend import Backend
from pyue.core.page import Page
from pyue.core.errors import BackendNotFoundError

try:
    from flask import Flask, Blueprint, render_template, abort
except ImportError:
    raise BackendNotFoundError("flask")


class FlaskBackend(Backend):
    """Backend for Flask web framework"""

    def __init__(
        self, static_path: str, router: Blueprint | None = None, logger=logger
    ) -> None:
        super().__init__()
        self.logger = logger
        if router and isinstance(router, Blueprint):
            self._router = router
        else:
            self._router = Blueprint(
                "frontend",
                __name__,
                template_folder=static_path,
                static_folder=static_path,
            )
        self.static_path = static_path

    @property
    def router(self) -> Blueprint:
        return self._router

    def add_page(self, page: Page, url: str) -> None:
        """Includes page into Blueprint"""

        def handler():
            """Handler for html pages"""
            try:
                return render_template(page.filename)
            except Exception:
                self.logger.error(f"Failed to show page: {traceback.format_exc()}...")
                abort(500)

        self._router.add_url_rule(
            url, endpoint=url.replace("/", "_"), view_func=handler, methods=["GET"]
        )

    def mount(self, app: Flask) -> None:
        """Registers router in Flask"""
        app.template_folder = self.static_path
        app.static_folder = self.static_path
        app.register_blueprint(self.router)
