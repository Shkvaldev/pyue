import re


from pyue.core.errors import BadResourceError


class Resource:
    """Represents abstract file (css, js, img), that can be used as a library or resource"""

    def __init__(self, resource: str, pattern: str, **kwargs):
        if not re.search(pattern, resource):
            raise BadResourceError(resource)
        self.resource = resource


class ResourceCss(Resource):
    """Represents css library/code"""

    def __init__(self, resource: str, **kwargs):
        super().__init__(resource=resource, pattern=r"\.css$")


class ResourceJs(Resource):
    """Represents js library/code"""

    def __init__(self, resource: str, **kwargs):
        super().__init__(resource=resource, pattern=r"\.js$")
