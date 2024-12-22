"""
Тестирование. Юнит тест, фикстуры.
Pytest.
"""
import unittest


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def setUpModule():
    print("UP модуля")


def tearDownModule():
    print("tearDown модуля")


class TestMathOperations(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # СОЗДАЕМ СОЕДИНЕНИЕ К БД
        print("Фикстура перед вызовом всех методов")

    @classmethod
    def tearDownClass(cls):
        # ЗАКРЫВАЕМ СОЕДИНЕНИЕ К БД
        print("Фикстура после вызова всех методов")

    def setUp(self):
        # используем созданное соединение для запроса в бд
        self.data = [
            {
                "name": "Diman",
                "age": 13
            }
        ]
        print("Фикстура перед вызовом метода")

    def tearDown(self):
        print("Фикстура после вызова метода")

    def test_add(self):
        self.assertEqual(add(3, 4), 7)

    def test_multiply(self):
        self.assertEqual(multiply(1, 2), 2)

    def test_wrong_test(self):
        self.assertNotEqual(add(3, 4), 9)

    def test_diman(self):
        self.assertIn("Diman", self.data[0].values())


if __name__ == "__main__":
    unittest.main()
