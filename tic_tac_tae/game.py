from tic_tac_tae.board import Board


class Game:
    def __init__(self, players) -> None:
        self._players = players
        self._current_index = 0

    def start_game(self):
        board = Board(row=5, col=5, wining_length=4)

        # while board.is_board_full() and not board.check_winner(pos):
        while True:
            player = self._players[self._current_index]

            try:
                print("\n\nplayer-name: ", player.get_name())
                pos = int(input("Enter a position (1-9): "))

                board.make_move(pos, player)
                board.display()

                if board.check_winner(pos):
                    return f"{player.get_name()} WON THE GAME......"
                self._current_index = (self._current_index + 1) % len(self._players)

                if board.is_board_full():
                    return "MATCH DRAW..!!"
            except ValueError as err:
                print(err)
            except Exception as err:
                print(err)

        # return "MATCH DRAW..!!!"
