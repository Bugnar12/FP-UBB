class ValidatorException(Exception):
    def __init__(self, message_list="Validation error!"):
        self._message_list = message_list

    @property
    def messages(self):
        return self._message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += message
            result += "\n"
        return result

class AllException(Exception):
    def __init__(self, message):
        self._message = message

    def __str__(self):
        return self._message

class StudentValidException(AllException):
    def __init__(self, error_list):
        self._error_list = error_list

    def __str__(self):
        result = ""
        for error in self._error_list:
            result += error
        return result

class DisciplineValidException(AllException):
    def __init__(self, error_list):
        self._error_list = error_list

    def __str__(self):
        result = ""
        for error in self._error_list:
            result += error
        return result

class GradeValidException(AllException):
    def __init__(self, error_list):
        self._error_list = error_list

    def __str__(self):
        result = ""
        for error in self._error_list:
            result += error
        return result