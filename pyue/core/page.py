import os
import hashlib
import traceback
from typing import Union, Optional, List


from pyue.__root__ import __root__
from pyue.core.component import Component
from pyue.core.errors import PageBuildingError


class Page:
    """Represents WEB page (root for all components)"""

    def __init__(
        self,
        title: str,
        lang: str = "en",
        favicon: str | None = None,
        content: Optional[List[Union[Component, str]]] = None,
        filename: str | None = None,
        static_path: str = "static",
    ) -> None:
        """
        Initialize a new Page instance.

        Args:
            title (str): The title of the page, displayed in the browser tab.
            lang (str, optional): The language code for the page (e.g., 'en', 'ru').
                Defaults to "en".
            favicon (str | None, optional): Path or URL to the favicon. Defaults to None.
            content: List of component instances or strings to nest inside this page.
            filename (str | None, optional): Desired filename for the generated HTML file.
                If None, a unique filename is generated from the title. Defaults to None.
            static_path (str | None, optional): Path to the static files directory.
                Defaults to "static".
        """
        self.title = title
        self.lang = lang
        self.favicon = favicon or "favicon.ico"
        self.filename = filename
        if not self.filename:
            hash_object = hashlib.sha256(title.encode())
            hash_hex = hash_object.hexdigest()[:8]
            self.filename = f"page_{hash_hex}.html"
        self.static_path = static_path
        self.content = content or []
        self.requirements = set()

    def to_string(self) -> str:
        """
        Render the page to an HTML string.

        The method generates HTML template using page data
        (title, language, requirements, and content), and returns the resulting string.

        Returns:
            str: The fully rendered HTML content of the page.

        Raises:
            PageBuildingError: If the template file cannot be read or any other
                rendering error occurs.
        """
        # Using html template
        template_path = os.path.join(__root__, "snippets", "page.html")
        try:
            with open(template_path, "r") as f:
                result = f.read()

            result = result.replace("$TITLE$", self.title)
            result = result.replace("$LANG$", self.lang)
            result = result.replace("$FAVICON$", self.static_path + "/" + self.favicon)
            result = result.replace("$REQUIREMENTS$", "\n".join(self.requirements))

            contents = []
            for content in self.content:
                if isinstance(content, str):
                    contents.append(" " * 4 + content)
                    continue
                # Add component requirements
                self.requirements.update(content.requirements)
                contents.extend(content.to_lines(level=1))
            result = result.replace("$CONTENT$", "\n".join(contents))
            return result
        except Exception:
            raise PageBuildingError(traceback.format_exc())

    def to_file(self, file_path: str | None) -> None:
        """
        Render the page and save it to a file.

        This method writes the rendered HTML content to the specified file path.
        If no path is provided, the page's filename attribute is used.

        Args:
            file_path (str | None): The full path where the HTML file should be saved.
                If None, the page's internally generated filename is used.

        Raises:
            PageBuildingError: If writing to the file fails due to an I/O error
                or a rendering error.
        """
        try:
            path = file_path or self.filename
            with open(path, "w") as f:
                f.write(self.to_string())
        except Exception:
            raise PageBuildingError(traceback.format_exc())
