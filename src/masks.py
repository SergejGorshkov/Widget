"""
Модуль 'masks' предназначен для получения от модуля `widget.py` номера банковской карты (16 цифр)
(например: 3232323245456565) и номера счета (20 цифр) (например: 90903209302935646897) и
формирования их масок в формате '3232 32** **** 6565' и '**6897' соответственно.
"""

def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера банковской карты"""
    mask_card_number = number[0:4] + " " + number[4:6] + "**" + " " + "****" + " " + number[-4:]
    return mask_card_number


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    mask_account_number = "**" + number[-4:]
    return mask_account_number
