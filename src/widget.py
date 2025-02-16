import os  # Для тестирования функций
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

# Константы путей к файлам для тестирования функций mask_account_card() и get_date()
PATH_TO_TEST_MASK = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "for_testing_masks.txt")
PATH_TO_TEST_DATE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "for_testing_date.txt")


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


# Блок для тестирования функции mask_account_card()
with open(PATH_TO_TEST_MASK, "r", encoding="utf-8") as file:
    numbers_list = file.readlines()  # чтение файла и построчное разделение на элементы списка
    cleaned_number_list = [number.strip() for number in numbers_list]
    for number in cleaned_number_list:
        print(mask_account_card(number))

# Блок для тестирования функции get_date()
with open(PATH_TO_TEST_DATE, "r", encoding="utf-8") as file:
    numbers_list = file.readlines()  # чтение файла и построчное разделение на элементы списка
    cleaned_number_list = [number.strip() for number in numbers_list]
    for number in cleaned_number_list:
        print(get_date(number))
