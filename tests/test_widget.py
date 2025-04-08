import pytest

from src.widget import mask_account_card, get_date

@pytest.fixture
def dates() -> str:
    return "2018-09-12T21:27:25.241689"

@pytest.mark.parametrize(
    "data, result",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305")
    ],
)
def test_mask_account_card(data: str, result: str) -> None:
    assert mask_account_card(data) == result

@pytest.mark.parametrize(
    "dates, expected_result",
    [
        ("2018-09-12T21:27:25.241689", "12.09.2018"),
    ]
)
def test_get_date(dates: str, expected_result: str) -> None:
    assert get_date(dates) == expected_result
