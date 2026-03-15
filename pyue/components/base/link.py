from typing import Union, Optional, List


from pyue.core.component import Component


class Link(Component):
    def __init__(
        self,
        url: str | None = None,
        **kwargs,
    ) -> None:
        classes = ["text-blue-600", "underline"]
        super().__init__(
            tag="a",
            classes=classes,
            attr__href=url or "#",
            **kwargs
        )
