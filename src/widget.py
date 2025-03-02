import os  # Для тестирования функций
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number

# Константы путей к файлам для тестирования функций mask_account_card() и get_date()
# PATH_TO_TEST_MASK = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "for_testing_masks.txt")
# PATH_TO_TEST_DATE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "tests", "for_testing_date.txt")


def mask_account_card(data_for_mask: str) -> str:
    """
    Функция маскировки номера карты или счета. Принимает строку с названием и номером карты или счета.
    Возвращает название карты или счета с маской.
    """
    if isinstance(data_for_mask, str):  # Проверка на соответствие входных данных типу "str"
        data_list = data_for_mask.split(" ")  # Разбиение полученной строки на список, разделение - по пробелам
        for element in data_list:

            if element.isdigit():  # Если элемент списка - целое число, выполняем его проверку...
                if len(element) == 16:  # Если "длина" числа соответствует номеру карты...
                    return data_for_mask.replace(element, get_mask_card_number(element))  # Выполняем маскировку
                    # номера карты и замену номера на его маску в исходных данных
                elif len(element) == 20 and ("счет" in data_for_mask.lower() or "счёт" in data_for_mask.lower()):
                    # Если "длина" числа соответствует номеру счета и в исходных данных есть слово "счет" или "счёт"...
                    return data_for_mask.replace(element, get_mask_account(element))  # Выполняем маскировку
                    # номера счета и замену номера на его маску в исходных данных

        raise Exception("Ошибка! В исходных данных номер карты или счета не обнаружен или указан неверно.")
    else:
        raise Exception("Неверный тип исходных данных. Ожидается тип 'str'")




def get_date(date_for_change: str) -> str:
    """
    Функция форматирования даты. Принимает строку с датой в формате ISO 8601 и приводит ее к виду "ДД.ММ.ГГГГ".
    """
    if date_for_change:
        date_datetime = datetime.fromisoformat(date_for_change)
        return date_datetime.strftime("%d.%m.%Y")
    else:
        raise ValueError("Invalid isoformat string")



# Блок для тестирования функции mask_account_card()
# with open(PATH_TO_TEST_MASK, "r", encoding="utf-8") as file:  # Чтение файла для тестирования
#     numbers_list = file.readlines()  # чтение файла и построчное разделение на элементы списка
#     cleaned_number_list = [number.strip() for number in numbers_list]  # Очистка строк от символов переноса строки
#     for number in cleaned_number_list:
#         print(mask_account_card(number))
#
# Блок для тестирования функции get_date()
# with open(PATH_TO_TEST_DATE, "r", encoding="utf-8") as file:
#     numbers_list = file.readlines()
#     cleaned_number_list = [number.strip() for number in numbers_list]
#     for number in cleaned_number_list:
#         print(get_date(number))
