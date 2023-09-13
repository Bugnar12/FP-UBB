from src.services.services_student import Student_service
from src.services.services_disciplines import Discipline_service
from src.services.services_grade import Grade_service


class Ui:
    def __init__(self, service_students : Student_service, service_disciplines : Discipline_service, service_grades : Grade_service):
        self.__commands = {
            'add_student': self.add_student,
            'remove_student': self.remove_student,
            'update_student': self.update_student,
            'display_student': self.display_student_list,
            'add_discipline': self.add_discipline,
            'remove_discipline': self.remove_discipline,
            'update_discipline': self.update_discipline_name,
            'display_discipline': self.display_discipline_list,
            'add_grade': self.add_grade,
            'display_grade': self.display_grades,
            'display_grades': self.display_all_grades,
            'search_student_by_id' : self.search_student_by_id,
            'search_student_by_name' : self.search_student_by_name,
            'search_student_by_first_name' : self.search_student_by_first_name,
            'search_student_by_last_name' : self.search_student_by_last_name,
            'search_discipline_by_id' : self.search_discipline_by_id,
            'search_discipline_by_name' : self.search_discipline_by_name,
            'statistics_failing_students' : self.statistics_failing_students,
            'statistics_best_students': self.statistics_best_students,
            'statistics_best_disciplines': self.statistics_best_disciplines,
        }
        self.__service_students = service_students
        self.__service_disciplines = service_disciplines
        self.__service_grades = service_grades

    def add_student(self, params):
        """
        has 2 parameters, one is the id and one is the name of the student
        :param params:
        :return:
        """
        if len(params) != 3:
            print("student must have an id and a name")
            return
        id = int(params[0])
        first_name = params[1]
        last_name = params[2]

        full_name = first_name + " " + last_name

        self.__service_students.add_student(id, full_name)
        print("A student was added")

    def remove_student(self, params):
        """
        has 1 parameter, the id of the student that will be removed
        :param params:
        :return:
        """
        if len(params) != 1:
            print("input only the id of the student you want to be deleted")
            return
        id = int(params[0])

        self.__service_students.remove_student(id)
        print("A student was removed")

    def update_student(self, params):
        """
        has 2 parameters, one is the id and one is the name that the student will have after the update
        :param params:
        :return:
        """
        if len(params) != 3:
            print("Input id and the desired name")
            return
        id = int(params[0])
        first_name = params[1]
        last_name = params[2]

        full_name = first_name + " " + last_name

        self.__service_students.update_student_name(id, full_name)
        print("The name of a student was updated")

    def display_student_list(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write display and that' s all")
            return

        list = self.__service_students.display_students()
        for s in list:
            print(s)

    def add_discipline(self, params):
        """
        has 2 parameters, one is the id and one is the name of the discipline
        :param params:
        :return:
        """
        if len(params) != 2:
            print("discipline must have an id and a name")
            return
        id = int(params[0])
        name = params[1]

        self.__service_disciplines.add_discipline(id, name)
        print("A discipline was added")

    def remove_discipline(self, params):
        """
        has 1 parameter, the id of the discipline that will be removed
        :param params:
        :return:
        """
        if len(params) != 1:
            print("input only the id of the discipline you want to be deleted")
            return
        id = int(params[0])

        self.__service_disciplines.remove_discipline(id)
        print("A discipline was removed")

    def update_discipline_name(self, params):
        """
        has 2 parameters, one is the id and one is the name that the discipline will have after the update
        :param params:
        :return:
        """
        if len(params) != 2:
            print("Input id and the desired name")
            return
        id = int(params[0])
        name = params[1]

        self.__service_disciplines.update_discipline_name(id, name)
        print("The name of a discipline was updated")

    def display_discipline_list(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write display and that's all")
            return

        list = self.__service_disciplines.display_disciplines()
        for d in list:
            print(d)

    def add_grade(self, params):
        """
        has 3 parameters, one is the id of the student, one is the id of the discipline and one is the grade
        :param params:
        :return:
        """
        if len(params) != 3:
            print("Input the id of the student, the id of the discipline and the grade")
            return
        student_id = int(params[0])
        discipline_id = int(params[1])
        grade = int(params[2])

        self.__service_grades.add_grade(student_id, discipline_id, grade)
        print("A grade was added")

    def display_grades(self, params):
        """
        has 1 parameter, the id of the student
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the id of the student")
            return
        student_id = int(params[0])

        list_of_grades = self.__service_grades.display_student_grade(student_id)
        for grade in list_of_grades:
            print(grade)
        print("The grades of a student were displayed")

    def display_all_grades(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write display and that's all")
            return

        list = self.__service_grades.display_all_grades()
        for grade in list:
            print(grade)

    def search_student_by_id(self, params):
        """
        has 1 parameter, the id of the student
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the id of the student")
            return
        student_id = int(params[0])

        student = self.__service_students.search_student_by_id(student_id)
        print(student)

    def search_student_by_name(self, params):
        """
        has 1 parameter, the name of the student
        :param params:
        :return:
        """
        if len(params) != 2:
            print("Input the name of the student")
            return

        first_name = params[0]
        first_name = first_name.capitalize()

        last_name = params[1]
        last_name = last_name.capitalize()

        full_name = first_name + " " + last_name

        print(self.__service_students.search_student_by_name(full_name))

    def search_student_by_first_name(self, params):
        """
        has 1 parameter, the name of the student
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the name of the student")
            return

        first_name = params[0]

        first_name = first_name.capitalize()

        print(self.__service_students.search_student_by_first_name(first_name))

    def search_student_by_last_name(self, params):
        """
        has 1 parameter, the name of the student
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the name of the student")
            return

        last_name = params[0]

        last_name = last_name.capitalize()

        print(self.__service_students.search_student_by_last_name(last_name))

    def search_discipline_by_id(self, params):
        """
        has 1 parameter, the id of the discipline
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the id of the discipline")
            return
        discipline_id = int(params[0])

        print(self.__service_disciplines.search_discipline_by_id(discipline_id))

    def search_discipline_by_name(self, params):
        """
        has 1 parameter, the name of the discipline
        :param params:
        :return:
        """
        if len(params) != 1:
            print("Input the name of the discipline")
            return
        discipline_name = params[0]

        discipline_name = discipline_name.capitalize()

        print(self.__service_disciplines.search_discipline_by_name(discipline_name))

    def statistics_failing_students(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write statistics and that's all")
            return

        list = self.__service_grades.statistics_failing_students()
        for student in list:
            print(student)

    def statistics_best_students(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write statistics and that's all")
            return

        list = self.__service_grades.statistics_best_students()
        for student in list:
            print(student)

    def statistics_best_disciplines(self, params):
        """
        has no parameters
        :param params:
        :return:
        """
        if len(params) != 0:
            print("Just write statistics and that's all")
            return

        list = self.__service_grades.statistics_sorted_reverse()
        for discipline in list:
            print(discipline)


    def printings(self):
        print("-------- The menu of the application starts here --------")
        print()
        print("The commands are: ")
        print("What is the sub-menu you want to access?\n")
        print("1. Students")
        print("2. Disciplines")
        print("3. Grades")
        print("4. Search student/discipline")
        print("5. Statistics\n")

        option = int(input("Your option is: \n"))

        if option == 1:
            print("1.for adding a student, write add_student(id, first_name, last_name)")
            print("2.for removing a student, write remove_student(id)")
            print("3.for updating the name of a student, write update_student(id, new_name)")
            print("4.for displaying the list of students, write display_student()")
            print("5.for exiting the sub-menu, write exit")

        elif option == 2:
            print("1.for adding a discipline, write add_discipline(id, name)")
            print("2.for removing a discipline, write remove_discipline(id)")
            print("3.for updating the name of a discipline, write update_discipline_name(id, new_name)")
            print("4.for displaying the list of disciplines, write display_discipline()")
            print("5.for exiting the sub-menu, write exit")

        elif option == 3:
            print("1.for adding a grade, write add_grade(student_id, discipline_id, grade)")
            print("2.for displaying the grades of a student, write display_grade(student_id)")
            print("3.for displaying all the grades, write display_grades()")
            print("4.for exiting the sub-menu, write exit")

        elif option == 4:
            print("1.for searching a student by id, write search_student_by_id(id)")
            print("2.for searching a student by name, write search_student_by_name(first_name, last_name)")
            print("3.for searching a student by first name, write search_student_by_first_name(first_name)")
            print("4.for searching a student by last name, write search_student_by_last_name(last_name)")
            print("5.for searching a discipline by id, write search_discipline_by_id(id)")
            print("6.for searching a discipline by name, write search_discipline_by_name(name)")
            print("7.for exiting the sub-menu, write exit")

        elif option == 5:
            print("1.for displaying the failing students, write statistics_failing_students()")
            print("2.for displaying the best students, write statistics_best_students()")
            print("3.for displaying the best disciplines, write statistics_best_disciplines()")
            print("4.for exiting the sub-menu, write exit")

        else:
            print("Invalid option")
            self.printings()

    def run(self):
        """
        the main loop of the program
        :return:
        """

        self.__service_students.generate_random_students()
        self.__service_disciplines.generate_random_disciplines()
        self.__service_grades.generate_random_grades()
        self.printings()
        while True:
            command = input(">>")
            command = command.strip()  # cleans visible characters
            if command == "":
                continue
            if command == "exit":
                print("Bye Bye!")
                return
            parts = command.split()
            command_name = parts[0]
            self.__params = parts[1:]
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](self.__params)
                except ValueError as ve:
                    print("Invalid parameters")
            else:
                print("Invalid command")

