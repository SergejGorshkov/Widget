import os

from src.processing import filter_by_state
from src.get_data_from_file import get_data_csv, get_data_excel
from src.utils import read_json_file

PATH_TO_JSON_FILE = os.path.join(os.path.dirname(__file__), "data", "operations.json")  # Путь к JSON-файлу
PATH_TO_CSV_FILE = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")  # Путь к CSV-файлу
PATH_TO_EXCEL_FILE = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")  # Путь к Excel-файлу

if __name__ == "__main__":
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
          "Для начала работы выберите необходимый пункт меню:\n"
          "1. Получить информацию о транзакциях из JSON-файла\n"
          "2. Получить информацию о транзакциях из CSV-файла\n"
          "3. Получить информацию о транзакциях из XLSX-файла")
    while True:
        try:
            answer = int(input("Введите 1, 2 или 3: ").replace(" ", ""))  # Удаление пробелов,
            # приведение к типу 'int' для проверки наличия нечисловых символов через обработку исключений
            if answer not in [1, 2, 3]:
                print("Ошибка. Введено значение вне указанного диапазона.")
                continue
        except ValueError:
            print("Ошибка: Введено нечисловое значение.")
        except Exception as error:
            print(f"Произошла ошибка: {error}")
        else:
            break

    selected_file = {1: "JSON", 2: "CSV", 3: "XLSX"}
    print(f"Для обработки выбран {selected_file[answer]}-файл.")

    if selected_file[answer] == "JSON":
        transactions = read_json_file(PATH_TO_JSON_FILE)
    elif selected_file[answer] == "CSV":
        transactions = get_data_csv(PATH_TO_CSV_FILE)
    elif selected_file[answer] == "XLSX":
        transactions = get_data_excel(PATH_TO_EXCEL_FILE)

    # print(transactions) # Для тестирования работы

    print("Введите статус, по которому необходимо выполнить фильтрацию (по умолчанию - 'EXECUTED').")
    while True:
        try:
            answer_key_state = input("Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ").replace(" ", "")

            if answer_key_state.upper() not in ["EXECUTED", "CANCELED", "PENDING"]:
                print(f"Ошибка. Введено неправильное значение. Статус операции '{answer_key_state}' недоступен.")
                continue
        except Exception as error:
            print(f"Произошла ошибка: {error}")
        else:
            break
    filtered_transactions = filter_by_state(transactions, answer_key_state)
    # print(filtered_transactions) # Для тестирования работы


