from random import random, randint

from src.domain.grade import Grade
from src.repository.student_repo import Student_repo
from src.repository.discipline_repo import Discipline_repo

class Grade_repo:
    def __init__(self, student_repo : Student_repo, discipline_repo : Discipline_repo):
        self._grades = []
        self._student_repo = Student_repo()
        self._discipline_repo = Discipline_repo()

    def add_grade(self, grade : Grade):
        """
        Adds a grade to the list of grades
        :param grade:
        :return:
        """
        self._grades.append(grade)

    def get_all_grades(self):
        """
        Returns the list of grades
        :return:
        """
        return self._grades

    #add a grade to student and discipline

    def get_grades_by_student(self, student_id):
        """
        Returns a list of grades for a student
        :param student_id:
        :return:
        """
        list_of_grades_for_student = []
        list = self.get_all_grades()
        for grade in list:
            if grade.student_id_grade == student_id:
                list_of_grades_for_student.append(grade)

        return list_of_grades_for_student

    def get_grades_by_discipline(self, discipline_id):
        """
        Returns a list of grades for a discipline
        :param discipline_id:
        :return:
        """
        list_of_grades_for_discipline = []
        list = self.get_all_grades()
        for grade in list:
            if grade.discipline_id_grade == discipline_id:
                list_of_grades_for_discipline.append(grade)

        return list_of_grades_for_discipline

    def remove_by_student_id(self, student_id : int):
        """
        Removes a grade from the list of grades
        :param student_id:
        :return:
        """
        for grade in self._grades:
            if grade.student_id_grade == student_id:
                self._grades.remove(grade)

    def remove_by_discipline_id(self, discipline_id : int):
        """
        Removes a grade from the list of grades
        :param discipline_id:
        :return:
        """
        for grade in self._grades:
            if grade.discipline_id_grade == discipline_id:
                self._grades.remove(grade)

    def generate_random_grades(self, n : int):
        """
        Generates random grades
        :return:
        """
        for i in range(n):
            student_id = randint(1, 20)
            discipline_id = randint(1, 20)
            grade_value = randint(1, 10)
            grade = Grade(student_id, discipline_id, grade_value)
            self.add_grade(grade)