import sys
sys.path.insert(0, '..')


class Vacancy:
    """
    Класс для работы с вакансиями.
    """
    def __init__(self, name: str, salary: int, url: str, description: str, company_name: str):
        self.__name = name
        self.__salary = salary
        self.__url = url
        self.__description = description
        self.__company_name = company_name

    def __repr__(self) -> str:
        return f"Вакансия: {self.__name}\nЗарплата: {self.__salary}\nСсылка: {self.__url}\nОписание: {self.__description}\nНазвание компании: {self.__company_name}\n"

    def __str__(self) -> str:
        return f"Вакансия: {self.__name}\nЗарплата: {self.__salary}\nСсылка: {self.__url}\nОписание: {self.__description}\nНазвание компании: {self.__company_name}\n"

    def __lt__(self, other) -> bool:
        return self.__salary < other.__salary

    def __gt__(self, other) -> bool:
        return self.__salary > other.__salary

    def __le__(self, other) -> bool:
        return self.__salary <= other.__salary

    def __ge__(self, other) -> bool:
        return self.__salary >= other.__salary

    def __iter__(self):
        self.value = 0
        return self

    def __next__(self):
        if self.value < self.count:
            self.value += 1
        else:
            raise StopIteration


class HHvacancy(Vacancy):
    """
    Класс для работы с вакансиями с сайта hh.ru.
    """
    def __init__(self, name, salary, url, description, company_name):
        super().__init__(name, salary, url, description, company_name)
        self.company_name = company_name

    @classmethod
    def fill_list_with_vacancies(cls, data):
        cls.vacancies_list = []
        for item in data['items']:
            hh_name = item['name']
            hh_url = item.get('alternate_url')
            try:
                hh_description = item['snippet'].get('responsibility').replace('<highlighttext>', '').replace('</highlighttext>', '')
                if hh_description is None:
                    hh_description = 'Работодатель не указал описание вакансии'
            except AttributeError:
                hh_description = 'Работодатель не указал описание вакансии'
            hh_company_name = item['employer']['name']
            try:
                hh_salary = item['salary'].get('from')
                if hh_salary is None:
                    hh_salary = 0
            except AttributeError:
                hh_salary = 0
            cls.vacancies_list.append(HHvacancy(hh_name, hh_salary, hh_url, hh_description, hh_company_name))
        return cls.vacancies_list


class SJvacancy(Vacancy):
    """
    Класс для работы с вакансиями с сайта superjob.ru.
    """
    def __init__(self, name, salary, url, description, company_name):
        super().__init__(name, salary, url, description, company_name)
        self.company_name = company_name

    @classmethod
    def fill_list_with_vacancies(cls, data):
        cls.vacancies_list = []
        for item in data['objects']:
            SJ_name = item['profession']
            SJ_url = item.get('link')
            try:
                SJ_description = item['candidat'].replace('\n', '').replace('\"', '').replace('\"', '')
                if SJ_description is None:
                    SJ_description = 'Работодатель не указал описание вакансии'
            except AttributeError:
                SJ_description = 'Работодатель не указал описание вакансии'
            try:
                SJ_company_name = item['client'].get('title').replace('\"', '').replace('\"', '')
                if SJ_company_name is None:
                    SJ_company_name = 'Работодатель не указал название компании'
            except AttributeError:
                SJ_company_name = 'Работодатель не указал название компании'
            try:
                SJ_salary = item.get('payment_from')
                if SJ_salary is None:
                    SJ_salary = 0
            except AttributeError:
                SJ_salary = 0
            cls.vacancies_list.append(HHvacancy(SJ_name, SJ_salary, SJ_url, SJ_description, SJ_company_name))
        return cls.vacancies_list
