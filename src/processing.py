def filter_by_state(data_of_bank_operations: list[dict[str, [str | int]]], key_state: str="EXECUTED") \
        -> list[dict[str, [str | int]]]:
    """Функция принимает список словарей и, опционально, значение для ключа "state" (по умолчанию "EXECUTED").
    Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному
    значению."""

    filtered_list = [operation for operation in data_of_bank_operations if operation.get("state") == key_state]
    return filtered_list


def sort_by_date(data_of_bank_operations: list[dict[str, [str | int]]], sort_key: str="True"):
    """Функция принимает список словарей и необязательный параметр (sort_key) в виде строки,
    задающий порядок сортировки (по умолчанию — убывание).
    Возвращает новый список, отсортированный по дате."""

    if sort_key.lower() == "true":
        sort_key = True
    elif sort_key.lower() == "false":
        sort_key = False
    # Блок проверки значения ключа для направления сортировки данных по дате

    sorted_data = sorted(data_of_bank_operations, key=lambda operation: operation.get("date"), reverse=sort_key)
    return sorted_data
