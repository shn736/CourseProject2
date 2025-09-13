from unittest.mock import patch

from src.api import HeadHunterAPI


class TestHeadHunterAPI:

    @patch('src.api.requests.get')
    def test_get_vacancies_success(self, mock_get):
        """Проверяем успешный ответ от API"""
        api = HeadHunterAPI()

        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'items': []}

        result = api.get_vacancies('developer')

        assert result == {'items': []}
        mock_get.assert_called_once_with('https://api.hh.ru/vacancies', params={'text': 'developer'})

    @patch('src.api.requests.get')
    def test_get_vacancies_failure(self, mock_get):
        """Проверяем поведение при ошибочном ответе от API"""
        api = HeadHunterAPI()

        mock_get.return_value.status_code = 404  # Ошибка 404

        result = api.get_vacancies('developer')

        assert result == {}
        mock_get.assert_called_once_with('https://api.hh.ru/vacancies', params={'text': 'developer'})
