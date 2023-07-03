class Vacancy:
    """Класс Вакансии для удобной работы"""
    def __init__(self, name, url, salary, requirement, experience):
        self.__name = name
        self.__url = url
        self.__salary = salary
        self.__requirement = requirement
        self.__experience = experience

    @property
    def name(self):
        return self.__name

    @property
    def url(self):
        return self.__url

    @property
    def salary(self):
        return self.__salary

    @property
    def requirement(self):
        return self.__requirement

    @property
    def experience(self):
        return self.__experience


class VacancyJSON(Vacancy):
    """Класс Вакансии для удобной работы с айди"""
    def __init__(self, name, url, salary, requirement, experience, id):
        super().__init__(name, url, salary, requirement, experience)
        self.__id = id

    @property
    def id(self):
        return self.__id
