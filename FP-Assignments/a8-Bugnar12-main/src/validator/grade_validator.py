from src.exceptions.validation_error import GradeValidException

class Grade_validator():
    def __init__(self):
        pass

    def validate_grade(self, grade):
        """
        validating a grade
        :param grade:
        :return:
        """
        errors = ""
        if grade.grade_value < 1 or grade.grade_value > 10:
            errors += "The grade value must be between 1 and 10"
        if len(errors) > 0:
            raise GradeValidException(errors)
