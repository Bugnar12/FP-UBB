class Student:
    """
    All stundets must have a unique ID(integer) and a name(string)
    """
    def __init__(self, student_id : int, student_name : str):
        self.__student_id = student_id
        self.__student_name = student_name

    #implementation of setters and geters for the student class domain

    @property #getter for id
    def student_id(self):
        return self.__student_id

    @property #getter for name
    def student_name(self):
        return self.__student_name

    @student_name.setter #setter for name
    def set_student_name(self, value : str):
        self.__student_name = value

    def __str__(self): #converting into string
        return str(self.__student_id) + " : " + str(self.__student_name)






