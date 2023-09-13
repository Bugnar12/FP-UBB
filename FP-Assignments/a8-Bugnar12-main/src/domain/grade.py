from src.domain.discipline import Discipline
from src.domain.student import Student


class Grade:
    """
    Class domain for the grade of a student which must contain the student id, discipline id and the grade value
    """
    def __init__(self, student_id : int, discipline_id : int, grade_value : int):
        self.__grade_student_id = student_id
        self.__grade_discipline_id = discipline_id
        self.__grade_value = grade_value

    @property # getter for id
    def student_id_grade(self):
        return self.__grade_student_id

    @property #getter for name
    def discipline_id_grade(self):
        return self.__grade_discipline_id

    @property #getter for grade value
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter #setter for the grade value
    def set_grade_value(self, value : str):
        self.__grade_value = value

    def __str__(self):
        return "Student_id : " + str(self.__grade_student_id) + " -> Discipline_id : " + str(self.__grade_discipline_id) + " Grade value : " + str(self.__grade_value)

