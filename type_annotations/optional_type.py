from datetime import datetime
from typing import Optional


def greet(name: Optional[str]) -> str:
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, stranger!"


print(greet(None))  # Hello stranger
print(greet("John"))  # Hello John


def get_age(birth_year: Optional[int]) -> Optional[int]:
    current_year = datetime.now().year
    if birth_year:
        return current_year - birth_year
    else:
        return None


print(get_age(1990))  # 31
print(get_age(None))  # None


class Person:
    def __init__(self, name: str, age: Optional[int] = None):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        if self.age:
            return f"{self.name} is {self.age} years old."
        else:
            return f"{self.name} is of an unknown age."


person1 = Person("Alice", 25)
person2 = Person("Bob")

print(person1.get_info())  # Output: "Alice is 25 years old."
print(person2.get_info())  # Output: "Bob is of an unknown age."


def divide(x: int, y: int) -> Optional[float]:
    if y == 0:
        return None
    else:
        return x / y


result1 = divide(10, 5)
result2 = divide(10, 0)

if result1 is not None:
    print(f"10 / 5 = {result1}")  # Output: "10 / 5 = 2.0"
else:
    print("Division by zero is not allowed.")

if result2 is not None:
    print(f"10 / 0 = {result2}")
else:
    # Output: "Division by zero is not allowed."
    print("Division by zero is not allowed.")
