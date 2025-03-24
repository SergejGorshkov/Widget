import json

# import os
# Path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
# Путь для тестирования работы функции


def read_json_file(path_to_file: str) -> list[dict]:
    """Функция чтения данных о финансовых транзакций из JSON-файла.
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не-список или не найден, функция возвращает пустой список."""
    data_json = []  # По умолчанию данные отсутствуют
    try:
        with open(path_to_file, "r", encoding="UTF-8") as file:
            data_json = json.load(file)  # Если данные получены без ошибок, значение 'data_json' перезаписывается
    except json.JSONDecodeError:
        print("Ошибка декодирования файла.")
    except FileNotFoundError:
        print(f"Ошибка! Файл по адресу {path_to_file} не найден.")

    return data_json  # Возврат содержимого JSON-файла или пустого списка в случае, если файл пустой, содержит
    # не-список или не найден


#################################################################################################################

# print(read_json_file(Path_to_file))
# Для тестирования работы функции
