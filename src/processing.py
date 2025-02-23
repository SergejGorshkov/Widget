def filter_by_state(data_of_bank_operations: list[dict[str, [str | int]]], key_state: str="EXECUTED") \
        -> list[dict[str, [str | int]]]:
    """Функция принимает список словарей и, опционально, значение для ключа "state" (по умолчанию "EXECUTED").
    Возвращает новый список словарей, содержащий только те словари, у которых ключ state соответствует указанному
    значению."""

    filtered_list = [operation for operation in data_of_bank_operations if operation.get("state") == key_state]
    return filtered_list
