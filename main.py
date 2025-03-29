# Далее - код остался от предыдущих домашних заданий (получение исходных данных от пользователя через диалог).
# Удалить перед слиянием с основной веткой в случае его неактуальности.

# from src.masks import get_mask_card_number, get_mask_account
#
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
