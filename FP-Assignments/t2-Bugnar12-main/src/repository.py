from src.domain import Player

class RepoException(Exception):
    pass


class MemoryRepo:
    def __init__(self):
        self.__players = {}

    def add_player(self, new_player : Player):
        """
        add player to repo
        :param new_player:
        :return:
        """
        if new_player.player_id in self.__players:
            raise RepoException("Player already exists!")
        self.__players[new_player.player_id] = new_player

    def get_player_by_id(self, id : int):
        """
        get player by id
        :param id:
        :return:
        """
        if id not in self.__players:
            raise RepoException("Player does not exist!")
        return self.__players[id]

    def get_all_players(self):
        """
        get all players.txt
        :return:
        """
        return list(self.__players.values())

    def __len__(self):
        return len(self.__players)

    def remove_by_id(self, id):
        """
        remove player by id
        :param id:
        :return:
        """
        if id not in self.__players:
            raise KeyError("Player does not exist!")
        del self.__players[id]

    def update_player(self, updated_player : Player):
        """
        update player
        :param updated_player:
        :return:
        """
        if updated_player.player_id not in self.__players:
            raise KeyError("Player does not exist!")
        self.__players[updated_player.player_id] = updated_player

class FileRepo(MemoryRepo):
    def __init__(self, file_name = "players.txt"):
        super(FileRepo, self).__init__()
        self.__file_name = file_name
        self.__load_file()

    def __load_file(self):
        """
        load file
        :return:
        """
        lines = []
        try:
            fin = open(self.__file_name, "rt")
            lines = fin.readlines()
            fin.close()
        except IOError:
            pass

        for line in lines :
            current_line = line.split(",")
            new_player = Player(int(current_line[0]), current_line[1], int(current_line[2]))
            super().add_player(new_player)

    def _save_file(self):
        fout = open(self.__file_name, "wt")
        for player in self.get_all_players():
            player_string = str(Player.player_id) + "," + str(Player.player_name) + "," + str(Player.player_strength)
            fout.write(player_string + "\n")

        fout.close()

    def add_player_file(self, new_player : Player):
        """
        add player to file
        :return:
        """
        super().add_player(new_player)
        self._save_file()

    def get_player_file(self, id : int):
        """
        get player from file
        :param id:
        :return:
        """
        return super().get_player_by_id(id)

    def get_all_players_file(self):
        """
        get all players.txt from file
        :return:
        """
        return super().get_all_players()

    def remove_player_file(self, id : int):
        """
        remove player from file
        :param id:
        :return:
        """
        super().remove_by_id(id)
        self._save_file()

    def update_player_file(self, updated_player : Player):
        """
        update player from file
        :param updated_player:
        :return:
        """
        super().update_player(updated_player)
        self._save_file()


