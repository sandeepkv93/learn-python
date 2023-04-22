from typing import Sequence, List, Tuple

sequence_of_ints: Sequence[int] = [1, 2, 3]
print(sequence_of_ints)  # [1, 2, 3]

sequence_of_strings: Sequence[str] = ["a", "b", "c"]
print(sequence_of_strings)  # ["a", "b", "c"]

sequence_of_bools: Sequence[bool] = [True, False, True]
print(sequence_of_bools)  # [True, False, True]


def add_numbers(numbers: Sequence[int]) -> int:
    return sum(numbers)


list1: List[int] = [1, 2, 3]
print(add_numbers(list1))  # 6

tuple1: Tuple[int, int, int] = (1, 2, 3)
print(add_numbers(tuple1))  # 6

range1: range = range(1, 4)
print(add_numbers(range1))  # 6
