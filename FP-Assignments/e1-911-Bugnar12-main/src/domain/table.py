import texttable
from src.domain.movesymbol import MoveSymbol

class Table:
    """
    This is the Table class
    """

    def __init__(self):
        """
        the constructor for the table
        here we initialize the table

        """
        self.table = [[" ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " "],
                      [" ", " ", " ", " ", " ", " "]]

    def table(self):
        """
        returns the table
        :return:
        """
        return self.table

    def add_move(self, move: MoveSymbol):
        self.table[move.get_x][move.get_y] = move.string






    def get_cell(self, x, y):
        """
        getter for the cell
        :param x:
        :param y:
        :return:
        """
        return self.table[x][y]




    def __repr__(self):
        """
        returns the string representation using texttable module
        :return:
        """

        table = texttable.Texttable()
        for row in range(3 + 3):
            table.add_row(self.table[row])
        return table.draw()
