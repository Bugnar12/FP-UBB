import unittest

from src.board.board import Board
from src.board.texttable_board import TextTable_board
from src.domain.ship import Ship
from src.game.game import BattleshipGame
from src.player.computer import Computer
from src.player.player import Player



class test_board(unittest.TestCase):
    def set_up(self):
        self.board = Board()
        self.board_play = [[' ' for _ in range(10)] for _ in range(10)]

    def test_play(self):
        self.set_up()
        self.assertEqual(self.board.play("A1", self.board.board), ("miss", 0, 0, False))
        self.assertEqual(self.board.play("A2", self.board.board), ("miss", 1, 0, False))
        self.assertEqual(self.board.play("A3", self.board.board), ("miss", 2, 0, False))
        self.assertEqual(self.board.play("A4", self.board.board), ("miss", 3, 0, False))
        self.assertEqual(self.board.play("A5", self.board.board), ("miss", 4, 0, False))
        self.assertEqual(self.board.play("A6", self.board.board), ("miss", 5, 0, False))
        self.assertEqual(self.board.play("A7", self.board.board), ("miss", 6, 0, False))
        self.assertEqual(self.board.play("A8", self.board.board), ("miss", 7, 0, False))
        self.assertEqual(self.board.play("A9", self.board.board), ("miss", 8, 0, False))
        self.assertEqual(self.board.play("B1", self.board.board), ("miss", 0, 1, False))
        self.assertEqual(self.board.play("B2", self.board.board), ("miss", 1, 1, False))
        self.assertEqual(self.board.play("B3", self.board.board), ("miss", 2, 1, False))
        self.assertEqual(self.board.play("B4", self.board.board), ("miss", 3, 1, False))
        self.assertEqual(self.board.play("B5", self.board.board), ("miss", 4, 1, False))
        self.assertEqual(self.board.play("B6", self.board.board), ("miss", 5, 1, False))
        self.assertEqual(self.board.play("B7", self.board.board), ("miss", 6, 1, False))
        self.assertEqual(self.board.play("B8", self.board.board), ("miss", 7, 1, False))
        self.assertEqual(self.board.play("B9", self.board.board), ("miss", 8, 1, False))

        self.board_play[3][3] = 'S'
        self.assertEqual(self.board.play("D4", self.board_play), ("hit", 3, 3, True))

    def test_parse_move(self):
        self.set_up()
        self.assertEqual(self.board._parse_move("A1"), (0, 0))
        self.assertEqual(self.board._parse_move("A2"), (1, 0))
        self.assertEqual(self.board._parse_move("A3"), (2, 0))
        self.assertEqual(self.board._parse_move("A4"), (3, 0))
        self.assertEqual(self.board._parse_move("A5"), (4, 0))
        self.assertEqual(self.board._parse_move("A6"), (5, 0))
        self.assertEqual(self.board._parse_move("A7"), (6, 0))
        self.assertEqual(self.board._parse_move("A8"), (7, 0))
        self.assertEqual(self.board._parse_move("A9"), (8, 0))
        self.assertEqual(self.board._parse_move("B1"), (0, 1))
        self.assertEqual(self.board._parse_move("B2"), (1, 1))
        self.assertEqual(self.board._parse_move("B3"), (2, 1))
        self.assertEqual(self.board._parse_move("B4"), (3, 1))
        self.assertEqual(self.board._parse_move("B5"), (4, 1))
        self.assertEqual(self.board._parse_move("B6"), (5, 1))
        self.assertEqual(self.board._parse_move("B7"), (6, 1))
        self.assertEqual(self.board._parse_move("B8"), (7, 1))
        self.assertEqual(self.board._parse_move("B9"), (8, 1))

    def test_check_win(self):
        self.set_up()
        self.assertEqual(self.board._check_win(self.board_play), True)
        self.board_play[4][4] = 'S'
        self.assertEqual(self.board._check_win(self.board_play), False)

class test_texttable_board(unittest.TestCase):
    def set_up(self):
        self.board = TextTable_board()

    def test_display_board(self):
        board = [[' ' for _ in range(10)] for _ in range(10)]
        self.set_up()
        self.assertEqual(self.board.display_board(board), None)

class test_ship(unittest.TestCase):
    def test_ships(self):
        self.ship = Ship(4)
        self.assertEqual(self.ship.size, 4)

class test_computer(unittest.TestCase):
    def set_up(self):
        self.computer = Computer()
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = [Ship(5), Ship(3), Ship(3), Ship(2), Ship(2)]

    def test_get_move(self):
        self.set_up()
        self.assertEqual(self.computer.get_move(), 'A1')

    def test_place_ships(self):
        self.set_up()
        self.assertEqual(self.computer.place_ships(), None)

    def test_check_place(self):
        self.set_up()
        self.assertEqual(self.computer._check_place(0, 0, "up", 3, self.board), False)
        self.assertEqual(self.computer._check_place(0, 0, "down", 3, self.board), True)
        self.assertEqual(self.computer._check_place(9,9 , "down", 3, self.board), False)
        self.assertEqual(self.computer._check_place(0, 0, "left", 3, self.board), False)
        self.assertEqual(self.computer._check_place(0, 0, "right", 3, self.board), True)
        self.assertEqual(self.computer._check_place(9, 9, "right", 3, self.board), False)
        self.board[9][9] = 'S'

    def test_place_ship(self):
        self.set_up()
        self.assertEqual(self.computer._place(0, 0, "up", 3, self.board), None)
        self.assertEqual(self.computer._place(0, 0, "down", 3, self.board), None)
        self.assertEqual(self.computer._place(0, 0, "left", 3, self.board), None)
        self.assertEqual(self.computer._place(0, 0, "right", 3, self.board), None)

    def test_check_win(self):
        self.set_up()
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.board[3][3] = 'S'
        self.assertEqual(self.computer.check_win(), True)
        self.board[4][4] = 'S'
        self.assertEqual(self.computer.check_win(), True)

    def test_str(self):
        self.set_up()
        self.assertEqual(self.computer.__str__(), "Computer")

    def test_hidden_board(self):
        self.set_up()
        create_board = [[' ' for _ in range(10)] for _ in range(10)]
        self.assertEqual(self.computer.hidden_board(), create_board)

class test_player(unittest.TestCase):
    def set_up(self):
        self.player = Player()
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = [Ship(5), Ship(3), Ship(3), Ship(2), Ship(2)]

    def test_get_move(self):
        self.set_up()
        self.assertEqual(self.player.get_move(), 'A1')

    def test_place_ships(self):
        self.set_up()
        self.assertEqual(self.player.place_ships(), None)

    def test_check_place(self):
        self.set_up()
        self.assertEqual(self.player._check_place(0, 0, "up", 3, self.board), False)
        self.assertEqual(self.player._check_place(0, 0, "down", 3, self.board), True)
        self.assertEqual(self.player._check_place(9,9 , "down", 3, self.board), False)
        self.assertEqual(self.player._check_place(0, 0, "left", 3, self.board), False)
        self.assertEqual(self.player._check_place(0, 0, "right", 3, self.board), True)
        self.assertEqual(self.player._check_place(9, 9, "right", 3, self.board), False)
        self.board[9][9] = 'S'

    def test_place_ship(self):
        self.set_up()
        self.assertEqual(self.player._place(0, 0, "up", 3, self.board), None)
        self.assertEqual(self.player._place(0, 0, "down", 3, self.board), None)
        self.assertEqual(self.player._place(0, 0, "left", 3, self.board), None)
        self.assertEqual(self.player._place(0, 0, "right", 3, self.board), None)

    def test_check_win(self):
        self.set_up()
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.board[3][3] = 'S'
        self.assertEqual(self.player.check_win(), True)
        self.board[4][4] = 'S'
        self.assertEqual(self.player.check_win(), True)

    def test_str(self):
        self.set_up()
        self.assertEqual(self.player.__str__(), "Player")


if __name__ == '__main__':
    unittest.main()
