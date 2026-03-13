from typing import Union, Optional
from pyue.core.component import Component
from pyue.core.resource import ResourceCss

TAILWIND_CSS = ResourceCss(
    "https://cdn.jsdelivr.net/npm/tailwindcss@2/dist/tailwind.min.css"
)


class Stack(Component):
    """
    A container that stacks its children vertically or horizontally with consistent spacing.
    Uses flexbox with flex-col (vertical) or flex-row (horizontal) and configurable gap.
    """

    def __init__(
        self,
        direction: str = "vertical",
        spacing: Union[int, str, None] = None,
        align: Optional[str] = None,
        justify: Optional[str] = None,
        **kwargs,
    ):
        """
        Args:
            direction: "vertical" (column) or "horizontal" (row).
            spacing: gap between children (int for Tailwind gap-{n} or custom class).
            align: Tailwind class for align-items (e.g., "items-center").
            justify: Tailwind class for justify-content (e.g., "justify-between").
        
        Example:
            ```python

            # Vertical stack with spacing 4
            Stack(direction="vertical", spacing=4,
                content=[
                    H1("Title"),
                    P("Some description"),
                    Button("Click me")
                ]
            )

            # Horizontal stack with centered alignment
            Stack(direction="horizontal", spacing=2, align="items-center",
                content=[
                    Icon("home"),
                    Span("Home"),
                    Span("/"),
                    Span("Products")
                ]
            )
            ```
        """
        classes = ["flex"]
        if direction == "vertical":
            classes.append("flex-col")
        else:
            classes.append("flex-row")
        if spacing is not None:
            if isinstance(spacing, int):
                classes.append(f"gap-{spacing}")
            else:
                classes.append(spacing)
        if align:
            classes.append(align)
        if justify:
            classes.append(justify)

        super().__init__(
            tag="div", classes=classes, requirements={TAILWIND_CSS}, **kwargs
        )
