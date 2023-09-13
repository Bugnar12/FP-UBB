from src.domain.ship import Ship
import random

class Computer:
    def __init__(self):
        self.board = [[' ' for _ in range(10)] for _ in range(10)]
        self.ships = [Ship(5), Ship(3), Ship(3), Ship(2), Ship(2)]

    def place_ships(self):
        for ship in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.choice(["up", "down", "left", "right"])
                if self._check_place(x, y, direction, ship.size, self.board):
                    self._place(x, y, direction, ship.size, self.board)
                    break

    def _check_place(self, x, y, direction, size, board):
        if direction == "up":
            for i in range(size):
                if x - i < 0:
                    return False
                if board[x - i][y] != ' ':
                    return False
        elif direction == "down":
            for i in range(size):
                if x + i > 9:
                    return False
                if board[x + i][y] != ' ':
                    return False
        elif direction == "left":
            for i in range(size):
                if y - i < 0:
                    return False
                if board[x][y - i] != ' ':
                    return False
        elif direction == "right":
            for i in range(size):
                if y + i > 9:
                    return False
                if board[x][y + i] != ' ':
                    return False
        return True

    def _place(self, x, y, direction, size, board):
        if direction == "up":
            for i in range(size):
                board[x-i][y] = "S"
        elif direction == "down":
            for i in range(size):
                board[x+i][y] = "S"
        elif direction == "left":
            for i in range(size):
                board[x][y-i] = "S"
        elif direction == "right":
            for i in range(size):
                board[x][y+i] = "S"

    def get_move(self):
        while True:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            move = chr(x + ord('A')) + str(y + 1)
            if self.board[x][y] == ' ':
                return move

    def check_win(self):
        for row in self.board:
            for cell in row:
                if cell == "S":
                    return False
        return True

    def __str__(self):
        return "Computer"

    #implement a function that hides the ships from the player

    def hidden_board(self):
        hidden_board = [[' ' for _ in range(10)] for _ in range(10)]
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == "S":
                    hidden_board[i][j] = " "
                else:
                    hidden_board[i][j] = self.board[i][j]
        return hidden_board

