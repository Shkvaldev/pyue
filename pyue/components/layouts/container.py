from pyue.core.component import Component

class Container(Component):
    """
    A centered container with responsive max-width, based on Tailwind's `container` class.
    By default, the container is centered and has responsive padding. Use `fluid=True` to make
    it full width without max-width constraints.
    """
    def init(
            self,
            fluid: bool = False,
            **kwargs
        ):
        """
        Args:
            fluid: If True, the container spans the full width (no max-width).
                If False (default), uses Tailwind's container class.
        
         Example:
            ```python
            # Default container
            Container(
                content=[
                    H1("Welcome"),
                    P("This text is inside a responsive container.")
                ]
            )

            # Fluid container (full width)
            Container(
                fluid=True,
                extra_classes=["bg-gray-100"],
                content=[P("Full width section")]
            )
            ```
        """
        classes = []
        if not fluid:
            classes.append("container")

        classes.append("mx-auto")
        classes.append("px-4")

        super().__init__(tag="div", classes=classes, **kwargs)
