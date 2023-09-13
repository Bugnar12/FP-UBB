from src.errors.erori import StudentValidationError
from src.domain.student import Student


class StudentValidator:


    def validate(self, student : Student):
        errors = []
        if student.student_id is str or student.student_id == 0:
            errors.append('Invalid id!')
        if str(student.name) == "":
            errors.append('Name should be a string!')
        if student.group is str or student.group == 0:
            errors.append('Group does not exist!')

        if len(errors) != 0:
            raise StudentValidationError(errors)

