import unittest
from unittest.mock import mock_open, patch

from utils import read_json_file


class TestReadJsonFile(unittest.TestCase):
    # Создание класса тестов TestReadJsonFile для написания тестов на открытие файлов

    @patch("builtins.open", new_callable=mock_open, read_data='[{"id": 22222222}, {"id": 1111111111}]')
    # Декоратор, заменяющий встроенную функцию 'open' на 'mock_open', который симулирует поведение чтения файлов.
    # read_data=... указание данных, которые "читаются" из mock-файла.
    def test_read_json_file_success(self, mock_file):
        # self ссылается на экземпляр тестового класса, что позволяет использовать методы unittest.TestCase.
        # mock_file — объект, который был создан при использовании декоратора @patch. Подделка для функции open,
        # имитирует файл, в котором содержится корректный JSON.
        """Тест на корректное чтение JSON-файла"""
        result = read_json_file("some_path_to_file.json")
        self.assertEqual(result, [{"id": 22222222}, {"id": 1111111111}])

    @patch("builtins.open", new_callable=mock_open, read_data="")
    def test_read_json_file_empty_file(self, mock_file):
        """Тест на корректное чтение пустого файла"""
        result = read_json_file("some_path_to_file.json")
        self.assertEqual(result, [])

    @patch("builtins.open", new_callable=mock_open, read_data="wrong data")
    def test_read_json_file_if_wrong_data(self, mock_file):
        """Тест на чтение файла с некорректным содержимым JSON-файла"""
        result = read_json_file("some_path_to_file.json")
        self.assertEqual(result, [])

    @patch("builtins.open", side_effect=FileNotFoundError)
    # side_effect=FileNotFoundError означает, что при попытке открыть файл будет возбуждена ошибка FileNotFoundError.
    def test_read_json_file_if_wrong_path(self, mock_file):
        """Тест на случай, когда файл не найден"""
        result = read_json_file("some_path_to_file.json")
        self.assertEqual(result, [])
