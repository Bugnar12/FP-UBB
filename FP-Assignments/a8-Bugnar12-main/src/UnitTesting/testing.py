import unittest

from src.domain.grade import Grade
from src.domain.student import Student
from src.domain.discipline import Discipline
from src.repository import discipline_repo
from src.repository.grade_repo import Grade_repo
from src.repository.student_repo import Student_repo
from src.services.services_student import Student_service
from src.validator.discipline_validator import Discipline_validator
from src.validator.grade_validator import Grade_validator
from src.validator.student_validator import Student_validator
from src.repository.discipline_repo import Discipline_repo



class TestStudent(unittest.TestCase):
    def test_str_student(self):
        student = Student(1234, "Bucur")
        self.assertEqual(student.__str__(), "1234 : Bucur")

    def test_set_student_name(self):
        student = Student(1234, "Bucur")
        student.set_student_name = "Sergiu"
        self.assertEqual(student.student_name, "Sergiu")

class TestDiscipline(unittest.TestCase):
    def test_str_discipline(self):
        discipline = Discipline(123, "Math")
        self.assertEqual(discipline.__str__(), "123 -> Math")

    def test_set_discipline_name(self):
        discipline = Discipline(123, "Math")
        discipline.set_discipline_name = "Physics"
        self.assertEqual(discipline.discipline_name, "Physics")

class TestGrade(unittest.TestCase):
    def test_str_grade(self):
        grade = Grade(123, 987, 8) #stud_id, dis_id, grade value
        self.assertEqual(grade.__str__(), "Student_id : 123 -> Discipline_id : 987 Grade value : 8")

    def test_set_grade_value(self):
        grade = Grade(123, 987, 8)
        grade.set_grade_value = 10
        self.assertEqual(grade.grade_value, 10)

    def test_getter_student_id(self):
        grade = Grade(123, 987, 8)
        self.assertEqual(grade.student_id_grade, 123)

    def test_getter_discipline_id(self):
        grade = Grade(123, 987, 8)
        self.assertEqual(grade.discipline_id_grade, 987)

class Test_student_validator(unittest.TestCase):
    def test_validate_student(self):
        id_student = 123
        name_student = "Bucur"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        self.assertEqual(student_validator.validate_student(student), None)

    def test_validate_id_student(self):
        id_student = -1
        name_student = "Bucur"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        self.assertRaises(ValueError, student_validator.validate_student(student))

    def test_validate_name_student(self):
        id_student = 123
        name_student = str()
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        self.assertRaises(ValueError, student_validator.validate_student(student))

class Test_discipline_validator(unittest.TestCase):
    def test_validate_discipline(self):
        id_discipline = 123
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        self.assertEqual(discipline_validator.validate_discipline(discipline), None)

    def test_validate_id_discipline(self):
        id_discipline = -1
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        self.assertRaises(ValueError, discipline_validator.validate_discipline(discipline))

    def test_validate_name_discipline(self):
        id_discipline = 123
        name_discipline = str()
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        self.assertRaises(ValueError, discipline_validator.validate_discipline(discipline))

class Test_grade_validator(unittest.TestCase):
    def test_validate_grade(self):
        id_student_grade = 123
        id_discipline_grade = 987
        grade_value = 8
        grade = Grade(id_student_grade, id_discipline_grade, grade_value)
        grade_validator = Grade_validator()
        self.assertEqual(grade_validator.validate_grade(grade), None)

    def test_validate_id_student(self):
        id_student_grade = -1
        id_discipline_grade = 987
        grade_value = 8
        grade = Grade(id_student_grade, id_discipline_grade, grade_value)
        grade_validator = Grade_validator()
        self.assertRaises(ValueError, grade_validator.validate_grade(grade))

    def test_validate_id_discipline(self):
        id_discipline_grade = -1
        id_student_grade = 123
        grade_value = 8
        grade = Grade(id_student_grade, id_discipline_grade, grade_value)
        grade_validator = Grade_validator()
        self.assertRaises(ValueError, grade_validator.validate_grade(grade))

    def test_validate_grade_value(self):
        id_student_grade = 123
        id_discipline_grade = 987
        grade_value = -1
        grade = Grade(id_student_grade, id_discipline_grade, grade_value)
        grade_validator = Grade_validator()
        self.assertRaises(ValueError, grade_validator.validate_grade(grade))

class Test_student_repo(unittest.TestCase):
    def test_add_student(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        self.assertEqual(len(student_repo.get_all_students()), 0)
        student_repo.add(student)
        self.assertEqual(len(student_repo.get_all_students()), 1)
        id_same_student = 35
        name_same_student = "Marco"
        same_student = Student(id_same_student, name_same_student)
        self.assertRaises(ValueError, student_repo.add, same_student)

    def test_update_student(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        id_same_student = 35
        name_same_student = "Sergiu"
        same_student = Student(id_same_student, name_same_student)
        student_repo.update_student(same_student)
        self.assertEqual(student_repo.get_all_students(), [same_student])
        another_student = Student(36, "Sergiu")
        self.assertRaises(ValueError, student_repo.update_student, another_student)

    def test_delete_student(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        list = student_repo.get_all_students()
        student_repo.remove_by_id(student)
        self.assertEqual(student_repo.get_all_students(), [])
        another_student = Student(36, "Sergiu")
        self.assertRaises(ValueError, student_repo.remove_by_id, another_student)

    def test_get_by_name(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        self.assertEqual(student_repo.get_by_name("Marco"), student)


    def test_get_by_first_name(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        self.assertEqual(student_repo.get_by_first_name("Marco"), student)


    def test_get_by_last_name(self):
        id_student = 35
        name_student = "Marco Popescu"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        self.assertEqual(student_repo.get_by_last_name("Popescu"), student)


    def test_len(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        self.assertEqual(len(student_repo), 1)
        student_repo.remove_by_id(student)
        self.assertEqual(len(student_repo), 0)

    def test_get_student_by_id(self):
        id_student = 35
        name_student = "Marco"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        student_repo.add(student)
        self.assertEqual(student_repo.get(35), student)
        self.assertRaises(ValueError, student_repo.get, 36)

    def test_generate_randomized(self):
        student_repo = Student_repo()
        generated_students = student_repo.randomized_students(10)
        self.assertEqual(len(generated_students), 10)

class Test_discipline_repo(unittest.TestCase):
    def test_add_discipline(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        self.assertEqual(len(discipline_repo.get_all_disciplines()), 0)
        discipline_repo.add(discipline)
        self.assertEqual(len(discipline_repo.get_all_disciplines()), 1)
        id_same_discipline = 35
        name_same_discipline = "Math"
        same_discipline = Discipline(id_same_discipline, name_same_discipline)
        self.assertRaises(ValueError, discipline_repo.add, same_discipline)

    def test_update_discipline(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        discipline_repo.add(discipline)
        id_same_discipline = 35
        name_same_discipline = "Physics"
        same_discipline = Discipline(id_same_discipline, name_same_discipline)
        discipline_repo.update_discipline(same_discipline)
        self.assertEqual(discipline_repo.get_all_disciplines(), [same_discipline])
        another_discipline = Discipline(36, "Physics")
        self.assertRaises(ValueError, discipline_repo.update_discipline, another_discipline)

    def test_delete_discipline(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        discipline_repo.add(discipline)
        list = discipline_repo.get_all_disciplines()
        discipline_repo.remove_by_id(discipline)
        self.assertEqual(discipline_repo.get_all_disciplines(), [])
        another_discipline = Discipline(36, "Physics")
        self.assertRaises(ValueError, discipline_repo.remove_by_id, another_discipline)

    def test_get_by_name(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        discipline_repo.add(discipline)
        self.assertEqual(discipline_repo.get_by_name("Math"), discipline)

    def test_len(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        discipline_repo.add(discipline)
        self.assertEqual(len(discipline_repo), 1)
        discipline_repo.remove_by_id(discipline)
        self.assertEqual(len(discipline_repo), 0)

    def test_get_discipline_by_id(self):
        id_discipline = 35
        name_discipline = "Math"
        discipline = Discipline(id_discipline, name_discipline)
        discipline_validator = Discipline_validator()
        discipline_repo = Discipline_repo()
        discipline_repo.add(discipline)
        self.assertEqual(discipline_repo.get(35), discipline)
        self.assertRaises(ValueError, discipline_repo.get, 36)

    def test_generate_random_discipline(self):
        discipline_repo = Discipline_repo()
        discipline_repo.randomized_disciplines(10)
        self.assertEqual(len(discipline_repo), 10)

class Test_grade_repo(unittest.TestCase):
    def test_add_grade(self):
        id_student = 35
        id_discipline = 35
        grade_value = 10
        grade = Grade(id_student, id_discipline, grade_value)
        grade_validator = Grade_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        self.assertEqual(len(grade_repo.get_all_grades()), 0)
        grade_repo.add_grade(grade)
        self.assertEqual(len(grade_repo.get_all_grades()), 1)
        id_same_student = 35
        id_same_discipline = 35
        same_grade_value = 10
        same_grade = Grade(id_same_student, id_same_discipline, same_grade_value)
        self.assertRaises(ValueError, grade_repo.add_grade(), same_grade)

    def test_get_grades_by_student(self):
        id_student = 35
        id_discipline = 35
        grade_value = 10
        grade = Grade(id_student, id_discipline, grade_value)
        grade_validator = Grade_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        grade_repo.add_grade(grade)
        self.assertEqual(grade_repo.get_grades_by_student(35), [grade])
        self.assertRaises(ValueError, grade_repo.get_grades_by_student, 36)

    def test_get_grades_by_discipline(self):
        id_student = 35
        id_discipline = 35
        grade_value = 10
        grade = Grade(id_student, id_discipline, grade_value)
        grade_validator = Grade_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        grade_repo.add_grade(grade)
        self.assertEqual(grade_repo.get_grades_by_discipline(35), [grade])
        self.assertRaises(ValueError, grade_repo.get_grades_by_discipline, 36)

    def test_remove_by_student_id(self):
        id_student = 35
        id_discipline = 35
        grade_value = 10
        grade = Grade(id_student, id_discipline, grade_value)
        grade_validator = Grade_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        grade_repo.add_grade(grade)
        self.assertEqual(len(grade_repo.get_all_grades()), 1)
        grade_repo.remove_by_student_id(35)
        self.assertEqual(len(grade_repo.get_all_grades()), 0)
        self.assertRaises(ValueError, grade_repo.remove_by_student_id, 36)

    def test_remove_by_discipline_id(self):
        id_student = 35
        id_discipline = 35
        grade_value = 10
        grade = Grade(id_student, id_discipline, grade_value)
        grade_validator = Grade_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        grade_repo.add_grade(grade)
        self.assertEqual(len(grade_repo.get_all_grades()), 1)
        grade_repo.remove_by_discipline_id(35)
        self.assertEqual(len(grade_repo.get_all_grades()), 0)
        self.assertRaises(ValueError, grade_repo.remove_by_discipline_id, 36)

    def test_generate_grades(self):
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        grade_repo.generate_random_grades(10)
        self.assertEqual(len(grade_repo.get_all_grades()), 10)


class Test_Student_service(unittest.TestCase):
    def test_add_student(self):
        id_student = 123
        name_student = "Bucur"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        service_student = Student_service(student_validator, student_repo, grade_repo)
        service_student.add_student(id_student, name_student)
        self.assertEqual(len(student_repo), 1)

    def test_remove_student(self):
        id_student = 123
        name_student = "Bucur"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        service_student = Student_service(student_validator, student_repo, grade_repo)
        service_student.add_student(id_student, name_student)
        service_student.remove_student(id_student)
        self.assertEqual(service_student.display_students(), [])

    def test_update_student_name(self):
        id_student = 123
        name_student = "Bucur"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        service_student = Student_service(student_validator, student_repo, grade_repo)
        service_student.add_student(id_student, name_student)
        service_student.update_student_name(id_student, "Sergiu")
        self.assertEqual(service_student.display_students(), [Student(123, "Sergiu")])

    def test_display_students(self):
        id_student = 123
        name_student = "Mara"
        student = Student(id_student, name_student)
        student_validator = Student_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        service_student = Student_service(student_validator, student_repo, grade_repo)
        service_student.add_student(id_student, name_student)
        list = service_student.display_students()
        for s in list:
            self.assertEqual(s, student)

    def test_generate_students(self):
        student_validator = Student_validator()
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        service_student = Student_service(student_validator, student_repo, grade_repo)
        service_student.generate_random_students()
        self.assertEqual(len(service_student.display_students()), 10)

    def test_search_student_by_name(self):
        id_student = 12
        name_student = "Bucur"
        student_repo = Student_repo()
        discipline_repo = Discipline_repo()
        student_validator = Student_validator()
        grade_repo = Grade_repo(student_repo, discipline_repo)
        student_services = Student_service(student_validator, student_repo, grade_repo)
        student_repo.add(Student(id_student, name_student))
        self.assertEqual(student_services.search_student_by_id(id_student), [Student(id_student, name_student)])


