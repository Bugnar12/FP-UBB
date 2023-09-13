from src.domain.student import Student
from src.exceptions.exceptions import RepoException
import random
from random import choice, randint


class Student_repo():
    """
    Here I will use the memory repo since it's the most convenient one,
    and the repo will represent the space where the list of students
    will be saved(memorized).

    The student repo will be represented as a dictionary that has only an id and a name
    """

    def __init__(self):
        self._students = {}

    def add(self, new_student : Student):
        """
        adding a student to the repo
        :param new_student:
        :return:
        """
        if new_student.student_id in self._students:
            raise RepoException("Student is already in repo")
        self._students[new_student.student_id] = new_student

    def get(self, id : int):
        """
        method for getting a student
        :param student:
        :return:A student from the repo
        """
        try:
            return self._students[id]
        except:
            raise RepoException("Student is not in repo")

    def get_all_students(self):
        """
        Gets all students from the repo
        :return: The repo
        """
        return list(self._students.values())

    def __len__(self):
        return len(self._students)

    def get_by_name(self, name : str):
        """
        This method returns a student by name
        :param name:
        :return:
        """

        list_of_students = []
        for s in self._students.values():
            if s.student_name == name:
                list_of_students.append(s)

        return list_of_students

    def get_by_first_name(self, first_name : str):
        """
        This method returns a student by first name
        :param first_name:
        :return:
        """
        list_of_students = []
        for s in self._students.values():
            if s.student_name.split()[0] == first_name:
                list_of_students.append(s)

        return list_of_students

    def get_by_last_name(self, last_name : str):
        """
        This method returns a student by last name
        :param last_name:
        :return:
        """
        list_of_students = []
        for s in self._students.values():
            if s.student_name.split()[1] == last_name:
                list_of_students.append(s)

        return list_of_students



    def update_student(self, updated_student : Student):
        """
        This method updates a student
        :param updated_student:
        :return:
        """
        if updated_student.student_id not in self._students:
            raise RepoException("Student is not in repo")
        self._students[updated_student.student_id] = updated_student

    def remove_by_id(self, removed_student : Student):
        if removed_student.student_id not in self._students:
            raise RepoException("The student can't be removed since he doesn't exist")
        del self._students[removed_student.student_id]

    def randomized_students(self, n : int):
        names = {
            "first_name" : ["John", "Paul", "George", "Ringo", "Pete", "Dave", "Roger", "Mick", "Keith", "Brian", "John"],
            "last_name" : ["Lennon", "McCartney", "Harrison", "Starr", "Townshend", "Gilmour", "Daltrey", "Jagger", "Richards", "Jones", "Lennon"]

        }
        for i in range (n):
            id = i
            name = choice(names["first_name"]) + " " + choice(names["last_name"])
            new_student = Student(id, name)
            Student_repo.add(self, new_student)



