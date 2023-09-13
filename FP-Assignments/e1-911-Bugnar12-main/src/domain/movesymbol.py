class MoveSymbol():
    """
    the domain class for the move symbol
    """

    def __init__(self, row : int, column : int, string : str):
        """
        :param x:
        :param y:
        :param string:
        """
        self.__y = column
        self.__x = row
        self.__string = string

    @property
    def get_x(self):
        """
        getter
        :return:
        """
        return self.__x

    @property
    def get_y(self):
        """
        getter
        :return:
        """
        return self.__y

    @property
    def string(self):
        """
        getter
        :return:
        """
        return self.__string

