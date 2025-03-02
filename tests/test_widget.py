import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("data_for_mask, expected",
                         [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ])
def test_mask_account_card_for_card(data_for_mask, expected):
    """"Проверка правильности создания маски номера карты для корректных значений ее номера"""
    assert mask_account_card(data_for_mask) == expected


@pytest.mark.parametrize("data_for_mask, expected",
                         [("Счет 64686473678894779589", "Счет **9589"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Счет 73654108430135874305", "Счет **4305"),
                          ("Счёт 35383033474447895560", "Счёт **5560"),
                          ])
def test_mask_account_card_for_account(data_for_mask, expected):
    """"Проверка правильности создания маски номера счета для корректных значений его номера"""
    assert mask_account_card(data_for_mask) == expected


def test_mask_account_card_if_data_is_not_string():
    with pytest.raises(Exception) as error_info:
        mask_account_card(64686473678894779589)
    assert str(error_info.value) == "Неверный тип исходных данных. Ожидается тип 'str'"



def test_mask_account_card_for_wrong_lenght_account_number():
    with pytest.raises(Exception) as error_info:
        mask_account_card("Счет 3538303347444789556000000000000000000")
    assert str(error_info.value) == "Ошибка! В исходных данных номер карты или счета не обнаружен или указан неверно."


def test_mask_account_card_for_wrong_lenght_card_number():
    with pytest.raises(Exception) as error_info:
        mask_account_card("Maestro 159683786")
    assert str(error_info.value) == "Ошибка! В исходных данных номер карты или счета не обнаружен или указан неверно."


def test_mask_account_card_for_for_empty_data():
    with pytest.raises(Exception) as error_info:
        mask_account_card("")
    assert str(error_info.value) == "Ошибка! В исходных данных номер карты или счета не обнаружен или указан неверно."



def test_get_date(right_date):
    """"Проверка правильности приведения даты из формата ISO 8601 к виду "ДД.ММ.ГГГГ" для корректного значения даты"""
    assert get_date(right_date) == "11.03.2024"


@pytest.mark.parametrize("date_for_change, expected",
                         [("2024-03-11T02:26:18", "11.03.2024"),
                          ("2024-03-11", "11.03.2024"),
                          ("2025-03-12T14:29:22+03:00", "12.03.2025"),
                          ])
def test_get_date(date_for_change, expected):
    assert get_date(date_for_change) == expected


def test_get_date_for_empty_data():
    with pytest.raises(ValueError) as error_info:
        get_date("")
    assert str(error_info.value) == "Invalid isoformat string"
