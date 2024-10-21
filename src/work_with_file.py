import sys
import json
from abc import ABC, abstractmethod
sys.path.insert(0, '..')


class AbstractClass_work_with_file(ABC):
    """
    Абстрактный класс для работы с файлами.
    """
    @abstractmethod
    def add_data_to_json_file(self):
        pass

    @abstractmethod
    def get_data_by_salary(self):
        pass

    @abstractmethod
    def delete_data_from_file(self):
        pass


class Data_file(AbstractClass_work_with_file):
    """
    Класс для работы с файлами.
    """
    def add_data_to_json_file(self, data, filename):
        """
        Функция добавления данных в файл в json формате.
        """
        json_data = []
        for vacancy in data:
            json_vacancy = {
                'name': vacancy._Vacancy__name,
                'salary': vacancy._Vacancy__salary,
                'url': vacancy._Vacancy__url,
                'description': vacancy._Vacancy__description,
                'company_name': vacancy._Vacancy__company_name
            }
            json_data.append(json_vacancy)
            with open(f'{filename}', 'w', encoding='utf-8') as f:
                json.dump(json_data, f)

    def get_data_by_salary(self, data, top_N):
        """
        Функция сортировки данных по зарплате.
        """
        if top_N == 0:
            return data
        else:
            data = sorted(data, reverse=True)
            i = 0
            while i < top_N:
                item = data[i]
                print(item)
                i += 1
            return data

    def delete_data_from_file(self, filename):
        """
        Функция удаления данных из файла.
        """
        with open(filename, 'w') as f:
            f.truncate()

    def print_data(self, data):
        """
        Функция вывода данных в консоль.
        """
        i = 0
        for item in data:
            item = data[i]
            print(item)
            i += 1
