class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width: float = width
        self.height: float = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)


# Usage example
my_rectangle: Rectangle = Rectangle(4.5, 5.2)
print(my_rectangle.area())  # This will print 23.4
print(my_rectangle.perimeter())  # This will print 19.4


def get_area(rectangle: Rectangle) -> float:
    return rectangle.area()


print(get_area(my_rectangle))  # This will print 23.4
