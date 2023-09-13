import copy

from src.domain import student


class Ui:
    def __init__(self, service):
        self.__commands={
            'add' : self.__add_student,
            'display' : self.__display_all_students,
            'filter' : self.__filter_students,
             'undo' : self.__undo
        }
        self.__service = service

    def __add_student(self, params):
        if len(params) != 3:
            print("Each student must have an id, a name and a group")
            return
        id = int(params[0])
        name = params[1]
        group = int(params[2])

        self.__service.add_student(id, name, group)
        print("A student has been added")

    def __display_all_students(self, params):
        if len(params) != 0:
            print("Parameters are invalid")
            return
        students = self.__service.display_all_students()
        for student in students:
            print(student)

    def __filter_students(self, params):
        """
        filter students s.t. they are removed from a mentioned group
        :param params:
        :return:
        """
        if len(params) != 1:
            print("A group that has to be removed was not given!")
            return

        group = int(params[0])
        self.__service.filter(group)
        print("The students from " ,group, "have been removed")


    def __undo(self, params):
        if len(params) != 0:
            print("Undo must not have any parameters")
            return
        self.__service.undo()
        print("The latest operation was undoeds")



    def run(self):
        print("\n--- Managing a student list was never easier than this --- \n")
        some_printing()
        self.__service.generate_random()
        while True:
            command = input(">>>")
            command = command.strip()  # cleans the invisible characters from the line
            if command == "":
                some_printing()
                continue
            if command == 'exit':
                print("Bye, bye!")
                return
            parts = command.split()
            command_name = parts[0]
            params = parts[1:]
            for param in params:
                param = param.strip()
            if command_name in self.__commands:
                try:
                    self.__commands[command_name](params)
                except ValueError as ve:
                    print(ve)
            else:
                print("Invalid command!\n")
                some_printing()


def some_printing():
    print("What operation do you want to be performed ?\n")
    print("'ADD' : add a new student to the existing list ")
    print("'DISPLAY' : Display the current state of the list of students")
    print("'FILTER' : Write a group that will have its students deleted from the list")
    print("'UNDO' : Undo the operation you made before")
    print("'EXIT' : Exit the program\n")

