from src.domain.table import Table
from src.domain.movesymbol import MoveSymbol


class MoveValidator:

    def validate(self, move: MoveSymbol, table: Table):
        """
        Function to validate if a move is valid for the user input at the functionality 3

        :param move:
        :param table:
        :return:
        """
        erori = ""
        if move.get_x < 0 or move.get_x > 5:
            erori += "The row index is not valid!\n"
        if move.get_y < 0 or move.get_y > 5:
            erori += "The column index is not valid!\n"
        if move.string != "0" and move.string != "X":
            erori += "The specified character is not valid.\n"
        if erori != "":
            raise ValueError(erori)
