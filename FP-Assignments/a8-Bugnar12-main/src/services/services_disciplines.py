from src.repository.discipline_repo import Discipline_repo
from src.domain.discipline import Discipline
from src.repository.grade_repo import Grade_repo
from src.validator.discipline_validator import Discipline_validator


class Discipline_service:
    def __init__(self, discipline_validator, discipline_repo : Discipline_repo, grade_repo : Grade_repo):
        self._discipline_validator = discipline_validator
        self._discipline_repo = discipline_repo
        self._grade_repo = grade_repo

    def generate_random_disciplines(self):
        """
        I have to generate random disciplines
        :return:
        """
        self._discipline_repo.randomized_disciplines(20)

    def add_discipline(self, id, name):
        """
        I have to add a discipline to the discipline repo
        :param id:
        :param name:
        :return:
        """
        new_discipline = Discipline(id, name)
        self._discipline_validator.validate_discipline(new_discipline)
        self._discipline_repo.add(new_discipline)

    def remove_discipline(self, id):
        """
        I have to remove the discipline from the discipline repo and from the grade repo
        :param id:
        :return:
        """
        discipline = self._discipline_repo.get(id)

        self._grade_repo.remove_by_discipline_id(discipline.discipline_id)

        self._discipline_repo.remove_by_id(discipline)

    def update_discipline_name(self, id, new_name):
        """
        I have to update the name of the discipline
        :param id:
        :param new_name:
        :return:
        """
        new_discipline = Discipline(id, new_name)
        self._discipline_repo.update_discipline(new_discipline)

    def display_disciplines(self):
        """
        I have to display all the disciplines
        :return:
        """
        new_list = []
        for d in self._discipline_repo.get_all_disciplines():
            new_list.append(d.__str__())
        return new_list

    def search_discipline_by_id(self, id):
        """
        I have to search a discipline by its id
        :param id:
        :return:
        """
        return self._discipline_repo.get(id)


    def search_discipline_by_name(self, name):
        """
        I have to search a discipline by its name
        :param name:
        :return:
        """
        new_list = []
        list = self._discipline_repo.get_by_name(name)
        for d in list:
            new_list.append(d.__str__())

        return new_list