def filter_by_currency(transactions, currency):
    """функция которая принимает на вход список словарей, представляющих транзакции."""
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction

def transaction_descriptions(transactions):
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for transaction in transactions:
        yield transaction.get('description')

def card_number_generator(first_number, last_number):
    """генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX"""
    for i in range(first_number, last_number + 1):
        card_number = f"{i:0>16}"
        yield card_number[:4] + " " + card_number[4:8] + " " + card_number[8:12] + " " + card_number[12:]
