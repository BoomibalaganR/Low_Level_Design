class Player:
    def __init__(self, name, symbol) -> None:
        self._name = name
        self._symbol = symbol

    def get_symbol(self):
        return self._symbol

    def get_name(self):
        return self._name
