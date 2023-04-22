from typing import List

list_of_ints: List[int] = [1, 2, 3]
print(list_of_ints)  # [1, 2, 3]

list_of_strings: List[str] = ["a", "b", "c"]
print(list_of_strings)  # ["a", "b", "c"]

list_of_list_of_ints: List[List[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_of_list_of_ints)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

list_of_list_of_strings: List[List[str]] = [
    ["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
# [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]]
print(list_of_list_of_strings)

list_of_list_of_list_of_ints: List[List[List[int]]] = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
    [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
# [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
print(list_of_list_of_list_of_ints)


def merge_list_of_lists(list_of_lists: List[List[int]]) -> List[int]:
    merged_list: List[int] = []
    for list_ in list_of_lists:
        merged_list += list_
    return merged_list


list1: List[int] = [1, 2, 3]
list2: List[int] = [4, 5, 6]
list3: List[int] = [7, 8, 9]
list_of_lists: List[List[int]] = [list1, list2, list3]
merged_list: List[int] = merge_list_of_lists(list_of_lists)
print(merged_list)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
