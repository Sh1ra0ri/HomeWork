def filter_by_currency(transactions, currency):
    """Функция, фильтрующая транзакции по указанной валюте.

    Принимает список словарей с транзакциями и возвращает генератор
    только тех, у которых валюта соответствует заданной.
    """
    for transaction in transactions:
        operation_amount = transaction.get('operationAmount', {})
        currency_info = operation_amount.get('currency', {})
        code = currency_info.get('code', None)

        if code == currency:
            yield transaction


def transaction_descriptions(transactions):
    """Генератор описаний транзакций.

    Принимает список словарей с транзакциями и возвращает описание
    каждой операции по очереди.
    """
    for transaction in transactions:
        yield transaction.get('description')


def card_number_generator(first_number, last_number):
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Выдает номера карт от first_number до last_number включительно.
    """
    for i in range(first_number, last_number + 1):
        card_number = f"{i:016}"
        yield (f"{card_number[:4]} {card_number[4:8]} "
               f"{card_number[8:12]} {card_number[12:]}")
