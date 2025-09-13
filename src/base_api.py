from abc import ABC, abstractmethod
from typing import Any


class AbstractAPI(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancies(self, query: str) -> Any:
        pass
