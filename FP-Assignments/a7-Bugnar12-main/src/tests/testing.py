from src.repository.student_repo import student_repo
from src.domain.student import Student
from src.services.services import Service

import unittest

class Testing:
    def __init__(self, repo, validator, service):
        self.__repo = repo
        self.__validator = validator
        self.__service = service

    def test_student(self):
        """
        Testing the function add with asserts
        :return:
        """
        # self.__new_student = Student(1234, "Marian Aurel", 912)
        student_list = []
        student_list = self.__repo.get_all_students()
        student_list.append(self.__service.add_student(1234, "George", 915))
        self.assertEqual(student_list[0].id == 1234)
        self.assertEqual(student_list[0].name == "George")
        self.assertEqual(student_list[0].group == 915)

     #   assert str(self.__new_student) == "1234 -> Marian Aurel - 912"

    def run_tests(self):
        self.test_student()

