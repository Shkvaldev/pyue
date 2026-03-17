from typing import Union
from pyue.core.component import Component


class Col(Component):
    """
    A column component to be used inside a Row in grid mode.
    Specifies how many grid columns the element should span.
    """

    def __init__(self, span: Union[int, str, None] = None, **kwargs):
        """
        Args:
            span:
                int: number of columns to span (e.g., 2 → "col-span-2")
                "full": span across all columns ("col-span-full")
                None: no explicit span (default column)

        Example:
            ```python
            Row(cols=3,
                content=[
                    Col(span=1, content=[P("First column")]),
                    Col(span=2, content=[P("Second column, wider")]),
                ]
            )
            ```
        """
        classes = []
        if span is not None:
            if isinstance(span, int):
                classes.append(f"col-span-{span}")
            elif span == "full":
                classes.append("col-span-full")
        super().__init__(tag="div", classes=classes, **kwargs)
