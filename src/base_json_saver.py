from abc import ABC, abstractmethod

class AbstractSaver(ABC):
    """Абстрактный класс для сохранения вакансий"""
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass
