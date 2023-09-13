from src.exceptions.validation_error import DisciplineValidException


class Discipline_validator:
    def __init__(self):
        pass

    def validate_discipline(self, discipline):
        """
        validating a discipline
        :param discipline:
        :return:
        """
        errors = ""
        if discipline.discipline_id < 0:
            errors += "The id can't be negative"
        if len(discipline.discipline_name) == 0:
            errors += "The name can't be empty"
        if len(errors) > 0:
            raise DisciplineValidException(errors)