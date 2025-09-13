from src.vacancy import Vacancy


def test_initialization():
    vacancy = Vacancy("Software Engineer", "http://example.com", 100000, "Experience in Python")
    assert vacancy.title == "Software Engineer"
    assert vacancy.url == "http://example.com"
    assert vacancy.salary == 100000
    assert vacancy.description == "Experience in Python"


def test_validate_salary():
    vacancy_with_salary = Vacancy("Developer", "http://example.com", 50000, "Developer skills")
    vacancy_without_salary = Vacancy("Designer", "http://example.com", None, "Design skills")

    assert vacancy_with_salary.salary == 50000
    assert vacancy_without_salary.salary == 0


def test_less_than_operator():
    vacancy1 = Vacancy("Junior Developer", "http://example.com", 60000, "Junior dev skills")
    vacancy2 = Vacancy("Senior Developer", "http://example.com", 90000, "Senior dev skills")

    assert vacancy1 < vacancy2
    assert not vacancy2 < vacancy1


def test_repr():
    vacancy = Vacancy("Data Scientist", "http://example.com", 120000, "Data analysis and algorithms")
    assert repr(vacancy) == "Vacancy(Data Scientist, http://example.com, 120000, Data analysis and algorithms)"


def test_cast_to_object_list():
    data = {
        'items': [
            {
                'name': 'Python Developer',
                'alternate_url': 'http://example.com/python',
                'salary': 70000,
                'snippet': {'requirement': 'Python, Django'}
            },
            {
                'name': 'Java Developer',
                'alternate_url': 'http://example.com/java',
                'salary': None,
                'snippet': {'requirement': 'Java, Spring'}
            }
        ]
    }

    vacancies = Vacancy.cast_to_object_list(data)
    assert len(vacancies) == 2
    assert vacancies[0].title == "Python Developer"
    assert vacancies[0].salary == 70000
    assert vacancies[1].title == "Java Developer"
    assert vacancies[1].salary == 0
