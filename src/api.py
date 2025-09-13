import requests
from src.base_api import AbstractAPI



class HeadHunterAPI(AbstractAPI):
    """Класс для работы с API hh.ru"""
    base_url = 'https://api.hh.ru/vacancies'


    def get_vacancies(self, query):
        response = requests.get(self.base_url, params={'text': query})
        return response.json() if response.status_code == 200 else {}
