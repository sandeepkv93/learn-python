nums = [1, 2, 3]

# 1. Return index of target
target = 2
print(nums.index(target))  # Prints 1

# 2. Append to list
nums.append(4)
print(nums)  # Prints [1, 2, 3, 4]

# 3. Insert a value at a specific index
nums.insert(2, 5)
print(nums)  # Prints [1, 2, 5, 3, 4]

# 4. Remove a value
nums.remove(3)  # Removes all occurrences of 3
print(nums)  # Prints [1, 2, 5, 4]

# 5. Pop a value
nums.pop()  # Removes last element in list
print(nums)  # Prints [1, 2, 5]

# 6. Find the frequency of a value in a list
print(nums.count(2))  # Prints 1

# 7. Reverse a list
nums.reverse()  # Reverses the list in place
print(nums)  # Prints [5, 2, 1]

# 8. Sort a list in place
nums.sort()  # Sorts the list in place
print(nums)  # Prints [1, 2, 5]

# 9. Sort a list and return a new list
nums = [1, 2, 3]
sorted_nums = sorted(nums)  # Returns a new list
print(nums)  # Prints [1, 2, 3]
print(sorted_nums)  # Prints [1, 2, 3]

# 10. Create a list of size n with default value
n = 5
nums = [0] * n
print(nums)  # Prints [0, 0, 0, 0, 0]

# 11. Create a list of size n with default value
n = 5
nums = [0 for _ in range(n)]

# 12. Merge two lists
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums1.extend(nums2)

# 13. Shallow copy a list
nums1 = [1, 2, 3]
nums2 = nums1.copy()
nums2[0] = 0
print(nums1)  # Prints [1, 2, 3]

# 14. Deep copy a list
import copy

nums1 = [[1, 2], [3, 4]]
nums2 = copy.deepcopy(nums1)
nums2[0][0] = 0
print(nums1)  # Prints [[1, 2], [3, 4]]

# 15. Iterate over a list
nums = [1, 2, 3]
for num in nums:
    print(num)

# 16. Iterate over a list with index
nums = [1, 2, 3]
for i, num in enumerate(nums):
    print(i, num)

# 17. Iterate over a list in reverse
nums = [1, 2, 3]
for num in reversed(nums):
    print(num)

# 18. Iterate over two lists
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for num1, num2 in zip(nums1, nums2):
    print(num1, num2)

# 19. Iterate over two lists with index
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for i, (num1, num2) in enumerate(zip(nums1, nums2)):
    print(i, num1, num2)

# 20. Check if a list is empty
nums = []
if not nums:
    print("List is empty")

# 21. Clear a list
nums = [1, 2, 3]
nums.clear()

# 22. Delete a list
nums = [1, 2, 3]
del nums

# 23. Convert list to string
nums = [1, 2, 3]
nums_str = "".join(str(num) for num in nums)
print(nums_str)  # Prints 123

# 24. Convert string to list
nums_str = "123"
nums = list(nums_str)

# 25. Convert list to set
nums = [1, 2, 3]
nums_set = set(nums)

# 26. Convert list to dictionary
nums = [1, 2, 3]
nums_dict = dict.fromkeys(nums, 0)

# 27. Convert list to tuple
nums = [1, 2, 3]
nums_tuple = tuple(nums)

# 28. Convert list to array
import array

nums = [1, 2, 3]
nums_array = array.array("i", nums)
