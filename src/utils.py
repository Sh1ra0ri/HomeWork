import json
import os
import requests
from pathlib import Path
from typing import List, Dict, Any
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")

def read_transactions(file_path: Path) -> List[Dict[str, Any]]:
    """функция, которая принимает на вход путь до JSON-файла и возвращает список словарей с данными"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Ошибка при чтении файла {file_path}: {e}")
        return []

def transaction_sum(transaction: dict, file_type: str = "json") -> float:
    """функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях,"""
    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}

    if file_type == "json":
        currency_code = transaction["operationAmount"]["currency"]["code"]
        amount = float(transaction["operationAmount"]["amount"])
    else:
        currency_code = transaction["currency_code"]
        amount = float(transaction["amount"])

    if currency_code == "RUB":
        return amount

    params = {"from": currency_code, "to": "RUB", "amount": amount}

    try:
        response = requests.get(url, headers=headers, params=params)
        response_data = response.json()

        if response.status_code == 200:
            return response_data.get('result', None)
        else:
            print(f"Ошибка запроса API: {response_data.get('error', 'Неизвестная ошибка')}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return None