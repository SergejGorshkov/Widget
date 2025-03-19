from decorators import log


# Тестирование декоратора 'log'
def test_log_output_to_console_without_error_1(capsys):
    """Проверка правильности вывода в консоль информации об успешном завершении работы функции,
    а также правильности возвращаемого результата.
    В проверке используются следующие фильтры: имя вызываемой функции, результат выполнения функции."""

    @log(filename="")
    def my_function_division(x, y):
        """Пример функции для тестирования декоратора 'log'."""
        return x / y

    result = my_function_division(10, 2)
    assert result == 5.0
    assert "Called function 'my_function_division' (successfully)" in capsys.readouterr().out


def test_log_output_to_console_without_error_2(capsys):
    """Проверка правильности вывода в консоль информации о завершении работы функции с ошибкой.
    В проверке используются следующие фильтры: имя вызываемой функции, результат выполнения функции, тип ошибки."""

    @log(filename="")
    def my_function_multiplication(x, y):
        """Пример функции для тестирования декоратора 'log'."""
        return x * y

    result = my_function_multiplication("10", 2)
    assert result == "1010"
    assert "Called function 'my_function_multiplication' (successfully)" in capsys.readouterr().out


def test_log_output_to_console_with_error(capsys):
    """Проверка правильности вывода в консоль информации о завершении работы функции с ошибкой,
    а также правильности возвращаемого результата.
    В проверке используются следующие фильтры: имя вызываемой функции, результат выполнения функции, тип ошибки."""

    @log(filename="")
    def my_function_division(x, y):
        """Пример функции для тестирования декоратора 'log'."""
        return x / y

    result = my_function_division(1, 0)
    assert not result
    assert (
        "Called function 'my_function_division' (unsuccessfully)"
        and "Error: division by zero" in capsys.readouterr().out
    )
