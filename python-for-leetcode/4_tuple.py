tuple1 = (1, 2, 3, 1)

# 1. Get the length of a tuple
print(len(tuple1))  # Prints 4

# 2. Get the index of an element
print(tuple1.index(1))  # Prints 0

# 3. Count the number of occurrences of an element
print(tuple1.count(1))  # Prints 2

# 4. Iterate over a tuple
for element in tuple1:
    print(element)

st = "car"
count = [0] * 26
for c in st:
    count[ord(c) - ord("a")] += 1

# Convert count to tuple
tuple2 = tuple(count)
print(tuple2)
