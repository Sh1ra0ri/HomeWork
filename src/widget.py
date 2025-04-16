from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(new_line: str) -> str:
    """Функция, которая обрабатывает информацию о счетах и картах."""
    card_elements: list[str] = new_line.split()
    card_account_number: int = int(card_elements[-1])
    first_element = card_elements[0]

    if first_element == "Счет":
        return f"{first_element} **{get_mask_account(card_account_number)}"

    return " ".join(card_elements[0:-1] + [get_mask_card_number(card_account_number)])


def get_date(user_date_and_time: str) -> str:
    """Функция, которая принимает дату в формате ISO и возвращает в формате ДД.ММ.ГГГГ."""
    year, month, day = user_date_and_time.split("T")[0].split("-")
    return ".".join([day, month, year])
