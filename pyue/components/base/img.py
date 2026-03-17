from typing import Optional
from pyue.core.component import Component


class Img(Component):
    """
    Image component that renders an `<img>` HTML tag.
    Handles image source and alt text.
    """

    def __init__(
        self,
        src: str,
        alt: str = "",
        width: Optional[int] = None,
        height: Optional[int] = None,
        lazy: bool = True,
        **kwargs
    ):
        """
        Args:
            src: Image source URL or path (take in accordance your static path!)
            alt: Alternative text for accessibility
            width: Optional width in pixels (adds width attribute)
            height: Optional height in pixels (adds height attribute)
            lazy: If True, adds loading="lazy" attribute
        """
        attrs = {"attr__src": src, "attr__alt": alt}

        if width:
            attrs["attr__width"] = str(width)
        if height:
            attrs["attr__height"] = str(height)
        if lazy:
            attrs["attr__loading"] = "lazy"

        super().__init__(tag="img", no_closing=True, **attrs, **kwargs)
