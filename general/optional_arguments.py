def greet(name=None):
    if name:
        return f"Hello, {name}!"
    else:
        return "Hello, stranger!"


print(greet())  # Hello stranger
print(greet("John"))  # Hello John

# function with 1 required argument and 1 optional argument


def greet_with_message(name, message="Hello"):
    return f"{message}, {name}!"


print(greet_with_message("John"))  # Hello, John!
print(greet_with_message("John", "Howdy"))  # Howdy, John!

# function with 1 required argument and 2 optional arguments


def greet_with_message_and_time(name, message="Hello", time="morning"):
    return f"{message}, {name}! Good {time}!"


print(greet_with_message_and_time("John"))  # Hello, John! Good morning!
# Howdy, John! Good morning!
print(greet_with_message_and_time("John", "Howdy"))
# Howdy, John! Good evening!
print(greet_with_message_and_time("John", "Howdy", "evening"))
