from typing import List


def binary_search_range(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    left_most_index: int = binary_search_biased(nums, target, True)
    right_most_index: int = binary_search_biased(nums, target, False)
    return [left_most_index, right_most_index]


def binary_search_biased(nums: List[int], target: int, left_biased: bool) -> int:
    """
    Binary Search Biased Algorithm

    Input: <nums> is a sorted list of integers, <target> is an integer, <left_biased> is a boolean
    Output: the leftmost or rightmost index of <target> in <nums>, or -1 if <target> is not found

    Logic:
    1. Initialize left and right pointer to the start and end of the list
    2. While left <= right:
        a. Calculate mid index
        b. If target < nums[mid], move right pointer to mid - 1 because target is in the left half
        c. If target > nums[mid], move left pointer to mid + 1 because target is in the right half
        d. If target == nums[mid], set i to mid
            i. If left_biased is True, move right pointer to mid - 1 because we want to find the leftmost index; therefore, we want to keep moving left
            ii. If left_biased is False, move left pointer to mid + 1 because we want to find the rightmost index; therefore, we want to keep moving right
    """
    left: int = 0
    right: int = len(nums) - 1
    i: int = -1
    while left <= right:
        mid: int = (left + right) // 2
        if target < nums[mid]:
            # Means target is in the left half
            right = mid - 1
        elif target > nums[mid]:
            # Means target is in the right half
            left = mid + 1
        else:
            # Means target is found
            i = mid
            if left_biased:
                # Means we want to find the leftmost index
                right = mid - 1
            else:
                # Means we want to find the rightmost index
                left = mid + 1
    return i


if __name__ == "__main__":
    nums: List[int] = [1, 2, 3, 3, 3, 4, 5]
    target: int = 3
    print(binary_search_range(nums, target))
    target: int = 6
    print(binary_search_range(nums, target))
