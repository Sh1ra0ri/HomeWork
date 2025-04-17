import json
import os
import requests
import logging
from pathlib import Path
from dotenv import load_dotenv
from typing import List, Dict, Any

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)

if not logger.handlers:
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)

load_dotenv()
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    logger.warning("API_KEY не найден в переменных окружения.")


def read_transactions(file_path: Path) -> List[Dict[str, Any]]:
    """Читает файл и возвращает данные как список."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                logger.info("Файл прочитан.")
                return data
            logger.warning(f"Файл {file_path} не содержит корректных данных.")
            return []
    except Exception as e:
        logger.error(f"Ошибка при чтении файла {file_path}: {e}")
        return []


def transaction_sum(transaction: Dict[str, Any], file_type: str = "json") -> float:
    """Возвращает сумму транзакции в рублях."""
    try:
        response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js", timeout=5)
        data = response.json()

        if file_type == "json":
            if transaction["operationAmount"]["currency"]["code"] == "RUB":
                amount = float(transaction["operationAmount"]["amount"])
                currency = 1.0
            else:
                valute = transaction["operationAmount"]["currency"]["code"]
                currency = data["Valute"].get(valute, {}).get("Value", 1.0)
                amount = float(transaction["operationAmount"]["amount"])
        else:
            if transaction.get("currency_code") == "RUB":
                amount = float(transaction["amount"])
                currency = 1.0
            else:
                valute = transaction.get("currency_code")
                currency = data["Valute"].get(valute, {}).get("Value", 1.0)
                amount = float(transaction["amount"])

        logger.info("Функция выполнена")
        return amount * currency

    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при запросе к API: {e}")
        return 0.0
