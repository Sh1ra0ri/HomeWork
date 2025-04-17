from typing import List, Dict


def filter_by_state(list_dict: List[Dict], state_stat: str = "executed") -> List[Dict]:
    """Принимает список словарей и возвращает те, у которых ключ 'state'
    соответствует указанному значению.
    """
    sorted_list = []
    for dict_ in list_dict:
        if "state" in dict_ and dict_["state"] == state_stat.upper():
            sorted_list.append(dict_)
    return sorted_list


def sort_by_date(list_dict: List[Dict]) -> List[Dict]:
    """Принимает список словарей и возвращает список, отсортированный по дате."""
    return sorted(list_dict, key=lambda value: value["date"])
