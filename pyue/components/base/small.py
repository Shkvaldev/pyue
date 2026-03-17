from pyue.core.component import Component


class Small(Component):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        super().__init__(tag="small", **kwargs)
