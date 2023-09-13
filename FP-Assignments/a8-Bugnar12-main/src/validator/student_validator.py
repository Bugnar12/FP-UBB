from src.exceptions.validation_error import StudentValidException

class Student_validator():

    def __init__(self):
        pass

    def validate_student(self, student):
        """
        validating a student
        :param student:
        :return:
        """
        errors = []
        if student.student_id < 0:
            errors.append("The id must be a positive number")
        if len(student.student_name) == 0:
            errors.append("The name must not be empty")
        if len(errors) > 0:
            raise StudentValidException(errors)
