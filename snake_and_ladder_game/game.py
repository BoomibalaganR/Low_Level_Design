from snake_and_ladder_game.board import Board
from snake_and_ladder_game.dice import Dice
from snake_and_ladder_game.player import Player


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
