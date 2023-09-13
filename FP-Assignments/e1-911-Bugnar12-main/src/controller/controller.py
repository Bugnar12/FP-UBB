from src.domain.movesymbol import MoveSymbol
from src.domain.table import Table
from src.domain.validator import MoveValidator


class TableService:

    def __init__(self, table: Table, move_validator: MoveValidator):
        self._table = table
        self._move_validator = move_validator

    def player_move(self, x_coord : int, y_coord : int, string):

        move = MoveSymbol(x_coord, y_coord, string)
        self._move_validator.validate(move, self._table)
        self._table.add_move(move)

    def computer_move(self):
        """
        the computer makes a move
        :return:
        """
        string = self.most_viewed_symbol()
        row, column = self.possible_move_indexes()
        computer_move = MoveSymbol(row, column, string)
        self._table.add_move(computer_move)


    def most_viewed_symbol(self):
        """
        returns the most common symbol
        :return:
        """
        x_count = 0
        o_count = 0

        for i in range(6):
            for j in range(6):
                if self._table.get_cell(i, j) == "X":
                    x_count += 1
                elif self._table.get_cell(i, j) == "O":
                    o_count += 1

        if x_count > o_count:
            return "O" # O is the most common symbol
        else:
            return "X" # X is the most common symbol


    def possible_move_indexes(self):
        """
        returns the indexes of the possible move
        :return:
        """

        for row in range(6):
            for col in range(6):
                if self._table.get_cell(row, col) == " ":
                    return row, col

    def get_table(self):
        return str(self._table)

    def check_win(self):
        """
        checks if there is a win
        :return:
        """
        if self.check_row():
            return True
        if self.check_column():
            return True
        if self.check_diagonals():
            return True
        else:
            return False

    def check_row(self):
        """
        checks if there is a win in a row
        :return:
        """

        for row in range(6):
            for col in range(1):
                if self._table.get_cell(row, col) != " " and self._table.get_cell(row, col) == self._table.get_cell(row, col + 1) == self._table.get_cell(row,col + 2) ==\
                   self._table.get_cell(row,col + 3) == self._table.get_cell(row,col + 4):
                    return True # if it is True then there is a win
        return False

    def check_column(self):
        """
        checks if there is a win in a column
        :return:
        """
        for column in range(6):
            for row in range(1):
                if self._table.get_cell(row, column) != " " and self._table.get_cell(row, column) == self._table.get_cell(row + 1, column)\
                   == self._table.get_cell(row + 2, column) ==\
                   self._table.get_cell(row + 3, column) == self._table.get_cell(row + 4, column):
                    return True # if it is True then there is a win
        return False # if it is False then there is no win

    def check_diagonals(self):
        """
        checks if there is a win in a diagonal
        :return:
        """

        for i in range(5, 3, - 1):
            for j in range(2):
                if self._table.get_cell(i, j) != " " and self._table.get_cell(i, j) ==\
                   self._table.get_cell(i - 1, j + 1) == self._table.get_cell(i - 2, j + 2) ==\
                   self._table.get_cell(i - 3, j + 3) == self._table.get_cell(i - 4, j + 4):
                    return True

        for i in range(5, 3, - 1):
            for j in range(5, 3, - 1):
                if self._table.get_cell(i, j) != " " and self._table.get_cell(i, j) ==\
                   self._table.get_cell(i - 1, j - 1) == self._table.get_cell(i - 2, j - 2) ==\
                   self._table.get_cell(i - 3, j - 3) == self._table.get_cell(i - 4, j - 4):
                    return True
        return False # if it is ok then the game is a draw

    def check_draw(self):
        """
        checks if there is a draw
        """
        for i in range(6):
            for j in range(6):
                if self._table.get_cell(i, j) == " ":
                    return False
        return True