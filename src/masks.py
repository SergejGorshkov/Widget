"""
Модуль 'masks' предназначен для получения от модуля `widget.py` номера банковской карты (16 цифр)
(например: 3232323245456565) и номера счета (20 цифр) (например: 90903209302935646897) и
формирования их масок в формате '3232 32** **** 6565' и '**6897' соответственно.
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log", "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(filename)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number: str) -> str:
    """Функция маскировки номера банковской карты"""
    logger.debug("Создана маска банковской карты.")
    return f"{number[0:4]} {number[4:6]}** **** {number[-4:]}"


def get_mask_account(number: str) -> str:
    """Функция маскировки номера банковского счета"""
    logger.debug("Создана маска банковского счета.")
    return f"**{number[-4:]}"
