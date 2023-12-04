from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Binary Search Algorithm

    Input: <nums> is a sorted list of integers, <target> is an integer
    Output: the index of <target> in <nums>, or -1 if <target> is not in <nums>

    Logic:
    1. Initialize left and right pointer to the start and end of the list
    2. While left <= right:
        a. Calculate mid index
        b. If nums[mid] == target, return mid
        c. If nums[mid] < target, move left pointer to mid + 1
        d. If nums[mid] > target, move right pointer to mid - 1
    """
    if not nums:
        return -1
    left: int = 0
    right: int = len(nums) - 1
    while left <= right:
        mid: int = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left: int = mid + 1
        else:
            right: int = mid - 1

    return -1


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 4, 5]
    target: int = 3
    print(binary_search(nums, target))
    target: int = 6
    print(binary_search(nums, target))
