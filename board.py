"""Module for creating game board"""


from arrays import Array2D
from btree import LinkedBST
import random


class Board:
    """ Represents game board """
    def __init__(self):
        self.game_board = Array2D(3, 3)

    def __setitem__(self, key, value):
        assert value == 'X' or value == 'O'
        self.game_board[key[0], key[1]] = value

    def filled_cells(self):
        filled = 0
        for i in range(self.game_board.num_rows()):
            for j in range(self.game_board.num_cols()):
                if self.game_board[i, j] is not None:
                    filled += 1
        return filled

    def check_condition(self):
        if self._check_horizontal() == 1 or self._check_vertical() == 1 or \
                self._check_diagonals() == 1:
            return 1
        if self._check_horizontal() == -1 or self._check_vertical() == -1 or \
                self._check_diagonals() == -1:
            return -1
        return 0

    def _check_horizontal(self):
        for i in range(self.game_board.num_rows()):
            if self.game_board[i, 0] == self.game_board[i, 1] == self.game_board[i, 2]:
                if self.game_board[i, 1] == 'O':
                    return 1
                return -1
        return 0

    def _check_vertical(self):
        for j in range(self.game_board.num_cols()):
            if self.game_board[0, j] == self.game_board[1, j] == self.game_board[2, j]:
                if self.game_board[0, j] == 'O':
                    return 1
                return -1
        return 0

    def _check_diagonals(self):
        if self.game_board[0, 0] == self.game_board[1, 1] == self.game_board[2, 2]:
            if self.game_board[0, 0] == 'O':
                return 1
            return -1

        if self.game_board[2, 0] == self.game_board[1, 1] == self.game_board[0, 2]:
            if self.game_board[0, 0] == 'O':
                return 1
            return -1

        return 0

    def create_tree(self):
        pass

    def create_board(self, player):
        free_cells = self.get_free_cells()
        filled_cells = self.get_filled_cells()
        new_board = Board()
        for element in filled_cells:
            new_board[element[0], element[1]] = element[2]

        random_cell = random.choice(free_cells)

        if player == "COMP":
            element = 'O'
        elif player == "PERSON":
            element = 'X'
        new_board[random_cell[0], random_cell[1]] = element
        return new_board

    def get_free_cells(self):
        free_cells = []
        for i in range(self.game_board.num_rows()):
            for j in range(self.game_board.num_cols()):
                if self.game_board[i, j] is None:
                    free_cells.append((i, j))
        return free_cells

    def get_filled_cells(self):
        filled_cells = []
        for i in range(self.game_board.num_rows()):
            for j in range(self.game_board.num_cols()):
                if self.game_board[i, j] is not None:
                    filled_cells.append((i, j, self.game_board[i, j]))
        return filled_cells

    def __str__(self):
        result = ''
        for i in range(self.game_board.num_rows()):
            for j in range(self.game_board.num_cols()):
                result += '{} '.format(self.game_board[i, j])
            result += '\n'
        return result
