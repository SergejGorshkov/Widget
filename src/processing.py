import re
from collections import Counter
from typing import Union


def filter_by_state(data_of_bank_operations: list[dict], key_state: str = "EXECUTED") -> list[dict]:
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


def sort_by_date(data_of_bank_operations: list[dict], sort_key: Union[str, bool] = "True") -> list[dict]:
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


def filter_operations_by_keyword(data_of_bank_operations: list[dict], keyword: str) -> list[dict]:
    """Функция принимает список словарей с информацией о банковских операциях и строку поиска.
     Поиск ведется в описании операции (по значению ключа "description").
    Возвращает новый список словарей, у которых в описании обнаружено совпадение с заданным значением.
    Если совпадения не найдены, возвращается пустой список."""
    # В генераторе списка проверяется, что тип значения ключа "description" - str (во избежание ошибок при
    # использовании метода re.search()), а также проверяется наличие заданной строки в описании операции
    # (без учета регистра)
    filtered_transactions = [
        transaction
        for transaction in data_of_bank_operations
        if (isinstance(transaction.get("description"), str) and re.search(keyword, transaction["description"],
                                                                          re.IGNORECASE))
    ]

    return filtered_transactions


def count_operations_by_category(data_of_bank_operations: list[dict], categories: list[str]) -> dict[str, int]:
    """Функция принимает список словарей с информацией о банковских операциях и список категорий операций для поиска.
     Поиск ведется в описании операции (по значению ключа "description").
    Возвращает словарь с названиями заданных категорий и соответствующим количеством операций в каждой категории."""
    # В объект Counter помещен генератор списка, в котором проверяется соответствие текста описания операции заданным
    # ключевым словам. Список с категориями для поиска (categories) сделан нечувствительным к регистру
    categories_counts = Counter(
        transaction["description"].lower()
        for transaction in data_of_bank_operations
        if transaction["description"].lower() in list(map(str.lower, categories))
    )

    return dict(categories_counts)
