import os
from abc import ABC, abstractmethod

import requests

from classes.vacancy import Vacancy


class VacanciesApi(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterApi(VacanciesApi):
    """Класс для работы с апи hh.ru"""

    def get_vacancies(self, keyword):
        """Позволяет получить список объектов Vacancy по запросу"""
        params = {
            "text": f"{keyword}",
            "page": 1,
            "per_page": 100
        }

        response = requests.get(f'https://api.hh.ru/vacancies', params)

        if response.status_code == 200:
            data = response.json()
            vacancies = []
            for i in range(len(data['items'])):
                if data['items'][i]['salary'] is not None:
                    salary_from = data['items'][i]['salary']['from']
                    salary_to = data['items'][i]['salary']['to']
                    salary_currency = data['items'][i]['salary']['currency']
                    salary = {
                        'from': salary_from,
                        'to': salary_to,
                        'currency': salary_currency,
                    }
                else:
                    salary = None

                try:
                    name = data['items'][i]['name'].replace('<highlighttext>', '').replace('</highlighttext>', '')
                except AttributeError:
                    name = None
                try:
                    requirement = data['items'][i]['snippet']['requirement'].replace('<highlighttext>', '').replace(
                        '</highlighttext>', '')
                except AttributeError:
                    requirement = None

                format_data = {
                    'name': name,
                    'url': data['items'][i]['alternate_url'],
                    'salary': salary,
                    'requirement': requirement,
                    'experience': data['items'][i]['experience']['name']
                }
                vacancies.append(Vacancy(**format_data))
            return vacancies
        else:
            print("Произошла ошибка, попробуйте ещё раз!hh")


class SuperJobApi(VacanciesApi):
    """Класс для работы с апи superjob.ru"""

    def get_vacancies(self, keyword):
        """Позволяет получить список объектов Vacancy по запросу"""
        sj_api_url = 'https://api.superjob.ru/2.0/vacancies/'
        sj_api_key = os.getenv('SJ_API_KEY')
        headers = {
            'X-Api-App-Id': sj_api_key,
        }

        payload = {
            'keyword': f'{keyword}',
            'page': 0,
            'count': 200
        }
        response = requests.get(sj_api_url, headers=headers, params=payload)
        if response.status_code == 200:
            data = response.json()
            vacancies = []
            for i in range(len(data['objects'])):
                salary_from = data['objects'][i]['payment_from']
                salary_to = data['objects'][i]['payment_to']
                salary_currency = data['objects'][i]['currency'].upper()

                if salary_from == 0 and salary_to == 0:
                    salary = None
                else:
                    salary = salary = {
                        'from': salary_from,
                        'to': salary_to,
                        'currency': salary_currency,
                    }
                try:
                    name = data['objects'][i]['profession'].replace('<highlighttext>', '').replace('</highlighttext>',
                                                                                                   '')
                except AttributeError:
                    name = None
                try:
                    requirement = data['objects'][i]['candidat'].replace('<highlighttext>', '').replace(
                        '</highlighttext>', '')
                except AttributeError:
                    requirement = None

                format_data = {
                    'name': name,
                    'url': data['objects'][i]['link'],
                    'salary': salary,
                    'requirement': requirement,
                    'experience': data['objects'][i]['experience']['title'],
                }
                vacancies.append(Vacancy(**format_data))
            return vacancies
        else:
            print("Произошла ошибка, попробуйте ещё раз!sj")
