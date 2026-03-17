from typing import List, Union, Optional

from pyue.core.component import Component
from pyue.core.resource import ResourceCss


class CenteredBox(Component):
    """
    A flex container that centers its content vertically.
    Uses Tailwind CSS classes for styling.
    """

    def __init__(
        self,
        middle: bool | None = None,
        **kwargs,
    ):
        """
        Args:
            idx: HTML id attribute.
            classes: List of base Tailwind classes. Defaults to
                ["flex", "items-center", "justify-center"].
            extra_classes: Additional classes appended to the base list.
            content: Child components or strings.
            v_if, v_for, v_content: Jinja2 directives.
            **kwargs: Additional HTML attributes or CSS styles.

        Example:
            ```python
            box = CenteredBox(
                content=[
                    "Hello, world!",
                    A(href="#", content="Click me", classes=["text-blue-500"])
                ],
                extra_classes=["bg-gray-100"]
            )
            ```
        """
        classes = ["flex", "items-center", "justify-center", "flex-col"]

        if middle:
            classes.extend(["h-screen", "overflow-y-auto"])

        super().__init__(
            tag="div",
            classes=classes,
            **kwargs,
        )
