import os
import traceback
from typing import Union, Optional, List


from pyue.__root__ import __root__
from pyue.core.errors import ComponentBuildingError


class Component:
    """Represents a reusable page component that can be rendered to HTML.

    Components are the building blocks of Pyue pages, allowing for modular
    and dynamic HTML generation with Jinja2 template support.
    """

    def __init__(
        self,
        tag: str = "div",
        idx: str | None = None,
        classes: list[str] | None = None,
        extra_classes: list[str] | None = None,
        v_content: str | None = None,
        v_if: str | None = None,
        v_for: str | None = None,
        content: Optional[List[Union["Component", str]]] = None,
        requirements: set[str] | None = None,
        **kwargs,
    ) -> None:
        """Initialize a new Component instance.

        Args:
            tag: HTML tag name for the component (e.g., 'div', 'span', 'section').
                Defaults to "div".
            idx: Optional identifier for the component in HTML.
            classes: List of CSS classes to apply to the component.
            extra_classes: Additional CSS classes to append to existing classes.
            v_content: Variable name for content insertion in Jinja2 template.
                The content will be rendered as a variable in the template.
            v_if: Condition string for Jinja2 `if` directive. The component will
                only be rendered if this condition evaluates to true.
            v_for: Loop definition string for Jinja2 `for` directive. Enables
                repetitive rendering of the component.
            content: List of child Component instances or strings to nest inside this component.
            requirements: List of required dependencies or resources for this component.
            **kwargs: Additional HTML attributes and CSS styles. CSS styles will be
                automatically formatted and included in the `style` attribute.
                Key-value pairs will be converted to HTML attributes.

        Example:
            ```python
            component = Component(
                 idx = "box",
                 tag = "div",
                 classes = ["container", "mx-auto"],
                 font_size = "14px",
                 v_content = "message"
            )
            print(component.to_string())
            # <div id="box" class="container mx-auto" style="font-size:14px">
            #     {{ message }}
            #
            # </div>
            ```
        """
        self.tag = tag
        self.idx = idx
        self.classes = classes or []
        self.extra_classes = extra_classes or []
        self.v_content = v_content
        self.v_if = v_if
        self.v_for = v_for
        self.content = content or []
        self.requirements = requirements or set()
        # Using other args as `style` data
        self.styles = {}
        for k, v in kwargs.items():
            self.styles[k.replace("_", "-")] = v

    def to_lines(self, level: int = 0) -> list[str]:
        """Render the component to a list of HTML strings.

        This method generates a list of the complete HTML representations of the component parts,
        including all child components and applying any Jinja2 template directives
        (v_if, v_for, v_content). The rendering process:
        1. Processes the component's HTML tag and attributes
        2. Recursively renders all child components
        3. Applies Jinja2 template syntax for dynamic content
        4. Combines everything into a final list of HTML strings

        Returns:
            List of fully rendered HTML content of the component as strings.

        Raises:
            ComponentBuildingError: If an error occurs during template strings
                rendering, such as malformed template syntax or missing variables.

        Example:
            ```python
            component = Component(tag="h1", v_content="title")
            html = component.to_list()
            print(html)
            # <h1 >{{ title }}</h1>
            ```
        """
        try:
            indent = " " * 4 * level
            inner_indent = " " * 4 * (level + 1)
            result = []

            attrs = []
            if self.idx:
                attrs.append(f'id="{self.idx}"')
            if self.classes or self.extra_classes:
                classes = self.classes + self.extra_classes
                attrs.append(f'class="{" ".join(classes)}"')

            if self.styles:
                styles = []
                for k, v in self.styles.items():
                    styles.append(f"{k}:{v}")

                attrs.append(f'style="{";".join(styles)}"')
            attrs = " " + " ".join(attrs) if attrs else ""

            result.append(f"{indent}<{self.tag}{attrs}>")

            if self.v_content:
                result.append(f"{inner_indent}{{{{ {self.v_content} }}}}")

            for content in self.content:
                if isinstance(content, str):
                    result.append(inner_indent + content)
                    continue
                elif isinstance(content, Component):
                    self.requirements.update(content.requirements)
                    result.extend(content.to_lines(level=level + 1))

            result.append(f"\n{indent}</{self.tag}>")

            if self.v_if:
                result = (
                    [f"{indent}{{% if {self.v_if} %}}"]
                    + result
                    + [f"{indent}{{% endif %}}"]
                )
            if self.v_for:
                result = (
                    [f"{indent}{{% for {self.v_for} %}}"]
                    + result
                    + [f"{indent}{{% endfor %}}"]
                )

            return result
        except Exception:
            raise ComponentBuildingError(traceback.format_exc())

    def to_string(self, level: int = 0) -> str:
        """Return the component as a single string."""
        return "\n".join(self.to_lines(level))
