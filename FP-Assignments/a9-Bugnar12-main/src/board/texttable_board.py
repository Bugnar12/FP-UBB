from texttable import Texttable
from src.board.board import Board

class TextTable_board:
    def display_board(self, board):
        table = Texttable()
        table.add_rows([[""] + [chr(i) for i in range(ord('A'), ord('A')+10)]] +
                       [[i+1] + row for i, row in enumerate(board)])
        print(table.draw())

