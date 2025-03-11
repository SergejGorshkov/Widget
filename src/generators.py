from typing import Dict, Generator, List


def filter_by_currency(data_of_bank_transactions: List[Dict[str, dict]], currency_code: str) -> Generator:
    """Функция фильтрации транзакций по коду валюты.
     Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    (например, USD)."""
    if not data_of_bank_transactions:
        yield "Ошибка! Список транзакций пуст."
    try:
        filtered_data = list(
            filter(
                lambda transaction: transaction["operationAmount"]["currency"]["code"] == currency_code,
                data_of_bank_transactions,
            )
        )
        # Фильтрация данных о транзакциях по ключу "code" и заданному в переменной currency_code коду валюты
        if not filtered_data:  # Если в исходных данных не обнаружены транзакции по искомой валюте...
            yield f"Транзакции по валюте {currency_code} не найдены."
    except KeyError:  # Если в исходных данных в транзакции отсутствует ключ "code", прерывается выполнение функции
        yield "Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'code'."
    else:
        for transaction_data in filtered_data:  # Вывод отфильтрованных данных
            yield transaction_data


def transaction_descriptions(data_of_bank_transactions: List[Dict[str, dict]]) -> Generator:
    """Функция, которая принимает список словарей с транзакциями и ключу 'description' возвращает описание
    каждой операции по очереди."""
    if not data_of_bank_transactions:
        yield "Ошибка! Список транзакций пуст."

    try:
        description_list = [
            transaction["description"] for transaction in data_of_bank_transactions if transaction["description"] != ""
        ]
        # Создание списка из описаний транзакций по ключу "description". Если нет описания, транзакция игнорируется

        if not description_list:  # Если в исходных данных не обнаружены описания транзакций
            yield "Описание транзакций не найдено."
    except KeyError:  # Если в исходных данных в транзакции отсутствует ключ "description", прерывается
        # выполнение функции
        yield "Ошибка! Как минимум, в одной из транзакций отсутствует ключ 'description'."
    else:
        for description in description_list:  # Вывод полученных данных
            yield description


def card_number_generator(start: int, stop: int) -> list[str]:
    """Функция, которая выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Функция может генерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Принимает начальное и конечное значения для генерации диапазона номеров."""
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
# Запуск функции filter_by_currency. Данные для тестирования - см. в conftest.py.
# usd_transactions = filter_by_currency(transactions_data, "USD")
# try:
#     for _ in range(10):
#         print(next(usd_transactions))
# except StopIteration:
#     print("Поиск завершен.")
###############################################################################################
# Запуск функции transaction_descriptions. Данные для тестирования - см. в conftest.py.
# descriptions = transaction_descriptions(transactions_data)
# try:
#     for _ in range(10):
#         print(next(descriptions))
# except StopIteration:
#     print("Поиск завершен.")
###############################################################################################
# Запуск функции card_number_generator
# try:
#     for card_number in card_number_generator(1, 11):
#         print(card_number)
# except Exception as error_info:
#     print(error_info)
