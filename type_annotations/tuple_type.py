from typing import Tuple

tuple_of_ints: Tuple[int, int, int] = (1, 2, 3)
print(tuple_of_ints)  # (1, 2, 3)

tuple_of_strings: Tuple[str, str, str] = ("a", "b", "c")
print(tuple_of_strings)  # ("a", "b", "c")

tuple_of_bools: Tuple[bool, bool, bool] = (True, False, True)
print(tuple_of_bools)  # (True, False, True)

tuple_of_ints_and_strings: Tuple[int, str, int, str] = (1, "a", 2, "b")
print(tuple_of_ints_and_strings)  # (1, "a", 2, "b")

tuple_of_ints_and_bools: Tuple[int, bool, int, bool] = (1, True, 2, False)
print(tuple_of_ints_and_bools)  # (1, True, 2, False)

tuple_of_strings_and_bools: Tuple[str, bool,
                                  str, bool] = ("a", True, "b", False)
print(tuple_of_strings_and_bools)  # ("a", True, "b", False)

tuple_of_ints_and_strings_and_bools: Tuple[int, str, bool, int, str, bool] = (
    1, "a", True, 2, "b", False)
print(tuple_of_ints_and_strings_and_bools)  # (1, "a", True, 2, "b", False)

tuple_of_tuples: Tuple[Tuple[int, int], Tuple[int, int]] = ((1, 2), (3, 4))
print(tuple_of_tuples)  # ((1, 2), (3, 4))


def tuple_of_ints_returner() -> Tuple[int, int, int]:
    return (1, 2, 3)


print(tuple_of_ints_returner())  # (1, 2, 3)


def tuple_of_strings_returner() -> Tuple[str, str, str]:
    return ("a", "b", "c")


print(tuple_of_strings_returner())  # ("a", "b", "c")


def tuple_of_bools_returner() -> Tuple[bool, bool, bool]:
    return (True, False, True)


print(tuple_of_bools_returner())  # (True, False, True)


def merge_tuples(tuple1: Tuple[int, int, int],
                 tuple2: Tuple[int, int, int]) -> Tuple[int, int, int, int, int, int]:
    return tuple1 + tuple2


print(merge_tuples((1, 2, 3), (4, 5, 6)))  # (1, 2, 3, 4, 5, 6)
