class Student:
    """
    Add a new student to the already existing list of students.
    Each student must have :
    - a unique id ( integer )
    - a valid name ( string )
    - a group they are taking part of ( integer )
    """

    def __init__(self, student_id : int, name : str, group : int):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    #setters and getters

    @property
    def student_id(self):
        return self.__student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_value):
        self.__name = new_value

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, new_value):
        self.__group = new_value

    def __str__(self):
        return str(self.student_id) + " -> " + self.name + " - " + str(self.group)


def test_student():
    """
    testing function with asserts
    :return:
    """

    #create a student

    new_student = Student(124, "Marian Gabriel", 913)
    assert new_student.student_id == 124
    assert new_student.name == "Marian Gabriel"
    assert new_student.group == 913
    assert str(new_student) == "124 -> Marian Gabriel - 913"

    #rename a student :)

    new_student.name = "Gabriel Boca"
    assert new_student.name == "Gabriel Boca"
    assert str(new_student) == "124 -> Gabriel Boca - 913"

if __name__ == "__main__":
    test_student()





