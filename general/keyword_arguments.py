def print_info(name, age, city):
    print(f"{name} is {age} years old and lives in {city}.")


# Positional arguments example
# This will print "Alice is 25 years old and lives in New York."
print_info("Alice", 25, "New York")

# Keyword arguments example
# This will print "Bob is 30 years old and lives in London."
print_info(name="Bob", age=30, city="London")

# This will print "Charlie is 50 years old and lives in Paris."
print_info(city="Paris", name="Charlie", age=50)

# This will print "Diana is 40 years old and lives in Berlin."
print_info("Diana", city="Berlin", age=40)
