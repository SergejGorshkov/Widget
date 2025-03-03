from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(right_card_number):
    """ "Проверка правильности создания маски номера карты для корректного значения ее номера"""
    assert get_mask_card_number(right_card_number) == "1596 83** **** 5199"


def test_get_mask_account(right_account_number):
    """ "Проверка правильности создания маски номера счета для корректного значения его номера"""
    assert get_mask_account(right_account_number) == "**9589"
