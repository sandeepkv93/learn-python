from typing import Any


def get_user_input(prompt: str) -> Any:
    user_input = input(prompt)
    try:
        return int(user_input)
    except ValueError:
        try:
            return float(user_input)
        except ValueError:
            return user_input


result1 = get_user_input("Enter a number or a string: ")
result2 = get_user_input("Enter another number or a string: ")

print(f"Result 1: {result1}, type: {type(result1)}")
print(f"Result 2: {result2}, type: {type(result2)}")


def concatenate(x: Any, y: Any) -> Any:
    return x + y


result1 = concatenate(10, 20)
result2 = concatenate("Hello, ", "world!")

# Output: "Result 1: 30, type: <class 'int'>"
print(f"Result 1: {result1}, type: {type(result1)}")
# Output: "Result 2: Hello, world!, type: <class 'str'>"
print(f"Result 2: {result2}, type: {type(result2)}")
