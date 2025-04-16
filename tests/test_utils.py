from unittest.mock import patch, Mock, mock_open
import pytest
import json
import requests
from pathlib import Path
from src.utils import read_transactions, transaction_sum


@pytest.fixture
def sample_transaction_json() -> dict:
    return {
        "id": 12345,
        "operationAmount": {"amount": "8221.37", "currency": {"code": "USD"}},
        "description": "Test Transaction",
    }


@pytest.fixture
def mock_api_response() -> Mock:
    mock_response = Mock()
    mock_response.json.return_value = {
        "Valute": {
            "USD": {"Value": 90.0},
            "EUR": {"Value": 100.0},
        }
    }
    return mock_response


def test_read_transactions_success(sample_transaction_json: dict) -> None:
    file_content = json.dumps([sample_transaction_json])
    with patch("builtins.open", mock_open(read_data=file_content)):
        result = read_transactions(Path("test_file.json"))
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] == sample_transaction_json


def test_read_transactions_file_not_found() -> None:
    with patch("builtins.open", side_effect=FileNotFoundError):
        result = read_transactions(Path("non_existent.json"))
        assert result == []


def test_read_transactions_bad_json() -> None:
    with patch("builtins.open", mock_open(read_data="<invalid json>")):
        result = read_transactions(Path("bad_format.json"))
        assert result == []


def test_read_transactions_json_not_list() -> None:
    file_content = json.dumps({"key": "value"})
    with patch("builtins.open", mock_open(read_data=file_content)):
        result = read_transactions(Path("not_a_list.json"))
        assert result == []


@pytest.mark.parametrize(
    "currency_code, amount_str, expected_sum",
    [
        ("RUB", "500.50", 500.50),
        ("USD", "10.00", 900.0),
        ("EUR", "20.00", 2000.0),
        ("XYZ", "100.00", 100.00),
    ],
)
@patch("requests.get")
def test_transaction_sum_json_format(
    mock_get: Mock,
    mock_api_response: Mock,
    currency_code: str,
    amount_str: str,
    expected_sum: float,
) -> None:
    mock_get.return_value = mock_api_response

    transaction = {
        "operationAmount": {"amount": amount_str, "currency": {"code": currency_code}},
    }
    result = transaction_sum(transaction)
    assert result == expected_sum


@pytest.mark.parametrize(
    "currency_code, amount_str, expected_sum",
    [
        ("RUB", "150.75", 150.75),
        ("USD", "10.0", 900.0),
        ("XYZ", "200.0", 200.0),
    ],
)
@patch("requests.get")
def test_transaction_sum_other_file_type(
    mock_get: Mock,
    mock_api_response: Mock,
    currency_code: str,
    amount_str: str,
    expected_sum: float,
) -> None:
    mock_get.return_value = mock_api_response

    transaction = {"currency_code": currency_code, "amount": amount_str}

    result = transaction_sum(transaction, file_type="other")
    assert result == expected_sum


@patch("requests.get")
def test_transaction_sum_api_error(
    mock_get: Mock, sample_transaction_json: dict
) -> None:
    mock_get.side_effect = requests.exceptions.Timeout("API request timed out")

    result = transaction_sum(sample_transaction_json)
    assert result == 0.0
