class Discipline:
    """
    The discipline class domain has an id and a name
    """
    def __init__(self, discipline_id : int, discipline_name : str):
        self.__discipline_id = discipline_id
        self.__discipline_name = discipline_name

    @property #id getter
    def discipline_id(self):
        return self.__discipline_id

    @property #name getter
    def discipline_name(self):
        return self.__discipline_name

    @discipline_name.setter # name setter
    def set_discipline_name(self, value: str):
        self.__discipline_name = value

    #converting into string
    def __str__(self):
        return str(self.__discipline_id) + " -> " + str(self.discipline_name)