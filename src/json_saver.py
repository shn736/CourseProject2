import json
from typing import Any

from src.base_json_saver import AbstractSaver


class JSONSaver(AbstractSaver):
    """Класс для работы с JSON-файлом"""
    def __init__(self, filename: str = 'vacancies.json'):
        """Функция для определения файла сохранения"""
        self.filename = filename

    def add_vacancy(self, vacancy: Any) -> Any:
        """Добавление файла"""
        data = self.load_data()
        data.append(vars(vacancy))  # Преобразуйте объект Vacancy в словарь
        self.save_data(data)

    def delete_vacancy(self, vacancy: Any) -> Any:
        """Удаление файла"""
        data = self.load_data()
        data = [v for v in data if v['title'] != vacancy.title]  # Удаление по заголовку
        self.save_data(data)

    def load_data(self) -> Any:
        """Загрузка файла"""
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_data(self, data: Any) -> None:
        """Сохранение файла"""
        with open(self.filename, 'w') as file:
            json.dump(data, file, indent=4)


# Функция для фильтрации вакансий
def filter_vacancies(vacancies: dict, filter_words: Any) -> list:
    """Сортировка по ключевому слову, указанному пользователем"""
    return [v for v in vacancies if any(word in v.description for word in filter_words)]


def get_vacancies_by_salary(vacancies: list, salary_range: str) -> Any:
    """Сортировка по зарплате, указанной пользователем"""
    vacancies_by_salary = []
    min_salary, max_salary = map(int, salary_range.split(' - '))
    for vacancy in vacancies:
        salary_info = vacancy.salary  # Извлечение информации о зарплате
        if isinstance(salary_info, dict):
            salary_from = salary_info.get('from', 'не указано')
            salary_to = salary_info.get('to', 'не указано')
            if salary_to is not None and salary_from is not None:
                if int(salary_to) < max_salary or int(salary_from) > min_salary:
                    vacancies_by_salary.append(vacancy)
    return vacancies_by_salary


def sort_vacancies(vacancies: dict) -> list:
    """Сортировка по зарплате"""
    return sorted(vacancies, key=lambda v: v.salary['to'])


def get_top_vacancies(vacancies: list, n: int) -> Any:
    return vacancies[:n]


def print_vacancies(vacancies: dict) -> None:
    """Функция для печати"""
    for v in vacancies:
        print(f"{v.title} - {v.salary} - {v.description}")
