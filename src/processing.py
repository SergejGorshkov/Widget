from typing import Dict, List, Union


def filter_by_state(
    data_of_bank_operations: List[Dict[str, Union[str, int]]], key_state: str = "EXECUTED"
) -> List[Dict[str, Union[str, int]]]:
    """Функция принимает список словарей и, опционально, значение для ключа "state" (по умолчанию "EXECUTED").
    Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному
    значению."""

    if isinstance(data_of_bank_operations, list) and all(isinstance(item, dict) for item in data_of_bank_operations):
        # Проверка, что исходные данные банковских операций представлены в виде списка словарей
        filtered_list = [
            operation for operation in data_of_bank_operations if operation.get("state") == key_state.upper()
        ]
        return filtered_list
    else:
        raise Exception("Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'")


def sort_by_date(
    data_of_bank_operations: List[Dict[str, Union[str, int]]], sort_key: Union[str, bool] = "True"
) -> List[Dict[str, Union[str, int]]]:
    """Функция принимает список словарей и необязательный параметр (sort_key) в виде строки,
    задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате."""

    if isinstance(data_of_bank_operations, list) and all(isinstance(item, dict) for item in data_of_bank_operations):
        #  Проверка, что исходные данные банковских операций представлены в виде списка словарей

        if isinstance(sort_key, str):
            # Если ключ для определения направления сортировки - строка, выполняем анализ его значения
            if sort_key.lower() == "true":
                sort_key = True
            elif sort_key.lower() == "false":
                sort_key = False
            else:
                raise ValueError("Invalid value for sort_key")
            # Блок проверки значения ключа для направления сортировки данных по дате

        sorted_data = sorted(
            data_of_bank_operations, key=lambda operation: operation.get("date", ""), reverse=sort_key
        )
        return sorted_data
    else:
        raise Exception("Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'")
