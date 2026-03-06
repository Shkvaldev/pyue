class UnsupportedBackendError(Exception):
    """Raises when passing unknown backend type"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"Got unsupported backend: {self.message} (see `pyue.BackendType` for options)"


class BackendNotFoundError(Exception):
    """Raises when backend is not installed"""

    def __init__(self, message):
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"Can not find backend package: {self.message} (try to reinstall it via `pip install -U {self.message}`)"
