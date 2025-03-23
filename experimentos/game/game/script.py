class Script:
    _disabled: bool

    def __init__(self):
        self._disabled = False

    def is_disabled(self):
        return self._disabled

    def update(self):
        pass