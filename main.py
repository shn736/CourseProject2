import requests
import json
from abc import ABC, abstractmethod


# Абстрактный класс для работы с API
class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query):
        pass


# Класс для работы с hh.ru
class HeadHunterAPI(JobAPI):
    BASE_URL = "https://api.hh.ru/vacancies"

    def get_vacancies(self, query):
        response = requests.get(self.BASE_URL, params={"text": query})
        response.raise_for_status()  # Проверка на ошибки
        return response.json()


# Класс для представления вакансии
class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        if not salary:
            return "Зарплата не указана"
        return salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        print(f"Vacancy({self.title}, {self.url}, {self.salary}, {self.description})")

    @classmethod
    def cast_to_object_list(cls, data):
        vacancies = []
        for item in data['items']:
            vacancies.append(cls(
                item['name'],
                item['alternate_url'],
                item['salary'] or "Зарплата не указана",
                item['snippet']['requirement']
            ))
        return vacancies


# Абстрактный класс для работы с файлами
class AbstractFileSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


# Класс для сохранения информации о вакансиях в JSON-файл
class JSONSaver(AbstractFileSaver):
    def __init__(self, filename='vacancies.json'):
        self.filename = filename

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def delete_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies = [v for v in vacancies if v['title'] != vacancy.title]
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []


# Функции для взаимодействия с пользователем
def filter_vacancies(vacancies, keywords):
    return [vacancy for vacancy in vacancies if any(keyword in vacancy.description for keyword in keywords)]


def get_vacancies_by_salary(vacancies, salary_range):
    min_salary, max_salary = map(int, salary_range.split(' - '))
    return [vacancy for vacancy in vacancies if
            isinstance(vacancy.salary, int) and min_salary <= vacancy.salary <= max_salary]


def sort_vacancies(vacancies):
    return sorted(vacancies)


def get_top_vacancies(vacancies, n):
    return vacancies[:n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)


def user_interaction():
    hh_api = HeadHunterAPI()
    search_query = input("Введите поисковый запрос: ")
    hh_vacancies = hh_api.get_vacancies(search_query)
    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    json_saver = JSONSaver()

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
    salary_range = input("Введите диапазон зарплат: ")  # Пример: 100000 - 150000

    filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
    ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
    sorted_vacancies = sort_vacancies(ranged_vacancies)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    json_saver.add_vacancy(top_vacancies)
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()