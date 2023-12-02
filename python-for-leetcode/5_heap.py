import heapq

nums = [5, 7, 9, 1, 3]

heapq.heapify(nums)  # Min heap

print(heapq.heappop(nums))  # Prints 1

heapq.heappush(nums, 4)

heapq.heapreplace(nums, 2)  # Pop and push
print(nums)  # Prints [2, 4, 9, 7, 5]

# Max heap
max_heap = [-x for x in nums]
heapq.heapify(max_heap)
print(-heapq.heappop(max_heap))  # Prints 9

# Create a min heap of lists with custom comparator
nums = [[1, 2], [3, 4], [1, -1]]
heapq.heapify(nums)
print(heapq.heappop(nums))  # Prints [1, -1]
