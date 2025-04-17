import pandas as pd


def read_csv_transactions(file_name: str) -> list:
    """Считывает финансовые операции из CSV-файла"""
    if not file_name.endswith(".csv"):
        return []
    try:
        data = pd.read_csv(file_name, sep=";")
        cleaned_data = data.dropna(how="any")
        return cleaned_data.to_dict(orient="records")
    except FileNotFoundError:
        return []


def read_excel_transactions(file_name: str) -> list:
    """Считывает финансовые операции из XLSX-файлов."""
    if not (file_name.endswith(".xlsx") or file_name.endswith(".xls")):
        return []
    try:
        data = pd.read_excel(file_name)
        cleaned_data = data.dropna(how="any")
        return cleaned_data.to_dict(orient="records")
    except FileNotFoundError:
        return []
