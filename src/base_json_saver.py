from abc import ABC, abstractmethod

# Абстрактный класс для работы с файлами
class AbstractFileSaver(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass
