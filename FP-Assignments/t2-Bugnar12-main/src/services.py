from src.repository import FileRepo

class Services:
    def __init__(self, filerepo : FileRepo):
        self.Memory = FileRepo()

    def sort_players_by_descending_strength(self):
        """
        sort players.txt by descending strength
        :return:
        """
        players = self.Memory.get_all_players_file()
        players.sort(key=lambda x: x.player_strength, reverse=True)
        return players

    def display_players(self):
        """
        display players.txt
        :return:
        """
        new_list = []
        for p in self.Memory.get_all_players_file():
            new_list.append(p)
        return new_list

    def make_pairs(self):
        """
        make pairs of 2 random players
        :return:
        """
        players = self.Memory.get_all_players()
        players.sort(key=lambda x: x.player_strength, reverse=True)
        pairs = []
        for i in range (len(players) // 2):
            pairs.append((players[i], players[len(players) - i - 1]))
        return pairs

    def make_pairs_play(self):
        """
        make pairs of 2 random players
        :return:
        """
        list = self.make_pairs()
        for pair in list:
            if pair[0].player_strength > pair[1].player_strength:
                self.Memory.remove_by_id(pair[1].player_id)
            else:
                self.Memory.remove_by_id(pair[0].player_id)

    def eliminate_players(self):
        players = self.Memory.get_all_players()
        players.sort(key=lambda x: x.player_strength, reverse=False)
        for i in range(0, 5):
            self.Memory.remove_by_id(players[i].player_id)

    def play_qualifying_round(self):
        while len(self.Memory) > 4:
            self.make_pairs_play()
        return self.Memory.get_all_players()[0]

    def play_quarterfinals(self):
        for i in range(0, 2):
            self.make_pairs_play()
        self.display_players()
        self.make_pairs()


    def play_semifinals(self):
        self.make_pairs_play()
        self.make_pairs_play()
        self.display_players()

    def play_finals(self):
        self.make_pairs_play()
        self.display_players()

    def winner(self):
        self.make_pairs_play()
        return self.Memory.get_all_players()[0]

