from typing import Union, Optional, List


from pyue.core.component import Component


class A(Component):
    def __init__(
        self,
        idx: str | None = None,
        classes: list[str] | None = None,
        extra_classes: list[str] | None = None,
        v_content: str | None = None,
        v_if: str | None = None,
        v_for: str | None = None,
        content: Optional[List[Union["Component", str]]] = None,
        requirements: set[str] | None = None,
        no_closing: bool = False,
        href: str | None = None,
        **kwargs,
    ) -> None:
        super().__init__(
            tag="a",
            idx=idx,
            classes=classes,
            extra_classes=extra_classes,
            v_content=v_content,
            v_if=v_if,
            v_for=v_for,
            content=content,
            requirements=requirements,
            no_closing=no_closing,
            attr__href=href,
            **kwargs,
        )
