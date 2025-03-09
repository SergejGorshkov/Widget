from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(data_for_mask: str) -> str:
    """
    Функция маскировки номера карты или счета. Принимает строку с названием и номером карты или счета.
    Возвращает название карты или счета с маской.
    """
    if not isinstance(data_for_mask, str):  # Проверка на соответствие входных данных типу "str"
        raise Exception("Неверный тип исходных данных. Ожидается тип 'str'")

    data_list = data_for_mask.split(" ")  # Разбиение полученной строки на список, разделение - по пробелам
    for element in data_list:

        if element.isdigit():  # Если элемент списка - целое число, выполняем его проверку...
            if len(element) == 16:  # Если "длина" числа соответствует номеру карты...
                return data_for_mask.replace(element, get_mask_card_number(element))  # Выполняем маскировку
                # номера карты и замену номера на его маску в исходных данных
            elif len(element) == 20 and ("счет" in data_for_mask.lower() or "счёт" in data_for_mask.lower()):
                # Если "длина" числа соответствует номеру счета и в исходных данных есть слово "счет" или "счёт"
                return data_for_mask.replace(element, get_mask_account(element))  # Выполняем маскировку
                # номера счета и замену номера на его маску в исходных данных

    raise Exception("Ошибка! В исходных данных номер карты или счета не обнаружен или указан неверно.")


def get_date(date_for_change: str) -> str:
    """
    Функция форматирования даты. Принимает строку с датой в формате ISO 8601 и приводит ее к виду "ДД.ММ.ГГГГ".
    """
    if date_for_change:
        date_datetime = datetime.fromisoformat(date_for_change)
        return date_datetime.strftime("%d.%m.%Y")
    else:
        raise ValueError("Invalid isoformat string")
