import copy

from src.domain.student import Student
from random import choice, randint
import pickle
import random

class RepoException(Exception):
    pass

#memory repo

class student_repo(object):
    def __init__(self):
        self._students = {}

    def add(self, new_student : Student):
        if new_student.student_id in self._students:
            raise RepoException("Student already in repo")
        self._students[new_student.student_id] = new_student

    def get(self, student : Student):
        # If student cannot be found in repo, catch the dict's KeyError and
        # re-raise it as RepoException
        try:
            return self._students[student]
        except KeyError:
            raise RepoException("Student is not in repo")

    def get_all_students(self):
        return list(self._students.values())

    def __len__(self):
        return len(self._students)

    def update(self, updated_student: Student):
        if updated_student.student_id() not in self._students:
            raise RepoException("The student does not exist")
        self._students[updated_student.student_id()] = updated_student

    def remove_by_id(self, student_spec: Student):
        if student_spec.student_id not in self._students:
            raise RepoException("Student doesn't exist")
        else:
            del self._students[student_spec.student_id]

    def set_all_students(self, students):
        self._students = students


    def generate_randomized(self, n: int):
        result = []
        names = {
            "First name": ["Popescu", "Florescu", "Rus", "Afrasinei", "Dumitrescu", "Cantemir"],
            "Last name": ["Andrei", "Radu", "Cosmin", "Rares", "Dorian", "Lorena", "Ana"]
        }
        for i in range(n):
            id = random.randint(1000, 9999)
            type_of_name = choice(list(names.keys()))
            name = choice(names[type_of_name])
            group = random.randint(911, 939)
            new_student = Student(id, name, group)
            student_repo.add(self, new_student)

#binary file repo

class student_repo_bin_file(student_repo):
    def __init__(self, file_name="student.bin"):
        # call superclass constructor
        super(student_repo_bin_file, self).__init__()
        # remember the name of the file we're working with
        self._file_name = file_name
        # load the students from the file
        self._load_file()

    def add(self, new_student: Student):
        # call the add() method on the super class
        # we want to do everything the superclass add() already does
        super().add(new_student)
        # we also want to save all students to a text file
        self._save_file()

    def _load_file(self):
        # r - read, b - binary
        fin = open(self._file_name, "rb")
        obj = pickle.load(fin)

        for c in obj:
            super().add(c)
        fin.close()

    def _save_file(self):
        # w - write mode (overwrite), b - binary mode
        fout = open(self._file_name, "wb")
        pickle.dump(self.get_all_students(), fout)
        # NOTE Don't forget to close the file!
        fout.close()

#text-file repo


class student_repo_text_file(student_repo):
    # this class inherits from student_repo
    # => has all the methods and attributes in student_repo

    def __init__(self, file_name="students.txt"):
        # call superclass constructor
        super(student_repo_text_file, self).__init__()
        # remember the name of the file we're working with
        self._file_name = file_name
        # load the students from the file
        self._load_file()

    def _load_file(self):
        """
        Load the student from a text file
        """
        # open a text file for reading
        # t - text file mode, r - reading
        lines = []

        try:
            fin = open(self._file_name, "rt")
            # each student should be on its own line
            lines = fin.readlines()
            # close the file when done reading
            fin.close()
        except IOError:
            # It's ok if we don't find the input file
            pass

        for line in lines:
            current_line = line.split(",")
            new_student = Student(current_line[0].strip(), current_line[1].strip(), current_line[2].strip(),
                          current_line[3].strip())
            # NOTE call super() so that we don't write the file we're reading from
            super().add(new_student)

    def _save_file(self):
        """
        Save all student to a text file
        """
        # open a text file for writing
        # t - text file mode, w - writing (rewrite the file every time)
        fout = open(self._file_name, "wt")

        # writes student_string into the text file
        # fout.write(student_string)
        for student in self.get_all_students():
            student_string = str(student.student_id) + "," + str(student.name) + "," + str(student.group) + "\n"
            fout.write(student_string)

        # call close when done writing
        fout.close()

    def add(self, new_student : Student):
        # call the add() method on the super class
        # we want to do everything the superclass add() already does
        super().add(new_student)
        # we also want to save all students to a text file
        self._save_file()

# def generate_students(n : int):
#     result = []
#     names = {
#         "First name": ["Popescu", "Florescu", "Rus", "Afrasinei", "Dumitrescu", "Cantemir"],
#         "Last name": ["Andrei", "Radu", "Cosmin", "Rares", "Dorian", "Lorena", "Ana"]
#     }
#     for i in range(n):
#         id = random.randint(1000, 9999)
#         type_of_name = choice(list(names.keys()))
#         name = choice(names[type_of_name])
#         group = random.randint(911, 939)
#         result.append(Student(id, name, group))
#
#     return result
#
# if __name__ == "__main__":
#     repo = student_repo()
#     for s in generate_students(10):
#         print(str(s))
#         repo.add(s)


