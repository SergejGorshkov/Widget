from unittest.mock import Mock, patch

import pytest

from src.external_api import convert_currency


@pytest.mark.parametrize(
    "transaction, expected",
    [
        (
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            },
            31957.58,
        ),
        (
            {
                "id": 41428829,
                "state": "EXECUTED",
                "date": "2019-07-03T18:35:29.512364",
                "operationAmount": {"amount": "8221.37", "currency": {"name": "RUB", "code": "RUB"}},
                "description": "Перевод организации",
                "from": "MasterCard 7158300734726758",
                "to": "Счет 35383033474447895560",
            },
            8221.37,
        ),
    ],
)
def test_external_api_success_if_rub(transaction, expected):
    """Тест на корректную обработку транзакций в валюте RUB"""
    assert convert_currency(transaction) == expected


def test_external_api_success_if_usd():
    """Тест на успешную конвертацию валюты по API-запросу"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "date": "2018-02-22",
        "historical": "",
        "info": {"rate": 148.972231, "timestamp": 1519328414},
        "query": {"amount": 10, "from": "USD", "to": "RUB"},
        "result": 840.9453,
        "success": True,
    }
    with patch("requests.get", return_value=mock_response):
        result = convert_currency({"operationAmount": {"amount": "10", "currency": {"name": "USD", "code": "USD"}}})
    assert result == 840.9453


def test_external_api_if_invalid_currency():
    """Тест на обработку транзакций в неподдерживаемой валюте"""
    mock_response = Mock()
    mock_response.status_code = 404
    with patch("requests.get", return_value=mock_response):
        result = convert_currency({"operationAmount": {"amount": "10", "currency": {"name": "ETH", "code": "ETH"}}})
    assert result == 0


def test_external_api_if_wrong_data():
    """Тест на обработку транзакций, если входные данные не-словарь (строка или пустой файл)"""
    assert convert_currency("some_string") == 0
    assert convert_currency({}) == 0
    assert convert_currency([]) == 0
