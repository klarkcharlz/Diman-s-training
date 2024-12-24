import unittest
from unittest.mock import patch

# from api_client import APIClient  # В реальности типо так


class APIClient:
    def get_data_from_api(self):
        # тут типа делаем реальный запрос к внешнему апи
        pass

    def process_data(self):
        data = self.get_data_from_api()
        return [x * 2 for x in data["data"]]


class TestAPIClientMonkey(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # заманкейпатчили
        cls.original_method = APIClient.get_data_from_api
        APIClient.get_data_from_api = lambda self_: {"status": "success", "data": [10, 20, 30]}

    @classmethod
    def tearDownClass(cls):
        # вернули обратно
        APIClient.get_data_from_api = cls.original_method

    def test_process_data_with_monkey_patching(self):
        # Тест с манкей патчингом
        client = APIClient()
        self.assertEqual(client.process_data(), [20, 40, 60])


class TestAPIClientMock(unittest.TestCase):

    @patch.object(APIClient, 'get_data_from_api', return_value={"status": "success", "data": [10, 20, 30]})
    def test_process_data_with_mock(self, mock_object):
        # print(mock_object)
        client = APIClient()
        self.assertEqual(client.process_data(), [20, 40, 60])
        # Проверяем, что метод был вызван
        mock_object.assert_called_once()


if __name__ == "__main__":
    unittest.main()
