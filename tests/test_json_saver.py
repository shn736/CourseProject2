import json
import pytest

from src.json_saver import JSONSaver


class DummyVacancy:
    def __init__(self, title, salary, description):
        self.title = title
        self.salary = salary
        self.description = description


@pytest.fixture
def json_saver(tmpdir):
    """Создание временного файла для тестирования"""
    filename = tmpdir.join("test_vacancies.json")
    saver = JSONSaver(str(filename))
    return saver


def test_add_vacancy(json_saver):
    """Тестирование добавления вакансии"""
    vacancy = DummyVacancy("Developer", {"from": 1000, "to": 2000}, "Python developer")
    json_saver.add_vacancy(vacancy)

    data = json_saver.load_data()
    assert len(data) == 1
    assert data[0]['title'] == "Developer"
    assert data[0]['salary'] == {"from": 1000, "to": 2000}
    assert data[0]['description'] == "Python developer"


def test_delete_vacancy(json_saver):
    """Тестирование удаления вакансии"""
    vacancy1 = DummyVacancy("Developer", {"from": 1000, "to": 2000}, "Python developer")
    vacancy2 = DummyVacancy("Designer", {"from": 800, "to": 1600}, "UI/UX designer")
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)

    json_saver.delete_vacancy(vacancy1)

    data = json_saver.load_data()
    assert len(data) == 1
    assert data[0]['title'] == "Designer"


def test_load_data_empty_file(json_saver):
    """Тестирование загрузки пустого файла"""
    data = json_saver.load_data()
    assert data == []


def test_save_data(json_saver):
    """Тестирование сохранения данных"""
    vacancy = DummyVacancy("Developer", {"from": 1000, "to": 2000}, "Python developer")
    json_saver.add_vacancy(vacancy)

    with open(json_saver.filename, 'r') as file:
        data = json.load(file)

    assert len(data) == 1
    assert data[0]['title'] == "Developer"
