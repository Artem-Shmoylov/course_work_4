def filter_vacancies(vacancies, keyword):
    """Фильтр вакансий по ключевому слову"""
    filtered_vacancies = []
    for vacancy in vacancies:
        try:
            if keyword.lower() in vacancy.name.lower() or keyword.lower() in vacancy.requirement.lower():
                filtered_vacancies.append(vacancy)
        except Exception:
            continue

    return filtered_vacancies


def sort_vacancies(vacancies):
    """Фильтр вакансий по ЗП от большего"""
    sort_for_salary_none = [vacancy for vacancy in vacancies if vacancy.salary is not None]
    sort_for_salary_from = [vacancy for vacancy in sort_for_salary_none if vacancy.salary['from'] is not None]

    sorted_vacancies = sorted(sort_for_salary_from, key=lambda x: x.salary['from'], reverse=True)
    return sorted_vacancies


def get_top_vacancies(vacancies, top_n):
    """Возвращает топ N вакансий"""
    return vacancies[0:top_n]


def print_vacancies(vacancies):
    """Выводит в консоль топ N вакнсий"""
    for vacancy in vacancies:

        if vacancy.salary['to'] is not None:
            salary = f'от {vacancy.salary["from"]} до {vacancy.salary["to"]}'
        else:
            salary = f'от {vacancy.salary["from"]}'

        print(f'**************************************\n'
              f'    Айди ваканции - {vacancy.id}\n'
              f'    Название ваканции - {vacancy.name}\n'
              f'    ЗП - {salary}\n'
              f'    Сылка на вакансию - {vacancy.url}\n'
              f'    Описание вакансии - {vacancy.requirement}\n'
              f'    Опыт работы - {vacancy.experience}\n'
              f'**************************************\n')
