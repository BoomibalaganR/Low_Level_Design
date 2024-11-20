class Board:
    _ROW = 3
    _COL = 3

    def __init__(self, row=3, col=3, wining_length=3) -> None:
        self._row_size = row
        self._col_size = col
        self._board = [["_" for _ in range(col)] for _ in range(row)]
        self._pos_map = {}
        self._wining_length = wining_length
        self._total_move_count = 0
        self._board_size = self._row_size * self._col_size

        self._to_map_with_position()

    def _to_map_with_position(self):
        position = 1
        for row in range(self._row_size):
            for col in range(self._col_size):
                self._pos_map[position] = (row, col)
                position += 1
        print(self._pos_map)

    def display(self):
        print("\nBOARD")
        for row in self._board:
            for col in row:
                print(col, end=" ")
            print()

    def _are_consecutive_cells(self, cell1, cell2):
        return cell1 != "_" and cell1 is not None and cell1 == cell2

    def _has_row_winner(self, row):
        consecutive_count = 1
        for col in range(self._col_size - 1):
            current_cell = self._board[row][col]
            next_cell = self._board[row][col + 1]

            if not self._are_consecutive_cells(current_cell, next_cell):
                consecutive_count = 1
            else:
                consecutive_count += 1
            if consecutive_count == self._wining_length:
                return True
        return False

    def _has_col_winner(self, col):
        consecutive_count = 1
        for row in range(self._row_size - 1):
            current_cell = self._board[row][col]
            next_cell = self._board[row + 1][col]

            if not self._are_consecutive_cells(current_cell, next_cell):
                consecutive_count = 1
            else:
                consecutive_count += 1

            if consecutive_count == self._wining_length:
                return True
        return False

    def _has_left_diagonal(self, row, col):
        # Calculate the starting point for the left diagonal
        step = min(row, col)
        diagonal_start_row = row - step
        diagonal_start_col = col - step

        consecutive_count = 1

        while (
            diagonal_start_row < self._row_size - 1
            and diagonal_start_col < self._col_size - 1
        ):
            current_cell = self._board[diagonal_start_row][diagonal_start_col]
            next_cell = self._board[diagonal_start_row + 1][diagonal_start_col + 1]
            if not self._are_consecutive_cells(current_cell, next_cell):
                consecutive_count = 1
            else:
                consecutive_count += 1
            if consecutive_count == self._wining_length:
                return True

            # Move to the next diagonal position
            diagonal_start_row += 1
            diagonal_start_col += 1

        return False

    def _has_right_diagonal(self, row, col):
        # Calculate the starting point for the right diagonal
        step = min(row, (self._col_size - 1 - col))
        diagonal_start_row = row - step
        diagonal_start_col = col + step

        consecutive_count = 1

        # Ensure we are within bounds while checking diagonal
        while diagonal_start_row < self._row_size - 1 and diagonal_start_col > 0:
            current_cell = self._board[diagonal_start_row][diagonal_start_col]
            next_cell = self._board[diagonal_start_row + 1][diagonal_start_col - 1]

            if not self._are_consecutive_cells(current_cell, next_cell):
                consecutive_count = 1
            else:
                consecutive_count += 1

            if consecutive_count == self._wining_length:
                return True

            # Move to the next diagonal position
            diagonal_start_row += 1
            diagonal_start_col -= 1

        return False

    def check_winner(self, position):
        if self._total_move_count < 5:
            return False

        row, col = self._pos_map.get(position)  # type: ignore

        if self._has_row_winner(row):
            print("row winner...")
            return True

        if self._has_col_winner(col):
            print("col winner...")
            return True

        if self._has_left_diagonal(row, col):
            print("left diagonal winner...")
            return True

        if self._has_right_diagonal(row, col):
            print("right diagonal winner...")
            return True
        return False

    # def check_winner(self):
    #     if self.cell_count < 5:
    #         return False

    #     # row wise

    #     for row in range(Board._ROW):
    #         if (
    #             self._board[row][0] != "_"
    #             and self._board[row][0] == self._board[row][1] == self._board[row][2]
    #         ):
    #             return True

    #     # col wise:
    #     for col in range(Board._COL):
    #         if (
    #             self._board[0][col] != "_"
    #             and self._board[0][col] == self._board[1][col] == self._board[2][col]
    #         ):
    #             return True

    #     # left-diagonol wise:

    #     if (
    #         self._board[0][0] != "_"
    #         and self._board[0][0] == self._board[0][1] == self._board[0][2]
    #     ):
    #         return True

    #     # righ-diagonal wise:
    #     if (
    #         self._board[0][2] != "_"
    #         and self._board[0][2] == self._board[1][1] == self._board[2][0]
    #     ):
    #         return True

    def is_board_full(self):
        return self._total_move_count == self._board_size

    def make_move(self, pos, player):
        if pos <= 0 or pos > self._board_size:
            raise ValueError("invalid position..!!")

        position = self._pos_map[pos]
        if self._board[position[0]][position[1]] != "_":
            raise Exception("Already fill these position, enter another position")

        self._board[position[0]][position[1]] = player.get_symbol()
        self._total_move_count += 1
