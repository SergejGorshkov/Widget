from datetime import datetime

from src.masks import get_mask_card_number
from src.masks import get_mask_account


def mask_account_card(data_for_mask: str) -> str:
    """
    Функция маскировки номера карты или счета. Принимает строку с названием и номером карты или счета.
    Возвращает название карты или счета с маской.
    """
    data_list = data_for_mask.split(" ")
    for element in data_list:
        if element.isdigit():
            if len(element) == 16:
                result = data_for_mask.replace(element, get_mask_card_number(element))
                break
            elif len(element) == 20:
                result = data_for_mask.replace(element, get_mask_account(element))
                break
        result = f"Ошибка! В данных '{data_for_mask}' номер карты или счета не обнаружен."

    return result


def get_date(date_for_change: str) -> str:
    """
    Функция форматирования даты. Принимает строку с датой в формате ISO 8601 и приводит ее к виду "ДД.ММ.ГГГГ".
    """
    date_datetime = datetime.fromisoformat(date_for_change)
    formatted_date = date_datetime.strftime("%d.%m.%Y")

    return formatted_date
