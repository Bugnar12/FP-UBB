from src.services.services import Service
from src.repository.student_repo import student_repo
from src.domain.validator import StudentValidator
from src.tests.testing import Testing
from src.ui.userinterface import Ui

"""
CRUD(create, read, update, delete)

F S(filter, sort)

U/R(undo, redo)

STATS (statistics)

validation always on service

Value Error -> ui

Validation Error -> validator

Repo Error -> repository 
"""

if __name__ == "__main__":
    validator = StudentValidator()
    repo = student_repo()
    service = Service(validator, repo)
    tests = Testing(repo, validator, service)
    ui = Ui(service)
    ui.run()
