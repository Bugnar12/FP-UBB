import copy

from collections import deque

from src.domain.student import Student
from src.errors.erori import ServiceException
from src.repository.student_repo import student_repo
from src.repository import student_repo


class Service:
    def __init__(self, validator, repo):
        self.__validator = validator
        self.__repo = repo
        self.undo_stack = deque()

    def generate_random(self):
        self.__repo.generate_randomized(10)

    def add_student(self, student_id, name, group):
        new_student = Student(student_id, name, group)
        self.undo_stack.append(("add", new_student))
        self.__validator.validate(new_student)
        self.__repo.add(new_student)


    def delete(self, student_id : int):
        self.__repo.remove_by_id(student_id)

    def display_all_students(self):
        return self.__repo.get_all_students()

    def filter(self, given_group : int):
        array = self.__repo.get_all_students()
        for student in array:
            if student.group == given_group:
                self.undo_stack.append(("filter", student))
                self.__repo.remove_by_id(student)

    def undo(self):
        if self.undo_stack:
            operation, data = self.undo_stack.pop()
            if operation == "add":
                self.__repo.remove_by_id(data)
            if operation == "filter":
                self.__repo.add(data)







