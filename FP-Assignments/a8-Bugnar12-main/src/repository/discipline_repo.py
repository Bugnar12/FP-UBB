from src.domain.discipline import Discipline
from src.exceptions.exceptions import RepoException
from random import randint, choice, random, sample


class Discipline_repo():
    """
       Here I will use the memory repo since it's the most convenient one,
       and the repo will represent the space where the list of disciplines
       will be saved(memorized).

       The discipline repo will be represented as a dictionary that has only an id and a name
       """

    def __init__(self):
        self._disciplines = {}

    def add(self, new_discipline: Discipline):
        """
        This method adds a discipline to the repo
        :param new_discipline:
        :return:
        """
        if new_discipline.discipline_id in self._disciplines:
            raise RepoException("Discipline is already in repo")
        self._disciplines[new_discipline.discipline_id] = new_discipline

    def get(self, id : int):
        """
        method for getting a discipline
        :param self:
        :param id:
        :return:
        """
        try:
            return self._disciplines[id]
        except:
            raise RepoException("Discipline is not in repo")

    def get_all_disciplines(self):
        """
        Gets all disciplines from the repo
        :param self:
        :return:
        """
        return list(self._disciplines.values())

    def __len__(self):
        """
        The lenght of the repo
        :param self:
        :return:
        """
        return len(self._disciplines)

    def update_discipline(self, updated_discipline: Discipline):
        """
        This method updates a discipline
        :param self:
        :param updated_discipline:
        :return:
        """
        if updated_discipline.discipline_id not in self._disciplines:
            raise RepoException("The updated discipline does not exist")
        self._disciplines[updated_discipline.discipline_id] = updated_discipline

    def remove_by_id(self, removed_discipline: Discipline):
        """
        This method removes a discipline by id
        :param self:
        :param removed_discipline:
        :return:
        """
        if removed_discipline.discipline_id not in self._disciplines:
            raise RepoException("The discipline can't be removed since he doesn't exist")
        else:
            del self._disciplines[removed_discipline.discipline_id]


    def get_by_name(self, name : str):
        """
        This method searches for a discipline by name
        :param name:
        :return:
        """
        list = []
        for discipline in self._disciplines.values():
            if discipline.discipline_name == name:
                list.append(discipline)

        return list

    def randomized_disciplines(self, n : int):
        """
        This method generates random disciplines
        Each discipline has a unique id and a name
        :return:
        """
        disciplines = ["Math", "Physics", "Chemistry", "Biology", "History", "Geography", "English", "French", "Spanish", "German",
                       "Latin", "Greek", "Arabic", "Economics", "Philosophy", "Psychology", "Sociology", "Politics", "Law", "Computer Science",]
        for i in range(n):
            discipline_id = i
            discipline_name = choice(disciplines)
            new_discipline = Discipline(discipline_id, discipline_name)
            Discipline_repo.add(self, new_discipline)