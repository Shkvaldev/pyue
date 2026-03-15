from pyue.core.component import Component


class H1(Component):
    """
    Level 1 heading (<h1>).
    """
    def __init__(self, **kwargs):
        classes=["text-4xl", "font-bold", "tracking-tight"]
        super().__init__(tag="h1", classes=classes, **kwargs)

class H2(Component):
    """
    Level 2 heading (<h2>).
    """
    def __init__(self, **kwargs):
        classes=["text-3xl", "font-semibold", "tracking-tight"]
        super().__init__(tag="h2", classes=classes, **kwargs)

class H3(Component):
    """
    Level 3 heading (<h3>).
    """
    def __init__(self, **kwargs):
        classes=["text-2xl", "font-semibold"]
        super().__init__(tag="h3", classes=classes, **kwargs)

class H4(Component):
    """
    Level 4 heading (<h4>).
    """
    def __init__(self, **kwargs):
        classes=["text-xl", "font-semibold"]
        super().__init__(tag="h4", classes=classes, **kwargs)

class H5(Component):
    """
    Level 5 heading (<h5>).
    """
    def __init__(self, **kwargs):
        classes=["text-lg", "font-medium"]
        super().__init__(tag="h5", classes=classes, **kwargs)

class H6(Component):
    """
    Level 6 heading (<h6>).
    """
    def __init__(self, **kwargs):
        classes=["text-base", "font-medium"]
        super().__init__(tag="h6", classes=classes, **kwargs)
