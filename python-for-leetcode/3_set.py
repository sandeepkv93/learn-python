set = {1, 2, 3}

# 1. Check if an element exists in a set
if 1 in set:
    print("Element exists")

# 2. Add an element to a set
set.add(4)

# 3. Remove an element from a set
set.remove(4)

# 4. Remove an element from a set
set.discard(4)

# 5. Remove an arbitrary element from a set
set.pop()

# 6. Remove all elements from a set
set.clear()

# 7. Merge two sets
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set1.update(set2)

# 8. Create a set with default value
from collections import defaultdict

set = defaultdict(int)
print(set[1])  # Prints 0

# 9. Create a set with default value
set = {}
set.setdefault(1, 0)
print(set[1])  # Prints 0

# 10. Iterate over a set
set = {1, 2, 3}
for element in set:
    print(element)

# 11. Iterate over a set
set = {1, 2, 3}
for index, element in enumerate(set):
    print(index, element)

# Set operations
# 13. Union
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = set1.union(set2)
print(set3)  # Prints {1, 2, 3, 4, 5, 6}

# 14. Intersection
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.intersection(set2)
print(set3)  # Prints {2, 3}

# 15. Difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference(set2)
print(set3)  # Prints {1}

# 16. Symmetric difference
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.symmetric_difference(set2)
print(set3)  # Prints {1, 4}

# 17. Subset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Prints True

# 18. Superset
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4}
print(set2.issuperset(set1))  # Prints True

# 19. Disjoint
set1 = {1, 2, 3}
set2 = {4, 5, 6}
print(set1.isdisjoint(set2))  # Prints True
