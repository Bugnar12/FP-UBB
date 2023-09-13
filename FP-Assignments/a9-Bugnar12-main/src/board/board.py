#Implementing the board for battleships

from src.domain.cell import Cell
from src.domain.ship import Ship
from texttable import Texttable

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]

    def play(self, move, board):
        """
        :param move: a string representing a move
        :param board: a list of lists representing the board
        :return: a tuple (hit, win)
        :raises: ValueError if the move is invalid
        The function returns a tuple (hit, win) where hit is True if the move was a hit and False otherwise
        :param move:
        :param board:
        :return:
        """
        x = int(move[1]) - 1
        y = ord(move[0]) - ord('A')  # ord('A') = 65
        win = False
        if board[x][y] == 'S':
            board[x][y] = 'H'
            win = self._check_win(board)
            return "hit", x, y, win
        else:
            board[x][y] = 'M'
            return "miss", x, y, win

    def _parse_move(self, move):
        """
        :param move: a string representing a move
        :return: a tuple (x, y) representing the move
        :raises: ValueError if the move is invalid
        :param move:
        :return:
        """
        x = int(move[1]) - 1
        y = ord(move[0]) - ord('A')  # ord('A') = 65
        return x, y

    def _check_win(self, board):
        """
        :param board: a list of lists representing the board
        :return: True if the game is won and False otherwise
        :param board:
        :return:
        """
        for row in board:
            if "S" in row:
                return False
        return True










