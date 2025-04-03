# import json
# import os
import pandas as pd


def get_data_csv(path: str) -> list[dict]:
    """Функция считывания финансовых операций из CSV-файлов.
    Принимает в качестве аргумента путь к CSV-файлу.
    Возвращает список словарей с транзакциями."""
    try:
        df = pd.read_csv(path, sep=",|;", engine="python")  # Получение объекта DataFrame с данными.
        # В качестве разделителя при чтении CSV-файла может использоваться ',' или ';'
        if not df.empty:  # Если данные есть...
            transactions = df.to_dict(orient="records")  # Преобразование данных в список словарей
            return transactions
        else:
            raise ValueError("CSV-файл пуст!")
    except FileNotFoundError:
        print("При чтении CSV-файла возникла ошибка: файл не найден.")
        return []
    except Exception as error_info:
        print(f"При чтении CSV-файла возникла ошибка: {error_info}.")
        return []
    except ValueError as error_info:
        print(error_info)
        return []


def get_data_excel(path: str) -> list[dict]:
    """Функция считывания финансовых операций из Excel-файлов.
    Принимает в качестве аргумента путь к Excel-файлу.
    Возвращает список словарей с транзакциями."""
    try:
        df = pd.read_excel(path)  # Получение объекта DataFrame с данными
        if not df.empty:  # Если данные есть...
            transactions = df.to_dict(orient="records")  # Преобразование данных в список словарей
            return transactions
        else:
            raise ValueError("Excel-файл пуст!")
    except FileNotFoundError:
        print("При чтении Excel-файла возникла ошибка: файл не найден.")
        return []
    except Exception as error_info:
        print(f"При чтении Excel-файла возникла ошибка: {error_info}.")
        return []
    except ValueError as error_info:
        print(error_info)
        return []
