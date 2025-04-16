from src.logger import log_setup

logger = log_setup()


def get_mask_card_number(card_number: int) -> str:
    """Маскирует номер банковской карты по правилу XXXX XX** **** XXXX."""
    card_number_str = str(card_number)
    masked_card = (
        f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"
    )
    logger.info("Номер карты замаскирован")
    return masked_card


def get_mask_account(account_number: int) -> str:
    """Маскирует номер банковского счета по правилу XXXX."""
    account_number_str = str(account_number)
    masked_account = account_number_str[-4:]
    logger.info("Счет замаскирован")
    return masked_account
