import os

import requests
from dotenv import load_dotenv


def convert_currency(transaction: dict) -> float:
    """Функция для расчета суммы транзакции.
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API (Exchange Rates Data API от APILayer)
    для получения текущего курса валют и конвертации суммы операции в рубли."""
    if not transaction or not isinstance(transaction, dict):  # Если транзакция не существует
        # или тип объекта - не словарь, возвращается сумма транзакции, равная нулю
        print("Отсутствуют данные о транзакции или данные неправильного типа.")
        return 0
    if transaction.get("operationAmount", {}).get("currency", {}).get("code") == "RUB":  # Если транзакция в рублях...
        transaction_amount = transaction.get("operationAmount", {}).get("amount", 0)  # Возвращается сумма транзакции
        return float(transaction_amount)

    else:  # Если транзакция в другой валюте, выполняем API-запрос на конвертацию валюты в рубли
        currency = transaction.get("operationAmount", {}).get("currency", {}).get("code")  # Текущая валюта
        amount = transaction.get("operationAmount", {}).get("amount", 0)  # Сумма транзакции в текущей валюте

        url = "https://api.apilayer.com/exchangerates_data/convert"  # URL для API-запроса текущих курсов валют
        # Ниже - параметры для конвертации (сумма, из какой валюты, в какую валюту)
        payload = {"amount": amount, "from": currency, "to": "RUB"}

        load_dotenv()  # Загрузка API-ключа из .env-файла
        api_key = os.getenv("API_KEY")
        # Ниже - заголовок запроса по API-ключу для авторизации на Exchange Rates Data
        headers: dict = {"apikey": api_key}
        response = requests.get(url, headers=headers, params=payload)  # API-запрос на конвертацию валюты
        if response.status_code != 200:  # Если запрос неудачный...
            print(f"Неудачная попытка получить курс валюты {currency}. Возможная причина: {response.reason}.")
            return 0
        response_json = response.json()  # Преобразование данных в JSON-объект
        transaction_amount = response_json.get("result")  # Извлечение из ответа от API конвертированной в рубли
        # суммы транзакции

        return float(transaction_amount)


#####################################################################################################
# Ниже - код для тестирования работы функции.
# Path_to_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
# Или можно задать такой путь:
# local_path = "../data/operations.json"
# Path_to_file = os.path.abspath(local_path)
# transactions = read_json_file(Path_to_file)
# print(transactions)
# for transaction in transactions:
#     print(convert_currency(transaction))
