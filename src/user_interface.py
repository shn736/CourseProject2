
from src.api import hh_vacancies
from src.vacancy import Vacancy


def filter_vacancies(vacancies, keywords):
    return [vacancy for vacancy in vacancies if any(keyword in vacancy.description for keyword in keywords)]

vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)
print(filter_vacancies(vacancies_list, 'Москва'))

def get_vacancies_by_salary(vacancies, salary_range):
    for v in vacancies:

            print(v.salary['to'])


    # min_salary, max_salary = map(int, salary_range.split(' - '))
    # return [vacancy for vacancy in vacancies if
    #         isinstance(vacancy.salary, int) and min_salary <= vacancy.salary <= max_salary]

print(get_vacancies_by_salary(vacancies_list,  10000))

def sort_vacancies(vacancies):
    return sorted(vacancies)


def get_top_vacancies(vacancies, n):
    return vacancies[:n]


def print_vacancies(vacancies):
    for vacancy in vacancies:
        print(vacancy)

