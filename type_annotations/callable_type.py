from collections.abc import Callable


def add(x: int, y: int) -> int:
    return x + y


def subtract(x: int, y: int) -> int:
    return x - y


def multiply(x: int, y: int) -> int:
    return x * y


def divide(x: int, y: int) -> int:
    return x // y


def calculate(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)


print(calculate(10, 5, add))  # Output: 15
print(calculate(10, 5, subtract))  # Output: 5
print(calculate(10, 5, multiply))  # Output: 50
print(calculate(10, 5, divide))  # Output: 2.0


def apply_func(func: Callable[..., int], *args: int) -> int:
    return func(*args)


def sum(x: int, y: int) -> int:
    return x + y


print(apply_func(sum, 10, 20))  # Output: 30


def sum_all(w: int, x: int, y: int, z: int) -> int:
    return w + x + y + z


print(apply_func(sum_all, 10, 20, 30, 40))  # Output: 100
