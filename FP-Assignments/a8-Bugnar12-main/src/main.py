from src.repository.discipline_repo import Discipline_repo
from src.repository.grade_repo import Grade_repo
from src.services.services_disciplines import Discipline_service
from src.services.services_grade import Grade_service
from src.services.services_student import Student_service
from src.repository.student_repo import Student_repo
from src.ui.userinterface import Ui
from src.domain.student import Student
from src.validator.discipline_validator import Discipline_validator
from src.validator.grade_validator import Grade_validator
from src.validator.student_validator import Student_validator



if __name__ == "__main__":

    #Validators
    student_validator = Student_validator()
    discipline_validator = Discipline_validator()
    grade_validator = Grade_validator()

    #Repositories
    student_repo = Student_repo()
    discipline_repo = Discipline_repo()
    grade_repo = Grade_repo(student_repo, discipline_repo)

    #Services
    service_student = Student_service(student_validator, student_repo, grade_repo)
    service_discipline = Discipline_service(discipline_validator, discipline_repo, grade_repo)
    service_grades = Grade_service(grade_validator, grade_repo, student_repo, discipline_repo)

    #UI
    ui = Ui(service_student, service_discipline, service_grades)
    ui.run()