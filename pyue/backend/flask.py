import traceback
from loguru import logger

from pyue.core.backend import Backend
from pyue.core.page import Page
from pyue.core.errors import BackendNotFoundError, AddPageError, MountBackendError

try:
    from flask import Flask, Blueprint, render_template, abort
except ImportError:
    raise BackendNotFoundError("flask")


class FlaskBackend(Backend):
    """
    Backend for Flask web framework
    """

    def __init__(
        self,
        static_path: str,
        template_path: str,
        router: Blueprint | None = None,
        logger=logger,
    ) -> None:
        """
        Initialize the FlaskBackend.

        Args:
            static_path (str): Path to the static files directory.
            template_path (str): Path to the templates directory.
            router (Blueprint | None, optional): An existing Flask Blueprint to use.
                If None, a new Blueprint is created. Defaults to None.
            logger: Logger instance for logging messages. Defaults to the loguru logger.
        """
        super().__init__()
        self.logger = logger
        if router and isinstance(router, Blueprint):
            self._router = router
        else:
            self._router = Blueprint(
                "frontend",
                __name__,
                template_folder=template_path,
                static_folder=static_path,
            )
        self.static_path = static_path
        self.template_path = template_path

    @property
    def router(self) -> Blueprint:
        """
        Blueprint: The Flask Blueprint associated with this backend.
        """
        return self._router

    def add_page(self, page: Page, url: str, context_func=None) -> None:
        """
        Add a page to the backend's Blueprint.

        Args:
            page (Page): The page object containing the template filename and other page data.
            url (str): The URL rule for the page (e.g., '/' or '/about').
            context_func (callable, optional): A function that returns a dictionary of additional context variables.
                The function receives any keyword arguments captured from the URL and should return a dict.
                Defaults to None.

        Raises:
            AddPageError: If adding the page to the Blueprint fails due to an exception.
        """
        try:
            # Handler with context support
            def handler(**kwargs):
                try:
                    context = kwargs
                    if context_func:
                        extra_context = context_func(**kwargs)
                        if isinstance(extra_context, dict):
                            context.update(extra_context)
                    return render_template(page.filename, **context)
                except Exception:
                    self.logger.error(f"Failed to show page: {traceback.format_exc()}")
                    abort(500)

            self._router.add_url_rule(
                url, endpoint=url.replace("/", "_"), view_func=handler, methods=["GET"]
            )
        except Exception as e:
            self.logger.error(f"Failed to add page: {e}")
            raise AddPageError(traceback.format_exc())

    def mount(self, app: Flask) -> None:
        """
        Mount the backend's Blueprint onto a Flask application.

        Args:
            app (Flask): The Flask application instance.

        Raises:
            MountBackendError: If registering the blueprint with the Flask app fails.
        """
        try:
            app.template_folder = self.template_path
            app.static_folder = self.static_path
            app.register_blueprint(self.router)
        except Exception as e:
            self.logger.error(f"Failed to mount backend: {e}")
            raise MountBackendError(traceback.format_exc())
