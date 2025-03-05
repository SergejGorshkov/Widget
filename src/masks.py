"""
Модуль 'masks' предназначен для получения от модуля `widget.py` номера банковской карты (16 цифр)
(например: 3232323245456565) и номера счета (20 цифр) (например: 90903209302935646897) и
формирования их масок в формате '3232 32** **** 6565' и '**6897' соответственно.
"""


def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера банковской карты"""
    mask_card_number = number[0:4] + " " + number[4:6] + "**" + " " + "****" + " " + number[-4:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account_number = "**" + number[-4:]
    return mask_account_number


# Далее - код остался от предыдущих домашних заданий (получение исходных данных от пользователя через диалог).
# Удалить перед слиянием с основной веткой в случае его неактуальности.

# if __name__ == "__main__":
#     while True:
#         try:
#             card_number = int(input("Введите номер карты (16 цифр): ").replace(" ", ""))
#             # Удаление пробелов, приведение к типу 'int' для проверки наличия нечисловых символов
#             # через обработку исключений
#             if len(str(card_number)) != 16:
#                 raise Exception("Номер карты введен неверно. Количество цифр должно быть 16.")
#         except ValueError:
#             print("Ошибка: Введено нечисловое значение.")
#         except Exception as e:
#             print(f"Произошла ошибка. {e}")
#         else:
#             break
#
#     while True:
#         try:
#             account_number = int(input("Введите номер счета (20 цифр): ").replace(" ", ""))
#             # Удаление пробелов, приведение к типу 'int' для проверки наличия нечисловых символов
#             if len(str(account_number)) != 20:
#                 raise Exception("Номер счета введен неверно. Количество цифр должно быть 20.")
#         except ValueError:
#             print("Ошибка: Введено нечисловое значение.")
#         except Exception as e:
#             print(f"Произошла ошибка. {e}")
#         else:
#             break
#
#     print(f"Маска карты: {get_mask_card_number(str(card_number))}.")
#     print(f"Маска счета: {get_mask_account(str(account_number))}.")
