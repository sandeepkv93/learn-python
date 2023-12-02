dict = {"a": 1, "b": 2, "c": 3}

# 1. Get keys
keys = dict.keys()
print(keys)  # Prints dict_keys(['a', 'b', 'c'])

# 2. Get values
values = dict.values()
print(values)  # Prints dict_values([1, 2, 3])

# 3. Print key-value pairs
for key, value in dict.items():
    print(key, value)  # Prints a 1, b 2, c 3

# 4. Check if a key exists. Time complexity: O(1)
if "a" in dict:
    print("Key a exists")

# 5. Check if a value exists. Time complexity: O(n)
if 1 in dict.values():
    print("Value 1 exists")

# 6. Get a value with a default value
value = dict.get("d", 4)
print(value)  # Prints 4

# 7. Set a value if key does not exist
dict.setdefault("d", 4)

# 8. Set a value if key does not exist
dict["d"] = 4

# 9. Remove a key-value pair
dict.pop("a")

# 10. Remove a key-value pair
del dict["b"]

# 11. Remove all key-value pairs
dict.clear()

# 12. Merge two dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict1.update(dict2)

# 13. Create a dictionary with default value
from collections import defaultdict

dict = defaultdict(int)
print(dict["a"])  # Prints 0

# 14. Create a dictionary with default value
dict = {}
dict.setdefault("a", 0)
print(dict["a"])  # Prints 0

# 15. Iterate over a dictionary
dict = {"a": 1, "b": 2, "c": 3}
for key, value in dict.items():
    print(key, value)  # Prints a 1, b 2, c 3

# 16. Iterate over a dictionary keys
dict = {"a": 1, "b": 2, "c": 3}
for key in dict.keys():
    print(key)  # Prints a, b, c

# 17. Iterate over a dictionary values
dict = {"a": 1, "b": 2, "c": 3}
for value in dict.values():
    print(value)  # Prints 1, 2, 3

# 18. Iterate over a dictionary in sorted order by keys
dict = {"a": 1, "b": 2, "c": 3}
for key in sorted(dict.keys()):
    print(key)  # Prints a, b, c

# 19. Iterate over a dictionary in sorted order by values
dict = {"a": 1, "b": 2, "c": 3}
for key in sorted(dict.keys(), key=lambda x: dict[x]):
    print(key)  # Prints a, b, c
