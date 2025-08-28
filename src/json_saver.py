from src.base_json_saver import AbstractFileSaver
import json


class JSONSaver(AbstractFileSaver):
    def __init__(self, filename='../data/vacancies.json'):
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

