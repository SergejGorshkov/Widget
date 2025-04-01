from unittest.mock import Mock, patch

from src.get_data_from_file import get_data_csv, get_data_excel


def test_get_data_csv_success():
    """Тест на корректное чтение CSV-файла"""
    # Создание Mock для DataFrame
    mock_df = Mock()
    mock_df.empty = False  # Обход проверки условия, что полученные данные отсутствуют
    # Присвоение ожидаемого результата объекту df.to_dict() в функции
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    # Замена объекта pd.read_csv из модуля get_data_from_file.py на ранее созданный и настроенный объект Mock
    with patch("src.get_data_from_file.pd.read_csv", return_value=mock_df):
        expected_result = [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        assert get_data_csv("some_path_to_file.csv") == expected_result
        mock_df.to_dict.assert_called_once_with(orient="records")


def test_get_data_csv_if_not_found():
    """Тест на корректное чтение, если файл не найден"""
    assert get_data_csv("some_path_to_file.csv") == []


def test_get_data_csv_empty_data():
    """Тест на корректное чтение CSV-файла, если он пустой"""
    # Создание Mock для DataFrame
    mock_df = Mock()
    mock_df.empty = True  # Задается условие, что полученные данные отсутствуют
    assert get_data_csv("some_path_to_file.csv") == []


#####################
def test_get_data_excel_success():
    """Тест на корректное чтение Excel-файла"""
    # Создание Mock для DataFrame
    mock_df = Mock()
    mock_df.empty = False  # Обход проверки условия, что полученные данные отсутствуют
    # Присвоение ожидаемого результата объекту df.to_dict() в функции
    mock_df.to_dict.return_value = [
        {
            "id": 650703.0,
            "state": "EXECUTED",
            "date": "2023-09-05T11:30:32Z",
            "amount": 16210.0,
            "currency_name": "Sol",
            "currency_code": "PEN",
            "from": "Счет 58803664561298323391",
            "to": "Счет 39745660563456619397",
            "description": "Перевод организации",
        }
    ]

    # Замена объекта pd.read_excel из модуля get_data_from_file.py на ранее созданный и настроенный объект Mock
    with patch("src.get_data_from_file.pd.read_excel", return_value=mock_df):
        expected_result = [
            {
                "id": 650703.0,
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": 16210.0,
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]
        assert get_data_excel("some_path_to_file.excel") == expected_result
        mock_df.to_dict.assert_called_once_with(orient="records")


def test_get_data_excel_if_not_found():
    """Тест на корректное чтение Excel-файла, если файл не найден"""
    assert get_data_excel("some_path_to_file.excel") == []


def test_get_data_excel_empty_data():
    """Тест на корректное чтение Excel-файла, если он пустой"""
    # Создание Mock для DataFrame
    mock_df = Mock()
    mock_df.empty = True  # Задается условие, что полученные данные отсутствуют
    assert get_data_excel("some_path_to_file.excel") == []
