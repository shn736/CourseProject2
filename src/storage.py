import json
from abc import ABC, abstractmethod
from vacancy import Vacancy

# Интерфейс для работы с файлами
class AbstractVacancyStorage(ABC):

    @abstractmethod
    def save_to_file(self, vacancies):
        pass

    @abstractmethod
    def load_from_file(self):
        pass

    @abstractmethod
    def delete_vacancy(self, title):
        pass

# Класс для сохранения информации о вакансиях в JSON файл
class JsonFileStorage(AbstractVacancyStorage):

    def __init__(self, file_name):
        self.file_name = file_name

    def save_to_file(self, vacancies):
        with open(self.file_name, 'w', encoding='utf-8') as f:
            json.dump([v.__dict__ for v in vacancies], f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as f:
                vacancies_data = json.load(f)
                return [Vacancy(data) for data in vacancies_data]
        except FileNotFoundError:
            return []

    def delete_vacancy(self, title):
        vacancies = self.load_from_file()
        vacancies = [v for v in vacancies if v.title != title]
        self.save_to_file(vacancies)
