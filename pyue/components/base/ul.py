from pyue.core.component import Component


class UL(Component):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        classes = ["list-disc", "list-inside"]
        super().__init__(tag="ul", classes=classes, **kwargs)
