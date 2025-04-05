from typing import Generator


def filter_by_currency(data_of_bank_transactions: list[dict], currency_code: str) -> Generator:
    """Функция фильтрации транзакций по коду валюты.
     Принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной
    (например, USD)."""
    if not data_of_bank_transactions:
        print("Ошибка! Список транзакций пуст.")
        yield

    # Фильтрация данных о транзакциях по ключу "code" и заданному в переменной currency_code коду валюты
    filtered_data = list(
        filter(
            lambda transaction: (transaction.get("operationAmount", {}).get("currency", {}).get(
                "code") == currency_code.upper() or (transaction.get("currency_code") == currency_code.upper())),
            data_of_bank_transactions))

    if not filtered_data:  # Если в исходных данных не обнаружены транзакции по искомой валюте...
        print(f"Транзакции по валюте '{currency_code.upper()}' не найдены.")
        yield
    else:
        for transaction_data in filtered_data:  # Вывод отфильтрованных данных
            yield transaction_data


def transaction_descriptions(data_of_bank_transactions: list[dict]) -> Generator:
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
