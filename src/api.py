import requests
from src.base_api import JobAPI
from src.vacancy import Vacancy


class HeadHunterAPI(JobAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query, count=20):
        params = {'text': query, 'per_page': count}
        response = requests.get(self.BASE_URL, params=params)
        response.raise_for_status()  # Проверка на ошибки
        return response.json()



hh_api = HeadHunterAPI()
search_query = input("Введите поисковый запрос: ")
hh_vacancies = hh_api.get_vacancies(search_query)
print(hh_vacancies)
