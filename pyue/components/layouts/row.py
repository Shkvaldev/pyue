from typing import Union, List, Optional
from pyue.core.component import Component
from pyue.core.resource import ResourceCss

TAILWIND_CSS = ResourceCss(
    "https://cdn.jsdelivr.net/npm/tailwindcss@2/dist/tailwind.min.css"
)


class Row(Component):
    """
    A container that arranges its children in a grid or flex layout.
    By default uses CSS Grid, but can be switched to Flexbox. Use `Col` components
    as direct children when using Grid mode.

    """

    def __init__(
        self,
        cols: Union[int, List[str], None] = None,
        gap: Union[int, str, None] = None,
        as_flex: bool = False,
        justify: Optional[str] = None,
        align: Optional[str] = None,
        **kwargs,
    ):
        """
        Args:
            cols:
                int: number of equal columns (e.g., 3 → "grid-cols-3")
                List[str]: list of widths for grid-template-columns (e.g., ["1fr", "2fr"])
                None: columns not explicitly set (useful for flex mode)
            gap: spacing between children (int for Tailwind gap-{n} or custom class string)
            as_flex: if True, uses Flexbox instead of Grid
            justify: Tailwind class for justify-content (e.g., "justify-between")
            align: Tailwind class for align-items (e.g., "items-center")
        
        Example:
            ```python
            # Grid with 3 equal columns and gap 4
            Row(cols=3, gap=4,
                content=[
                    Col(content=[Div("Column 1")]),
                    Col(content=[Div("Column 2")]),
                    Col(content=[Div("Column 3")]),
                ]
            )

            # Flex row with items spaced between
            Row(as_flex=True, justify="justify-between",
                content=[
                    Div("Left"),
                    Div("Center"),
                    Div("Right"),
                ]
            )
            ```
        """
        classes = []
        if as_flex:
            classes.append("flex")
            classes.append("flex-wrap")
        else:
            classes.append("grid")
            if cols is not None:
                if isinstance(cols, int):
                    classes.append(f"grid-cols-{cols}")
                elif isinstance(cols, list):
                    cols_style = " ".join(cols)
                    kwargs.setdefault("style", "")
                    kwargs["style"] += f"grid-template-columns: {cols_style};"
        if gap is not None:
            if isinstance(gap, int):
                classes.append(f"gap-{gap}")
            else:
                classes.append(gap)
        if justify:
            classes.append(justify)
        if align:
            classes.append(align)

        super().__init__(
            tag="div", classes=classes, requirements={TAILWIND_CSS}, **kwargs
        )
