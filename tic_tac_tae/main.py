import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tic_tac_tae.game import Game
from tic_tac_tae.player import Player


class Tic_tac_tae:
    @staticmethod
    def run():
        p1 = Player("boomi", "X")
        p2 = Player("dhinesh", "O")

        game1 = Game([p1, p2])
        result = game1.start_game()

        print(result)


if __name__ == "__main__":
    Tic_tac_tae.run()
