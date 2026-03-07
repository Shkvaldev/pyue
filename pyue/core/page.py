import os
import hashlib
import traceback

from pyue.__root__ import __root__
from pyue.core.errors import PageBuildingError


class Page:
    """Represents WEB page (root for all components)"""

    def __init__(
        self,
        title: str,
        lang: str = "en",
        favicon: str | None = None,
        filename: str | None = None,
    ) -> None:
        self.title = title
        self.lang = lang
        self.favicon = favicon
        self.filename = filename
        if not self.filename:
            hash_object = hashlib.sha256(title.encode())
            hash_hex = hash_object.hexdigest()[:8]
            self.filename = f"page_{hash_hex}.html"
        self.content = []
        self.requirements = []

    def to_string(self) -> str:
        """Renders page to html string"""
        # Using html template
        template_path = os.path.join(__root__, "snippets", "page.html")
        try:
            with open(template_path, "r") as f:
                result = f.read()

            result = result.replace("$TITLE$", self.title)
            result = result.replace("$LANG$", self.lang)
            result = result.replace("$REQUIREMENTS$", "\n".join(self.requirements))

            contents = []
            for content in self.content:
                # TODO: add content rendering logic here
                pass
            result = result.replace("$CONTENT$", "\n".join(contents))
            return result
        except Exception:
            raise PageBuildingError(traceback.format_exc())

    def to_file(self, file_path: str | None) -> None:
        """Renders and saves page to file"""
        try:
            path = file_path or self.filename
            with open(path, "w") as f:
                f.write(self.to_string())
        except Exception:
            raise PageBuildingError(traceback.format_exc())
