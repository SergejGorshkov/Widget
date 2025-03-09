from typing import List, Dict

# Исходные данные о транзакциях для проверки работы функций filter_by_currency, transaction_descriptions
# transactions = (
#     [
#         {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         },
#         {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         },
#         {
#             "id": 873106923,
#             "state": "EXECUTED",
#             "date": "2019-03-23T01:09:46.296404",
#             "operationAmount": {
#                 "amount": "43318.34",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 44812258784861134719",
#             "to": "Счет 74489636417521191160"
#         },
#         {
#             "id": 895315941,
#             "state": "EXECUTED",
#             "date": "2018-08-19T04:27:37.904916",
#             "operationAmount": {
#                 "amount": "56883.54",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод с карты на карту",
#             "from": "Visa Classic 6831982476737658",
#             "to": "Visa Platinum 8990922113665229"
#         },
#         {
#             "id": 594226727,
#             "state": "CANCELED",
#             "date": "2018-09-12T21:27:25.241689",
#             "operationAmount": {
#                 "amount": "67314.70",
#                 "currency": {
#                     "name": "руб.",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Visa Platinum 1246377376343588",
#             "to": "Счет 14211924144426031657"
#         }
#     ]
# )


def filter_by_currency(data_of_bank_transactions: List[Dict[str, dict]], currency_code: str) -> List[Dict[str, dict]]:
    """Функция фильтрации транзакций по коду валюты.
     Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной (например, USD)."""
    if not data_of_bank_transactions:
        yield "Ошибка! Список транзакций пуст."
    try:
        filtered_data = list(filter(lambda transaction: transaction["operationAmount"]["currency"]["code"] ==
                                                        currency_code, data_of_bank_transactions))
        # Фильтрация данных о транзакциях по ключу "code" и заданному в переменной currency_code коду валюты
        if not filtered_data:  # Если в исходных данных не обнаружены транзакции по искомой валюте...
            yield f"Транзакций по валюте {currency_code} не найдено."
    except KeyError:  # Если в исходных данных в транзакции отсутствует ключ "code", прерывается выполнение функции
        yield f"Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'code'."
    else:
        for transaction in filtered_data:  # Вывод отфильтрованных данных
            yield transaction


def transaction_descriptions(data_of_bank_transactions: List[Dict[str, dict]]) -> str:
    if not data_of_bank_transactions:
        yield "Ошибка! Список транзакций пуст."
    try:
        description_list = [transaction["description"] for transaction in data_of_bank_transactions]
        # Создание списка из описаний транзакций по ключу "description"
        if not description_list:  # Если в исходных данных не обнаружены описания транзакций
            yield f"Описание транзакций не найдено."
    except KeyError:  # Если в исходных данных в транзакции отсутствует ключ "description", прерывается
        # выполнение функции
        yield f"Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'description'."
    else:
        for description in description_list:  # Вывод полученных данных
            yield description


def card_number_generator(start: int, stop: int):
    if not (1 <= start < 10000000000000000 and 1 <= stop < 10000000000000000 and start <= stop):
        raise Exception("Ошибка! Значения заданного диапазона номеров карт вне допустимых пределов.")
    number_generator = list()
    for i in range(start, stop + 1):
        number_str = "0" * (16 - len(str(i))) + str(i)  # Создание номера карты
        split_number = number_str[0:4] + " " + number_str[4:8] + " " + number_str[8:12] + " " + number_str[-4:]
        # Форматирование созданного номера карты в виде четырех блоков по 4 цифры
        number_generator.append(split_number)  # Заполнение списка номеров карт
    return number_generator

##############################################################################################
# usd_transactions = filter_by_currency(transactions, "USD")
# try:
#     for _ in range(10):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Поиск завершен.")
###############################################################################################
# descriptions = transaction_descriptions(transactions)
# try:
#     for _ in range(10):
#         print(next(descriptions))
# except StopIteration:
#     print("Поиск завершен.")
###############################################################################################
# try:
#     for card_number in card_number_generator(1, 2):
#         print(card_number)
# except Exception as error_info:
#     print(error_info)
