class Board:
    def __init__(self) -> None:
        self._snake = dict()
        self._ladder = dict()
        self._size = 100

    def initialize_board(self):
        snake_pos = [(36, 6), (32, 10), (88, 24)]
        ladder_pos = [(28, 74), (1, 38), (80, 99)]

        self._snake = {pos[0]: pos[1] for pos in snake_pos}
        self._ladder = {pos[0]: pos[1] for pos in ladder_pos}

    def is_snake_head(self, new_pos):
        snake_head_pos = self._snake.get(new_pos)
        if snake_head_pos:
            return snake_head_pos
        return None

    def is_ladder_base(self, new_pos):
        ladder_base_pos = self._ladder.get(new_pos)
        if ladder_base_pos:
            return ladder_base_pos
        return None
