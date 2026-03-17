from pyue.core.component import Component


class LI(Component):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(tag="li", **kwargs)
