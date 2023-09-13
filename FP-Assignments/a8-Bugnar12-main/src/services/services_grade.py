"""
I have to assign a grade to a student for a discipline in this service module only using
the student repo and the discipline repo and the grade repo and their respective services

"""

from src.repository.discipline_repo import Discipline_repo
from src.repository.grade_repo import Grade_repo
from src.services.services_disciplines import Discipline_service
from src.services.services_student import Student_service
from src.repository.student_repo import Student_repo
from src.domain.grade import Grade
from src.validator.grade_validator import Grade_validator


class Grade_service:
    def __init__(self, grade_validator, grade_repo : Grade_repo, student_repo : Student_repo, discipline_repo : Discipline_repo):
        self._grade_validator = grade_validator
        self._grade_repo = grade_repo
        self._student_repo = student_repo
        self._discipline_repo = discipline_repo

    def add_grade(self, student_id : int, discipline_id : int, grade_value : int):

        student = self._student_repo.get(student_id)
        discipline = self._discipline_repo.get(discipline_id)


        grade = Grade(student.student_id, discipline.discipline_id, grade_value)

        self._grade_validator.validate_grade(grade)
        self._grade_repo.add_grade(grade)


    def display_student_grade(self, student_id : int):
        """
        I have to display the grades of a student
        :param student_id:
        :return:
        """
        list_of_grades = self._grade_repo.get_grades_by_student(student_id)
        return list_of_grades

    def display_all_grades(self):
        """
        I have to display all the grades
        :return:
        """
        new_list = []
        for g in self._grade_repo.get_all_grades():
            new_list.append(g)
        return new_list

    # def remove_grade(self, student_id : int):
    #     self._grade_repo.remove_grade(student_id)

    def generate_random_grades(self):
        self._grade_repo.generate_random_grades(20)

    def statistics_failing_students(self):
        """
        I have to create a list of students who have failed
        :return:
        """
        new_list = []
        for g in self._grade_repo.get_all_grades():
            if self.average_grade_for_student(g.student_id_grade) < 5:
                new_list.append(g)
        return new_list

    def average_grade_for_student(self, student_id : int):
        """
        I have to calculate the average grade for a student
        :param student_id:
        :return:
        """
        list_of_grades = self._grade_repo.get_grades_by_student(student_id)
        average_grade = 0
        for grade in list_of_grades:
            average_grade += grade.grade_value
        if len(list_of_grades) == 0:
            return 0
        average_grade /= len(list_of_grades)
        return average_grade

    def average_grade_student_per_discipline(self, discipline_id : int):
        """
        I have to calculate the average grade for a student for a discipline
        :return:
        """
        list_of_grades = self._grade_repo.get_grades_by_discipline(discipline_id)
        average_discipline_grade = 0
        for grade in list_of_grades:
            average_discipline_grade += grade.grade_value
        if len(list_of_grades) == 0:
            return 0
        average_discipline_grade /= len(list_of_grades)
        return average_discipline_grade


    def statistics_best_students(self):
        """
        I have to create a list of students who have the best grades
        :return:
        """

        list_of_students = self._student_repo.get_all_students()
        for student in list_of_students:
            grade = self.average_grade_for_student(student.student_id)
            student.average_grade = grade
        list_of_students = sorted(list_of_students, key=lambda x: x.average_grade, reverse=True)
        final_list = [
            list_of_students[0], list_of_students[1], list_of_students[2], list_of_students[3], list_of_students[4]
        ]
        return final_list


    def statistics_sorted_reverse(self):
        """
        I have to sort the grades in reverse order
        :return:
        """
        list_of_disciplines = self._discipline_repo.get_all_disciplines()
        for discipline in list_of_disciplines:
            grade = self.average_grade_student_per_discipline(discipline.discipline_id)
            discipline.average_grade = grade

        list_of_disciplines = sorted(list_of_disciplines, key=lambda x: x.average_grade, reverse=True)

        return list_of_disciplines

