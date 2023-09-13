import unittest

from src.controller.controller import TableService
from src.domain.table import Table
from src.domain.movesymbol import MoveSymbol
from src.domain.validator import MoveValidator



class Row(unittest.TestCase):

    def test_check_row(self):
        """
        Function to test if the row is valid
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        move = MoveSymbol(0, 0, "X")
        table_service.player_move(0, 0, "X")
        self.assertEqual(table.get_cell(0, 0), "X")

class Column(unittest.TestCase):

    def test_check_column(self):
        """
        Function to test if the column is valid
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        move = MoveSymbol(0, 0, "X")
        table_service.player_move(0, 0, "X")
        self.assertEqual(table.get_cell(0, 0), "X")

class Draw(unittest.TestCase):

    def test_check_draw(self):
        """
        Function to test if the game is a draw
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        move = MoveSymbol(0, 0, "X")
        table_service.player_move(0, 0, "X")
        self.assertEqual(table.get_cell(0, 0), "X")

class Diagonal(unittest.TestCase):

    def test_check_diagonal(self):
        """
        Function to test the diagonal
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        move = MoveSymbol(0, 0, "X")
        table_service.player_move(0, 0, "X")
        self.assertEqual(table.get_cell(0, 0), "X")

class Full_win(unittest.TestCase):

    def test_check_win(self):
        """
        checks if the player wins
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        move = MoveSymbol(0, 0, "X")
        table_service.player_move(0, 0, "X")
        self.assertEqual(table.get_cell(0, 0), "X")

    def test_check_computer_move(self):
        """
        checks if the computer makes a move
        :return:
        """
        table = Table()
        move_validator = MoveValidator()
        table_service = TableService(table, move_validator)
        table_service.computer_move()
        self.assertEqual(table.get_cell(0, 0), "O")


if __name__ == '__main__':
    unittest.main()


