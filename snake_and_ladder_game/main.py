import random
import threading


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


class Dice:
    MAX = 1
    MIN = 6

    @classmethod
    def roll(cls):
        return random.randint(cls.MAX, cls.MIN)


class Player:
    def __init__(self, name) -> None:
        self._name = name
        self._position = 0

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_position(self):
        return self._position

    def set_position(self, cur_pos):
        self._position = cur_pos


class Game:
    def __init__(self, players) -> None:
        self._players = [Player(each_player) for each_player in players]
        self._board = Board()
        # self._dice = Dice()
        self._current_player_index = 0

    def start(self):
        self._board.initialize_board()

        while not self.is_game_over():
            player = self._players[self._current_player_index]
            player_new_pos = player.get_position() + Dice.roll()

            print("player_name", player.get_name())
            print("roll-dice", player_new_pos - player.get_position())
            print("old-pos", player.get_position())
            print("new-pos", player_new_pos)

            if player_new_pos <= 100:
                snake_tail_pos = self._board.is_snake_head(player_new_pos)
                ladder_top_pos = self._board.is_ladder_base(player_new_pos)

                if snake_tail_pos:
                    player.set_position(snake_tail_pos)
                    print("snake bite from", player_new_pos, " to ", snake_tail_pos)
                elif ladder_top_pos:
                    player.set_position(ladder_top_pos)
                    print("ladder from", player_new_pos, " to ", ladder_top_pos)
                else:
                    player.set_position(player_new_pos)
                    print("no snake and ladder", player.get_position())

                if player.get_position() == 100:
                    print(f"====>>>>> {player.get_name()} WIN THE GAME !!!")
                    return

            self._current_player_index = (self._current_player_index + 1) % len(
                self._players
            )
            print("\n\n")

    def is_game_over(self):
        for each_player in self._players:
            if each_player.get_position() != 100:
                return False
        print("game over ")
        return True


class SnakeAndLadderGame:
    def run():
        group1 = ["player1", "player2", "player3"]
        game1 = Game(group1)

        threading.Thread(target=game1.start).start()

        group2 = ["p1", "p2"]
        game2 = Game(group2)
        threading.Thread(target=game2.start).start()


if __name__ == "__main__":
    SnakeAndLadderGame.run()
