from typing import Dict

dict_of_ints: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
print(dict_of_ints)  # {'a': 1, 'b': 2, 'c': 3}

dict_of_strings: Dict[str, str] = {"a": "a", "b": "b", "c": "c"}
print(dict_of_strings)  # {'a': 'a', 'b': 'b', 'c': 'c'}

dict_of_dict_of_ints: Dict[str, Dict[str, int]] = {
    "a": {"a": 1, "b": 2, "c": 3},
    "b": {"a": 4, "b": 5, "c": 6},
    "c": {"a": 7, "b": 8, "c": 9}}
# {'a': {'a': 1, 'b': 2, 'c': 3}, 'b': {'a': 4, 'b': 5, 'c': 6}, 'c': {'a': 7, 'b': 8, 'c': 9}}
print(dict_of_dict_of_ints)

dict_of_dict_of_dict_of_ints: Dict[str, Dict[str, Dict[str, int]]] = {
    "a": {
        "a": {"a": 1, "b": 2, "c": 3},
        "b": {"a": 4, "b": 5, "c": 6},
        "c": {"a": 7, "b": 8, "c": 9}},
    "b": {
        "a": {"a": 10, "b": 11, "c": 12},
        "b": {"a": 13, "b": 14, "c": 15},
        "c": {"a": 16, "b": 17, "c": 18}},
    "c": {
        "a": {"a": 19, "b": 20, "c": 21},
        "b": {"a": 22, "b": 23, "c": 24},
        "c": {"a": 25, "b": 26, "c": 27}}}
# {'a': {'a': {'a': 1, 'b': 2, 'c': 3}, 'b': {'a': 4, 'b': 5, 'c': 6}, 'c': {'a': 7, 'b': 8, 'c': 9}}, 'b': {'a': {'a': 10, 'b': 11, 'c': 12}, 'b': {'a': 13, 'b': 14, 'c': 15}, 'c': {'a': 16, 'b': 17, 'c': 18}}, 'c': {'a': {'a': 19, 'b': 20, 'c': 21}, 'b': {'a': 22, 'b': 23, 'c': 24}, 'c': {'a': 25, 'b': 26, 'c': 27}}}
print(dict_of_dict_of_dict_of_ints)


def merge_dict_of_dicts(dict_of_dicts: Dict[str, Dict[str, int]]) -> Dict[str, int]:
    merged_dict: Dict[str, int] = {}
    for dict_ in dict_of_dicts.values():
        merged_dict.update(dict_)
    return merged_dict


dict1: Dict[str, int] = {"a": 1, "b": 2, "c": 3}
dict2: Dict[str, int] = {"d": 4, "e": 5, "f": 6}
dict3: Dict[str, int] = {"g": 7, "h": 8, "i": 9}
dict_of_dicts: Dict[str, Dict[str, int]] = {
    "dict1": dict1, "dict2": dict2, "dict3": dict3}
# {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9}
print(merge_dict_of_dicts(dict_of_dicts))
