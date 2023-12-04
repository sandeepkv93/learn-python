from typing import List


def binary_search_range(nums: List[int], target: int) -> List[int]:
    left_most_index: int = binary_search_biased(nums, target, True)
    right_most_index: int = binary_search_biased(nums, target, False)
    return [left_most_index, right_most_index]


def binary_search_biased(nums: List[int], target: int, left_biased: bool) -> int:
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
