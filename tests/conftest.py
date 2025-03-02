import pytest


@pytest.fixture
def right_card_number():
    return "1596837868705199"


@pytest.fixture
def right_account_number():
    return "64686473678894779589"


@pytest.fixture
def right_date():
    return "2024-03-11T02:26:18.671407"


@pytest.fixture
def right_data_for_processing_filter_by_state():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ]


@pytest.fixture
def right_data_for_processing_sort_by_date():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12'},
            {'id': 594226222, 'state': 'CANCELED', 'date': '2018-09-12'},
            {'id': 594226700, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            ]
