class Player:
    def __init__(self, id : int, name : str, strength : int):
        self.__id = id
        self.__name = name
        self.__strength = strength

    @property
    def player_id(self):
        return self.__id
    @property
    def player_name(self):
        return self.__name

    @property
    def player_strength(self):
        return self.__strength

    @player_name.setter
    def set_name(self, value):
        self.__name = value

    @player_strength.setter
    def set_strength(self, value):
        self.__strength = value

    @property
    def __str__(self):
        return str(self.__id) + "," + str(self.__name) + "," + str(self.__strength)
