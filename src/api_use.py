import sys
import requests
from abc import ABC, abstractmethod
sys.path.insert(0, '..')


class AbstractClass_api_use(ABC):
    """
    Абстрактный класс для работы с api
    """
    @abstractmethod
    def get_vacancies(self, search_word: str):
        return search_word


class Headhunter_API(AbstractClass_api_use):
    """
    Класс для работы с api hh.ru
    """
    __url_headhunter = 'https://api.hh.ru/'
    __vacancies_count = 20

    def get_vacancies(self, search_word: str) -> dict:
        response = requests.get(f'{self.__url_headhunter}/vacancies?text={search_word}&per_page={self.__vacancies_count}')
        if response.status_code == 200:
            return response.json()
        return None


class SuperJob_API(AbstractClass_api_use):
    """
    Класс для работы с api superjob.ru
    """
    __url = 'https://api.superjob.ru/2.0'
    __secret = 'v3.r.138649906.1bf43c6696f33076a8a218a4ba39bf57f35c3980.23615578f6424c1b4c2161011043e8c88eae880a'
    __vacancies_count = 20
    headers = {'X-Api-App-Id': __secret}

    def get_vacancies(self, search_word: str) -> dict:
        response = requests.get(f'{self.__url}/vacancies?keyword={search_word}&count={self.__vacancies_count}', headers=self.headers)
        if response.status_code == 200:
            return response.json()
        return None
