from src.services import Services
from src.domain import Player

class UI:
    def __init__(self, services : Services):
        self.services = services
        self.__commands = {
            'display_players': self.__display_players,
            'sort_players': self.__sort_players,
            'make_pairs': self.__make_pairs,
            'play_qualifying' : self.__play_qualifying,
            'play_quarterfinals' : self.__play_quarterfinals,
            'play_semifinals' : self.__play_semifinals,
            'play_finals' : self.__play_finals,
            'winner' : self.__winner

        }

    def __display_players(self, params):
        """
        display players.txt
        :return:
        """
        if len(params) != 0:
            print("Invalid command")
            return
        players = self.services.display_players()
        for player in players:
            print(str(player.player_id) + "," + player.player_name + "," + str(player.player_strength))

    def __sort_players(self, params):
        """
        sort players.txt by descending strength
        :return:
        """
        if len(params) != 0:
            print("invalid")
            return
        players = self.services.sort_players_by_descending_strength()
        for player in players:
            print(str(player.player_id) + "," + player.player_name + "," + str(player.player_strength))

    def __make_pairs(self, params):
        """
        make pairs
        :return:
        """
        if len(params) != 0:
            print("invalid")
            return
        pairs = self.services.make_pairs()
        for pair in pairs:
            print(str(pair[0].player_id) + "," + pair[0].player_name + "," + str(pair[0].player_strength) + " vs " + str(pair[1].player_id) + "," + pair[1].player_name + "," + str(pair[1].player_strength))

    def __play_qualifying(self, params):
        """
        eliminate players
        :return:
        """
        if len(params) != 0:
            print("invalid")
            return
        self.services.eliminate_players()
        players = self.services.display_players()
        for player in players:
            print(str(player.player_id) + "," + player.player_name + "," + str(player.player_strength))

        print("Congratulations! You have qualified for the quarterfinals!")

    def __play_quarterfinals(self, params):
        if len(params) != 0:
            print("invalid")
            return
        print("Quarterfinals")
        print(self.services.play_quarterfinals())

    def __play_semifinals(self, params):
        if len(params) != 0:
            print("invalid")
            return
        print("Semifinals")
        print(self.services.play_semifinals())

    def __play_finals(self, params):
        if len(params) != 0:
            print("invalid")
            return
        print("Finals")
        print(self.services.play_finals())

    def __winner(self, params):
        if len(params) != 0:
            print("invalid")
            return
        print("the winner is : ")
        winner = self.services.winner()
        print(str(winner.player_id) + "," + winner.player_name + "," + str(winner.player_strength))


    def printings(self):
        print("Available commands:")
        print("1.display_players")
        print("2.sort_players")
        print("3.make_pairs")
        print("4.play_qualifying")
        print("5.play_quarterfinals")
        print("6.play_semifinals")
        print("7.play_finals")
        print("8.winner")

    def run(self):
        self.printings()
        while True:
            command = input(">>")
            command = command.strip()
            if command == "":
                continue
            if command == "exit":
                print("Goodbye!")
                return
            parts = command.split()
            command_name = parts[0]
            self.__params = parts[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](self.__params)
                except ValueError as ve:
                    print(ve)

            else:
                print("Invalid command")

