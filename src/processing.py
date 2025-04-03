import re
from collections import Counter
from typing import Dict, List, Union


def filter_by_state(
        data_of_bank_operations: List[Dict[str, Union[str, int]]], key_state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """Функция принимает список словарей с информацией о банковских операциях и, опционально, значение для ключа
    "state" (по умолчанию "EXECUTED").
    Возвращает новый список словарей, содержащий только те словари, у которых ключ "state" соответствует указанному
    значению."""

    if not isinstance(data_of_bank_operations, list) or not all(
            isinstance(item, dict) for item in data_of_bank_operations
    ):
        raise Exception("Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'")
        # Проверка, что исходные данные банковских операций представлены в виде списка словарей
    filtered_list = [operation for operation in data_of_bank_operations if operation.get("state") == key_state.upper()]
    return filtered_list


def sort_by_date(
        data_of_bank_operations: List[Dict[str, Union[str, int]]], sort_key: Union[str, bool] = "True"
) -> List[Dict[str, Union[str, int]]]:
    """Функция принимает список словарей с информацией о банковских операциях и необязательный параметр (sort_key)
    в виде строки, задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате."""

    if not isinstance(data_of_bank_operations, list) or not all(
            isinstance(item, dict) for item in data_of_bank_operations
    ):
        #  Проверка, что исходные данные банковских операций представлены в виде списка словарей
        raise Exception("Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'")

    if isinstance(sort_key, str):
        # Если ключ для определения направления сортировки - строка, выполняем анализ его значения
        if sort_key.lower() == "true":
            sort_key = True
        elif sort_key.lower() == "false":
            sort_key = False
        else:
            raise ValueError("Неверное значение для ключа 'sort_key'. Ожидается значение 'True' или 'False'.")
        # Блок проверки значения ключа для направления сортировки данных по дате

    sorted_data = sorted(data_of_bank_operations, key=lambda operation: operation.get("date", ""), reverse=sort_key)
    return sorted_data


###################
# transactions = [
#     {
#         "id": 939719570,
#         "state": "EXECUTED",
#         "date": "2018-06-30T02:08:58.425572",
#         "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод организации",
#         "from": "Счет 75106830613657916952",
#         "to": "Счет 11776614605963066702",
#     },
#     {
#         "id": 142264268,
#         "state": "EXECUTED",
#         "date": "2019-04-04T23:20:05.206878",
#         "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 19708645243227258542",
#         "to": "Счет 75651667383060284188",
#     },
#     {
#         "id": 873106923,
#         "state": "EXECUTED",
#         "date": "2019-03-23T01:09:46.296404",
#         "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод со счета на счет",
#         "from": "Счет 44812258784861134719",
#         "to": "Счет 74489636417521191160",
#     },
#     {
#         "id": 895315941,
#         "state": "EXECUTED",
#         "date": "2018-08-19T04:27:37.904916",
#         "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
#         "description": "",
#         "from": "Visa Classic 6831982476737658",
#         "to": "Visa Platinum 8990922113665229",
#     },
#     {
#         "id": 594226727,
#         "state": "CANCELED",
#         "date": "2018-09-12T21:27:25.241689",
#         "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
#         "description": "Перевод организации",
#         "from": "Visa Platinum 1246377376343588",
#         "to": "Счет 14211924144426031657",
#     },
# ]


def filter_operations_by_keyword(data_of_bank_operations: List[Dict[str, Union[str, int]]], keyword: str
                                 ) -> List[Dict[str, Union[str, int]]]:
    """Функция принимает список словарей с информацией о банковских операциях и строку поиска.
     Поиск ведется в описании операции (по значению ключа "description").
    Возвращает новый список словарей, у которых в описании обнаружено совпадение с заданным значением."""
    # В генераторе списка проверяется, что тип значения ключа "description" - str (во избежание ошибок при
    # использовании метода re.search()), а также проверяется наличие заданной строки в описании операции
    filtered_transactions = [transaction for transaction in data_of_bank_operations
                             if (isinstance(transaction["description"], str)
                                 and re.search(keyword, transaction["description"], re.IGNORECASE))]

    return filtered_transactions


def count_operations_by_category(data_of_bank_operations: List[Dict[str, Union[str, int]]], categories: list[str]
                                 ) -> dict[str, int]:
    """Функция принимает список словарей с информацией о банковских операциях и список категорий операций для поиска.
     Поиск ведется в описании операции (по значению ключа "description").
    Возвращает словарь с названиями заданных категорий и соответствующим количеством операций в каждой категории."""
    # В объект Counter помещен генератор списка, в котором проверяется соответствие текста описания операции заданным
    # ключевым словам. Список с категориями для поиска (categories) сделан нечувствительным к регистру
    categories_counts = Counter(transaction["description"].lower() for transaction in data_of_bank_operations
                                if transaction["description"].lower() in list(map(str.lower, categories)))

    return dict(categories_counts)

# filter_operations_by_keyword(transactions, "пеРевод")
# count_operations_by_category(transactions, ["ПерЕвод со счета на счет", "Перевод организации"])
