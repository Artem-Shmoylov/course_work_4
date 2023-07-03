import json

from classes.vacancy import VacancyJSON


class JSONSaver:
    """Класс для работы с json"""
    i = 0

    def __init__(self):
        self.vacancies = None

    def add_vacancies(self, *args):
        """Записывает в файл вакансии с сайтов"""
        all_vac_list = []
        for vac_list in args:
            for el in vac_list:
                self.i += 1
                temp_data = {
                    "id": self.i,
                    "name": el.name,
                    "url": el.url,
                    "salary": el.salary,
                    "requirement": el.requirement,
                    "experience": el.experience,
                }
                all_vac_list.append(temp_data)

        self.vacancies = all_vac_list
        self.i = 0
        with open("../src/vacancies.json", "w", encoding="utf-8") as f:
            json.dump(self.vacancies, f, indent=4, ensure_ascii=False)


    def get_vacancies_from_json(self):
        """Считывает  вакансии с файла для удобной работы с ними"""
        with open('../src/vacancies.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            vacancies = []
            for vacancy in data:
                vacancies.append(VacancyJSON(**vacancy))
            return vacancies
