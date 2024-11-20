class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._position = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_position(self):
        return self._cur_pos

    def set_position(self, cur_pos):
        self._cur_pos = cur_pos
