import random

from src.board.texttable_board import TextTable_board
from src.player.player import Player
from src.board.board import Board
from src.player.computer import Computer

"""
Explaining the game and how I created it:
The game is a simple battleship game. The game is played on a 10x10 grid. The player has 5 ships of different sizes. The player
places the ships on the grid. The computer places the ships on the grid. The player and the computer take turns to shoot at
each other's ships. The player who sinks all the other player's ships wins the game. The game ends when one of the players
sinks all the other player's ships.

I created the game by creating a class called BattleshipGame. The class has 3 attributes: player, computer and board. The
player and computer are instances of the Player and Computer classes. The board is an instance of the Board class. The
BattleshipGame class has 3 methods: play, _place_ships and _play_turn.
"""


class BattleshipGame:
    def __init__(self):
        """
        Initialize the game
        """
        self.player = Player()
        self.computer = Computer()
        self.board = Board()
        self.table = TextTable_board()

    def play(self):
        #place the ships
        self.player.place_ships()
        self.computer.place_ships()

        #display the board
        self.table.display_board(self.player.board)
        self.table.display_board(self.computer.hidden_board())

        while True:
            #get the move of the player

            move = input("Enter your move (e.g. A5): ")
            if not self._validate_move(move):
                print("Invalid move, please enter a move in the format A5")
                continue

            result, x, y, win = self.board.play(move, self.computer.board)

            #display the result of the move
            if result == "hit":
                print("Hit!")
                self.computer.board[x][y] = 'H'
                self.computer.hidden_board()[x][y] = 'H'
                if win:
                    print("You win!")
                    break
            elif result == "miss":
                print("Miss!")
                self.computer.board[x][y] = 'M'
                self.computer.hidden_board()[x][y] = 'M'

            #here display the board of the computer after the move of the player
            self.table.display_board(self.computer.hidden_board())

            #get the move of the computer
            move = self.computer.get_move()
            print()

            result, x, y, win = self.board.play(move, self.player.board)
            #analyze the result of the move
            if result == "hit":
                print("Computer Hit your ship!")
                self.player.board[x][y] = 'H'

                if win:
                    print("Computer wins!")
                    break

            elif result == "miss":
                print("Computer Missed!")
                self.player.board[x][y] = 'M'

            #here display the board of the player after the move of the computer
            self.table.display_board(self.player.board)


    def _validate_move(self, move):
        if len(move) != 2:
            return False
        if move[0] not in "ABCDEFGHIJ":
            return False
        if not move[1].isnumeric() or int(move[1]) < 1 or int(move[1]) > 10:
            return False
        return True


if __name__ == "__main__":
    game = BattleshipGame()
    game.play()