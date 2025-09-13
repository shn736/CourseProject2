from abc import ABC, abstractmethod


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancies(self, query):
        pass
