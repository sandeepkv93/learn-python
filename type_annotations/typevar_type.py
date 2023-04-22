from typing import TypeVar, List, Tuple

T = TypeVar("T")


def identity(x: T) -> T:
    return x


result1 = identity(10)
result2 = identity("Hello, world!")

# Output: "Result 1: 10, type: <class 'int'>"
print(f"Result 1: {result1}, type: {type(result1)}")
# Output: "Result 2: Hello, world!, type: <class 'str'>"
print(f"Result 2: {result2}, type: {type(result2)}")


def get_item(list1: List[T], index: int) -> T:
    return list1[index]


print(get_item([1, 2, 3], 0))  # 1
print(get_item(["a", "b", "c"], 1))  # b

U = TypeVar("U")


def combine_lists(list1: List[T], list2: List[U]) -> List[Tuple[T, U]]:
    combined = []
    for i in range(min(len(list1), len(list2))):
        combined.append((list1[i], list2[i]))
    return combined


# Usage example
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(combine_lists(list1, list2))  # [(1, 'a'), (2, 'b'), (3, 'c')]
