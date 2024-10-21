import sys
import os
from src.work_with_file import Data_file
from src.classes import HHvacancy, SJvacancy
from src.api_use import Headhunter_API, SuperJob_API
sys.path.insert(0, '../src')


def test_add_and_delete_data():
    hh_api = Headhunter_API()
    SJ_api = SuperJob_API()
    response_hh = hh_api.get_vacancies('python')
    response_sj = SJ_api.get_vacancies('python')
    data_hh = HHvacancy.fill_list_with_vacancies(response_hh)
    data_sj = SJvacancy.fill_list_with_vacancies(response_sj)
    filename_hh = 'test_hh.json'
    filename_sj = 'test_sj.json'
    Data_file().add_data_to_json_file(data_hh, filename_hh)
    Data_file().add_data_to_json_file(data_sj, filename_sj)
    assert os.path.exists(filename_hh) and os.path.exists(filename_sj)
    assert os.path.getsize(filename_hh) > 0 and os.path.getsize(filename_sj) > 0
    Data_file().delete_data_from_file(filename_hh)
    Data_file().delete_data_from_file(filename_sj)
    assert os.path.getsize(filename_hh) == 0 and os.path.getsize(filename_sj) == 0
