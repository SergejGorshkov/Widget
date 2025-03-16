import os
from datetime import datetime
from functools import wraps
from typing import Any, Callable


def log(filename: str = "") -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор, который автоматически регистрирует следующие детали выполнения декорируемых функций:
    имя функции, время вызова, результат выполнения, а в случае возникновения ошибок при ее работе - дополнительно
    передаваемые аргументы и информацию об ошибках.
    Декоратор имеет необязательный входной параметр 'filename' - имя файла, в который вносится информация
    о работе функции. Если при вызове декоратора параметр 'filename' не указан, логирование выводится в консоль.
    Файл с логами по умолчанию находится в папке 'logs'."""

    def decorator(function: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Фиксация времени запуска функции
            try:
                result: Any = function(*args, **kwargs)
                logging_info = f"{start_time}. Called function '{function.__name__}' (successfully)."
            except Exception as error_info:
                logging_info = (
                    f"{start_time}. Called function '{function.__name__}' (unsuccessfully). "
                    f"Inputs: {args}, {kwargs}. Error: {error_info}."
                )
            if filename:
                path_to_logfile = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs", filename)
                with open(path_to_logfile, "a", encoding="UTF-8") as file:
                    file.write(f"{logging_info}\n")
            else:
                print(logging_info)

        return wrapper

    return decorator


# Код для тестирования декоратора
@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(1, 0)
