import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def mask_card() -> str:
    return "6533983459435493"

def test_get_mask_card_number(mask_card) -> None:  # Исправлено имя аргумента
    assert get_mask_card_number(mask_card) == "6533 98** **** 5493"
    assert get_mask_card_number("56356") == "Неккоректный ввод номера карты"

def test_get_mask_account(mask_card) -> None:  # Добавлено использование фикстуры
    assert get_mask_account(mask_card) == "**5493"
    assert get_mask_account("34296759") == "Неккоректный ввод номера карты"
