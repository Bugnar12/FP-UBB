from src.domain.student import Student
from src.repository.grade_repo import Grade_repo
from src.repository.student_repo import Student_repo
from src.validator.student_validator import Student_validator


class Student_service():
    def __init__(self, validator, student_repo : Student_repo, grade_repo : Grade_repo):
        self._validator = validator
        self._student_repo = student_repo
        self._grade_repo = grade_repo

    def generate_random_students(self):
        """
        generating 20 random students with id and name
        :return:
        """
        self._student_repo.randomized_students(20)

    def add_student(self, id : int, name : str):
        """
        adding a student to the repo while being given its id and name
        :param id:
        :param name:
        :return:
        """
        new_student = Student(id, name)
        self._validator.validate_student(new_student)
        self._student_repo.add(new_student)

    def remove_student(self, id : int):
        """
        Removing a student from the repo
        :param id:
        :return:
        """
        # 1.We search the student that we want to remove by the id
        student = self._student_repo.get(id)

        self._student_repo.remove_by_id(student)
        self._grade_repo.remove_by_student_id(student.student_id)

    def update_student_name(self, id_stud: int, new_name: str):
        """
        Updating a student
        :param id:
        :param new_name:
        :return:
        """
        updated_student = Student(id_stud, new_name)
        self._student_repo.update_student(updated_student)

    def display_students(self):
        """
        Displaying all students
        :return:
        """
        new_list = []
        for s in self._student_repo.get_all_students():
            new_list.append(s.__str__())
        return new_list

    def search_student_by_id(self, id):
        """
        Searching a student by id
        :param id:
        :return:
        """
        return self._student_repo.get(id)

    def search_student_by_name(self, name):
        """
        Searching a student by name
        :param name:
        :return:
        """
        new_list = []
        list = self._student_repo.get_by_name(name)
        for s in list:
            new_list.append(s.__str__())
        return new_list

    def search_student_by_first_name(self, first_name):
        """
        Searching a student by first name
        :param first_name:
        :return:
        """
        new_list = []
        list = self._student_repo.get_by_first_name(first_name)
        for s in list:
            new_list.append(s.__str__())
        return new_list

    def search_student_by_last_name(self, last_name):
        """
        Searching a student by last name
        :param last_name:
        :return:
        """
        new_list = []
        list = self._student_repo.get_by_last_name(last_name)
        for s in list:
            new_list.append(s.__str__())
        return new_list
