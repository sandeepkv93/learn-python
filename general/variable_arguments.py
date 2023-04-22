def print_items(*args):
    print("Printing items:")
    for item in args:
        print(item)


# Variable arguments example
# This will print "Printing items:" followed by each item on a separate line.
print_items(1, 2, 3, "four", True)


def print_person_info(name, age, *interests, **kwargs):
    print(f"{name} is {age} years old and is interested in:")
    for interest in interests:
        print(f"- {interest}")

    if 'city' in kwargs:
        print(f"Lives in {kwargs['city']}")

    if 'occupation' in kwargs:
        print(f"Occupation is {kwargs['occupation']}")


# Variable arguments with positional and keyword arguments example
print_person_info("Alice", 25, "Reading", "Hiking",
                  city="New York", occupation="Software Engineer")


def apply_operation(func, *args):
    result = func(*args)
    return result


# Variable arguments with lambda function example
# This will set result1 to 5
result1 = apply_operation(lambda x, y: x + y, 2, 3)
print(result1)
# This will set result2 to 20
result2 = apply_operation(lambda x, y: x * y, 4, 5)
print(result2)
