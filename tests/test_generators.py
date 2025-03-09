import pytest

from generators import filter_by_currency, transaction_descriptions, card_number_generator


# Тестирование функции filter_by_currency
def test_filter_by_currency(transactions_data_for_generators):
    """Проверка правильности фильтрации списка словарей по заданным ключам."""
    usd_transactions = filter_by_currency(transactions_data_for_generators, "USD")
    assert next(usd_transactions) == {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                                      'operationAmount': {'amount': '9824.07',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                                      'to': 'Счет 11776614605963066702'}
    assert next(usd_transactions) == {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                                      'operationAmount': {'amount': '79114.93',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                                      'to': 'Счет 75651667383060284188'}
    assert next(usd_transactions) == {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916',
                                      'operationAmount': {'amount': '56883.54',
                                                          'currency': {'name': 'USD', 'code': 'USD'}},
                                      'description': '',
                                      'from': 'Visa Classic 6831982476737658',
                                      'to': 'Visa Platinum 8990922113665229'}


def test_filter_by_currency_with_missing_key(transactions_data_for_generators):
    """Проверка правильности фильтрации списка словарей, если значение по ключу отсутствует в исходных данных."""
    eur_transactions = filter_by_currency(transactions_data_for_generators, "EUR")
    assert next(eur_transactions) == "Транзакции по валюте EUR не найдены."


def test_filter_by_currency_with_empty_data():
    """Проверка правильности фильтрации списка словарей, если он пустой."""
    usd_transactions = filter_by_currency([], "USD")
    assert next(usd_transactions) == "Ошибка! Список транзакций пуст."


def test_filter_by_currency_without_key_in_data():
    """Проверка правильности фильтрации списка словарей, если в исходных данных пропущен ключ 'code'."""
    transaction = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                    'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'cooode': 'USD'}},
                    'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                    'to': 'Счет 11776614605963066702'},
                   {'id': 142264333, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                    'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'cooode': 'RUB'}},
                    'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                    'to': 'Счет 75651667383060284188'},
                   ]
    usd_transactions = filter_by_currency(transaction, "USD")
    assert next(usd_transactions) == "Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'code'."


##########################################################################################################
# Тестирование функции transaction_descriptions
def test_transaction_descriptions(transactions_data_for_generators):
    """Проверка правильности вывода описаний каждой операции."""
    descriptions = transaction_descriptions(transactions_data_for_generators)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"


def test_transaction_descriptions_with_empty_key_value():
    """Проверка правильности фильтрации списка словарей, если все значения по ключу 'description' отсутствуют
    в исходных данных, т.е. итоговый список с описаниями операций пуст."""
    transaction = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                    'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                    'description': '', 'from': 'Счет 75106830613657916952',
                    'to': 'Счет 11776614605963066702'},
                   {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                    'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                    'description': '', 'from': 'Счет 19708645243227258542',
                    'to': 'Счет 75651667383060284188'},
                   ]
    descriptions = transaction_descriptions(transaction)
    assert next(descriptions) == "Описание транзакций не найдено."


def test_transaction_descriptions_with_empty_data():
    """Проверка правильности обработки списка словарей, если он пустой."""
    descriptions = transaction_descriptions([])
    assert next(descriptions) == "Ошибка! Список транзакций пуст."


def test_transaction_descriptions_without_key_in_data():
    """Проверка правильности обработки списка словарей, если в исходных данных пропущен ключ 'description'."""
    transaction = [{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
                    'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
                    'dddescription': 'Перевод организации', 'from': 'Счет 75106830613657916952',
                    'to': 'Счет 11776614605963066702'},
                   {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
                    'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
                    'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
                    'to': 'Счет 75651667383060284188'},
                   ]
    descriptions = transaction_descriptions(transaction)
    assert next(descriptions) == "Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'description'."


##########################################################################################################
# Тестирование функции card_number_generator
@pytest.mark.parametrize("start, stop, expected", [
    (1, 3, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003']),
    (1, 10, ['0000 0000 0000 0001', '0000 0000 0000 0002', '0000 0000 0000 0003', '0000 0000 0000 0004',
             '0000 0000 0000 0005', '0000 0000 0000 0006', '0000 0000 0000 0007', '0000 0000 0000 0008',
             '0000 0000 0000 0009', '0000 0000 0000 0010']),
    (1, 1, ['0000 0000 0000 0001']),
]
                         )
def test_card_number_generator(start, stop, expected):
    """Проверка правильности генерирования номеров банковских карт в заданном диапазоне."""
    assert card_number_generator(start, stop) == expected


def test_card_number_generator_if_out_of_range():
    """Проверка поведения функции, если заданный диапазон номеров карт находится вне допустимых пределов."""
    with pytest.raises(Exception) as error_info:
        card_number_generator(0, 2)
    assert str(error_info.value) == "Ошибка! Значения заданного диапазона номеров карт вне допустимых пределов."

    with pytest.raises(Exception) as error_info:
        card_number_generator(1, 10000000000000000)
    assert str(error_info.value) == "Ошибка! Значения заданного диапазона номеров карт вне допустимых пределов."
