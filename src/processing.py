def filter_by_state(list_dict: list, state_stat: str = "executed") -> list:
    '''принимает список и возвращает список у которых ключ state соответствует указанному значению'''
    sorted_list = []
    for dict_ in list_dict:
        if "state" in dict_ and dict_["state"] == state_stat.upper():
            sorted_list.append(dict_)
    return sorted_list

def sort_by_date(list_dict: list) -> list:
    """принимает список и возвращает список отсортированный по дате"""
    sorted_list = []
    sorted_list = sorted(list_dict, key=lambda value: value["date"], reverse=True)
    return sorted_list