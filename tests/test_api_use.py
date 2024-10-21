import sys
from src.api_use import Headhunter_API, SuperJob_API
sys.path.insert(0, '../src')


def test_get_vacancies():
    hh = Headhunter_API()
    sj = SuperJob_API()
    assert hh.get_vacancies('python')
    assert sj.get_vacancies('python')
