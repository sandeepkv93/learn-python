from typing import Generic, TypeVar, List

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self):
        self.items = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


# Usage example
my_stack1 = Stack[int]()
my_stack1.push(1)
my_stack1.push(2)
my_stack1.push(3)
print(my_stack1.pop())  # 3
print(my_stack1.size())  # 2

my_stack2 = Stack[str]()
my_stack2.push("hello")
my_stack2.push("world")
my_stack2.push("!")

print(my_stack2.pop())  # !
print(my_stack2.size())  # 2
