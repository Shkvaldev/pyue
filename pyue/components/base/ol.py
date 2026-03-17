from pyue.core.component import Component


class OL(Component):
    def __init__(
        self,
        **kwargs,
    ) -> None:
        classes = ["list-decimal", "list-inside", "pl-5"]
        super().__init__(tag="ol", classes=classes, **kwargs)
