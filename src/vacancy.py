class Vacancy:
    def __init__(self, title, url, salary, description):
        self.title = title
        self.url = url
        self.salary = self.validate_salary(salary)
        self.description = description

    def validate_salary(self, salary):
        if not salary:
            return 0
        return salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __repr__(self):
        return f"Vacancy({self.title}, {self.url}, {self.salary}, {self.description})"

    @classmethod
    def cast_to_object_list(cls, data):
        vacancies = []
        for item in data['items']:
            vacancies.append(cls(
                item['name'],
                item['alternate_url'],
                item['salary'] or 0,
                item['snippet']['requirement']
            ))
        return vacancies
