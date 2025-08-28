from abc import ABC, abstractmethod


# Абстрактный класс для работы с API
class JobAPI(ABC):
    @abstractmethod
    def get_vacancies(self, query):
        pass

