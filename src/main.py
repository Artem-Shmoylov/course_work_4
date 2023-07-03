from classes.json_saver import JSONSaver
from classes.vacancies_api import HeadHunterApi, SuperJobApi
import utils


def user_interaction():
    """Интерфейс взаимодействия с пользователем"""
    user_request = input("Введите ключевое слово для поиска вакансий: \n")

    hh_api = HeadHunterApi()
    sj_api = SuperJobApi()

    hh_vacancies = hh_api.get_vacancies(user_request)
    sj_vacancies = sj_api.get_vacancies(user_request)

    json_saver = JSONSaver()
    json_saver.add_vacancies(hh_vacancies, sj_vacancies)
    vacancies = json_saver.get_vacancies_from_json()

    while True:
        try:
            top_n = int(input("Введите количество вакансий для вывода в топ N: \n"))
        except ValueError:
            print("Введите число!")
            continue
        else:
            break

    filter_word = input("Введите ключевое слово для фильтрации вакансий(Пропустить - Enter): \n").strip()
    if len(filter_word) != 0:
        filtered_vacancies = utils.filter_vacancies(vacancies, filter_word)
        if not filtered_vacancies:
            print("Нет вакансий, соответствующих заданным критериям.")
    else:
        filtered_vacancies = vacancies

    sorted_vacancies = utils.sort_vacancies(filtered_vacancies)
    top_vacancies = utils.get_top_vacancies(sorted_vacancies, top_n)
    utils.print_vacancies(top_vacancies)

    while True:
        user_choice = input("Для других вакансий нажмите - 1, выйти из приложения - 0\n")
        if user_choice == "1":
            user_interaction()
        elif user_choice == "0":
            break
        else:
            continue


if __name__ == "__main__":
    user_interaction()
