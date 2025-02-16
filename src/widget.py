def mask_account_card(data_for_mask: str) -> str:
    """Функция маскировки номера карты или счета"""

    pass



def get_date(date_for_change: str) -> str:
    """Функция приведения даты к виду 'ДД.ММ.ГГГГ'"""
    from datetime import datetime
    date_datetime = datetime.fromisoformat(date_for_change)
    formatted_date = date_datetime.strftime("%d.%m.%Y")

    return formatted_date

# print(get_date("2024-03-11T02:26:18.671407"))
