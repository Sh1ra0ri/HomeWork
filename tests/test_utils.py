from unittest.mock import patch, Mock, mock_open
import pytest
import json
from pathlib import Path
from src.utils import read_transactions, transaction_sum


@pytest.fixture
def first_operation() -> dict:
    return {
        "operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}},
    }


def test_read_transactions(first_operation: dict) -> None:
    with patch("builtins.open", mock_open(read_data=json.dumps([first_operation]))):
        result = read_transactions(Path("test_file.json"))
        assert isinstance(result, list)
        assert result == [first_operation]


def test_transaction_sum() -> None:
    with patch("requests.get") as mock_get:
        mock_response = Mock()
        mock_response.json.return_value = {
            "Valute": {
                "USD": {"Value": 90},
                "EUR": {"Value": 100}
            }
        }
        mock_get.return_value = mock_response

        result = transaction_sum({
            "operationAmount": {"amount": 100, "currency": {"code": "USD"}}
        })
        assert result == 9000