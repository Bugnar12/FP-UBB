from src.controller.controller import TableService

class UserInterface:

    def __init__(self, table_service: TableService):
        self.table_service = table_service

    def run_game(self):
        """
        the main function of the game
        Here the game gets executed
        :return:
        """
        while True:

            print("Welcome to the game!")
            print("\n")
            print("The game is played on a 3x3 grid.")
            print("The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
            print("When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")

            print(str(self.table_service.get_table()))
            self._handle_player_move()
            print(str(self.table_service.get_table()))
            if self.table_service.check_draw():
                print("The forces of chaos have gained the victory !!!")
                print("\n")
                return

            if self.table_service.check_win():
                print("The forces of chaos have gained the victory !!!")
                print("\n")
                return
            print("")
            print("The computer is going to play next : ")
            self._handle_computer_move()

            if self.table_service.check_draw():
                print("The forces of chaos have gained the victory !!!")
                return
            if self.table_service.check_win():
                print("The forces of order have gained the victory !!!")
                return

    def _handle_player_move(self):
        """
        the player makes a move
        :return:
        """

        while True:
            try:


                params = input("The format of the input is : line,column,symbol\n")

                row = int(params[0]) - 1 # we have to subtract 1 because the user will input the line number starting from 1
                column = int(params[1]) - 1 # we have to subtract 1 because the user will input the column number starting from 1
                string1 = params[2]



                self.table_service.player_move(row, column, string1)

                return

            except Exception as ex:
                print(ex)

    def _handle_computer_move(self):
        """
        the computer makes a move
        :return:
        """
        self.table_service.computer_move()
