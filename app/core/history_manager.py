class HistoryManager:

    def __init__(self):

        self._history = []


    @property
    def history(self):

        return self._history.copy()


    def add(
        self,
        operation: str
    ):

        self._history.append(
            operation
        )


    def clear(self):

        self._history.clear()