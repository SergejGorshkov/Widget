import json
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/utils.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path_to_file: str) -> list[dict]:
    """Функция чтения данных о финансовых транзакциях из JSON-файла.
    Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не-список или не найден, функция возвращает пустой список."""
    data_json = []  # По умолчанию данные отсутствуют
    try:
        logger.info("Чтение данных из JSON-файла...")
        with open(path_to_file, "r", encoding="UTF-8") as file:
            data_json = json.load(file)  # Если данные получены без ошибок, значение 'data_json' перезаписывается
            logger.info("Данные из JSON-файла успешно получены.")
    except json.JSONDecodeError:
        print("Ошибка декодирования файла.")
        logger.error("Произошла ошибка декодирования файла.")
    except FileNotFoundError:
        print(f"Ошибка! Файл по адресу {path_to_file} не найден.")
        logger.error(f"Ошибка! Файл по адресу {path_to_file} не найден.")

    if not isinstance(data_json, list):
        logger.warning("Данные из JSON-файла неправильного формата.")
        return []

    return data_json  # Возврат содержимого JSON-файла или пустого списка в случае, если файл пустой, содержит
    # не-список или не найден
