from abc import ABC, abstractmethod
from typing import Any


class AbstractSaver(ABC):
    """Абстрактный класс для сохранения вакансий"""
    @abstractmethod
    def add_vacancy(self, vacancy: list) -> Any:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: list) -> Any:
        pass
