import sys
from src.api_use import Headhunter_API, SuperJob_API
from src.work_with_file import Data_file
from src.classes import SJvacancy, HHvacancy
sys.path.insert(0, '..')


def user_interaction():
    """
    Функция взаимодействия с пользователем.

    Функция позволяет пользователю выбрать платформу для поиска вакансий (HeadHunter или SuperJob),
    Ввести ключевое слово для поиска, а также выбрать, нужно ли сортировать вакансии по зарплате.
    Если пользователь выбирает сортировку по зарплате, он также вводит количество вакансий, которые нужно вывести.
    """
    hh_api = Headhunter_API()
    SJ_api = SuperJob_API()
    json_saver = Data_file()
    url_type = input('Выберите платформу для поиска (HeadHunter/SuperJob): ')
    if url_type == 'HeadHunter' or url_type == 'headhunter' or url_type == 'Headhunter':
        key_word = input('Введите ключевое слово: ')
        response = hh_api.get_vacancies(key_word)
        data = HHvacancy.fill_list_with_vacancies(response)
        if input('Сортировать по зарплате? (да/нет): ') == 'да':
            top_N = int(input('Количество вакансий: '))
            data = json_saver.get_data_from_file_by_salary(data, top_N)
            json_saver.add_data_to_json_file(data, 'HH_vacancies.json')
        else:
            json_saver.add_data_to_json_file(data, 'HH_vacancies.json')
            json_saver.print_data(data)
    elif url_type == 'SuperJob' or url_type == 'superjob' or url_type == 'Superjob':
        key_word = input('Введите ключевое слово: ')
        response = SJ_api.get_vacancies(key_word)
        data = SJvacancy.fill_list_with_vacancies(response)
        if input('Сортировать по зарплате? (да/нет): ') == 'да':
            top_N = int(input('Количество вакансий: '))
            data = json_saver.get_data_from_file_by_salary(data, top_N)
            json_saver.add_data_to_json_file(data, 'HH_vacancies.json')
        else:
            json_saver.add_data_to_json_file(data, 'SJ_vacancies.json')
            json_saver.print_data(data)
    else:
        print('Введено неверное название')


if __name__ == '__main__':
    user_interaction()
