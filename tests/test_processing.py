import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "data_of_bank_operations, key_state, expected",
    [
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
                {},
                {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
            ],
            "EXECUTED",
            [{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}],
        ),
        (
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "PENDING", "date": "2018-10-14T08:21:33.419441"},
                {},
                {"id": 615064591, "state": "", "date": "2018-10-14T08:21:33.419441"},
            ],
            "canceled",
            [{"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"}],
        ),
    ],
)
def test_filter_by_state(data_of_bank_operations, key_state, expected):
    """ "Проверка правильности фильтрации списка словарей по заданным ключам"""
    assert filter_by_state(data_of_bank_operations, key_state) == expected


def test_filter_by_state_without_key(right_data_for_processing_filter_by_state):
    """ "Проверка правильности фильтрации списка словарей, если ключ не задан"""
    assert filter_by_state(right_data_for_processing_filter_by_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_with_missing_key(right_data_for_processing_filter_by_state):
    """ "Проверка правильности фильтрации списка словарей по заданному ключу при его отсутствии в списке словарей"""
    assert filter_by_state(right_data_for_processing_filter_by_state, key_state="PENDING") == []


def test_filter_by_state_with_empty_data():
    """ "Проверка правильности фильтрации списка словарей при его отсутствии"""
    assert filter_by_state([], key_state="CANCELED") == []


def test_filter_by_state_with_key_in_lowercase(right_data_for_processing_filter_by_state):
    """ "Проверка правильности фильтрации списка словарей по заданному ключу при его написании в нижнем регистре"""
    assert filter_by_state(right_data_for_processing_filter_by_state, key_state="executed") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_filter_by_state_if_data_is_not_list_of_dictionary():
    with pytest.raises(Exception) as error_info:
        filter_by_state([12, "12", 0])
    assert str(error_info.value) == "Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'"


def test_sort_by_date_if_data_is_not_list_of_dictionary():
    with pytest.raises(Exception) as error_info:
        sort_by_date([12, "12", 0])
    assert str(error_info.value) == "Неверный тип исходных данных банковских операций. Ожидается тип 'list[dict]'"


def test_sort_by_date_if_key_is_not_true_or_false(right_data_for_processing_sort_by_date):
    with pytest.raises(ValueError) as error_info:
        sort_by_date(right_data_for_processing_sort_by_date, sort_key="some string")
    assert str(error_info.value) == "Неверное значение для ключа 'sort_key'. Ожидается значение 'True' или 'False'."


def test_sort_by_date_with_key_in_lowercase(right_data_for_processing_sort_by_date):
    """ "Проверка правильности фильтрации списка словарей по заданному ключу при его написании в нижнем регистре,
    сортировка - по убыванию"""
    assert sort_by_date(right_data_for_processing_sort_by_date, sort_key="true") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226700, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 594226222, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_sort_by_date_with_key_in_uppercase(right_data_for_processing_sort_by_date):
    """ "Проверка правильности фильтрации списка словарей по заданному ключу при его написании в верхнем регистре,
    сортировка - по возрастанию"""
    assert sort_by_date(right_data_for_processing_sort_by_date, sort_key="FALSE") == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 594226222, "state": "CANCELED", "date": "2018-09-12"},
        {"id": 594226700, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]
