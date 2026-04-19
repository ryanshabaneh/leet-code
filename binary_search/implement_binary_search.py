# Implement Binary Search
# Classic / Drill
#
# Given a sorted array of integers nums and a target integer target,
# return the index of target if it exists, or -1 if it does not.
#
# Do not use any built-in search functions.
#
# Example 1:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 9
# Output: 4
#
# Example 2:
# Input: nums = [-1, 0, 3, 5, 9, 12], target = 2
# Output: -1
#
# Goal: implement this from memory until it's automatic.

def binary_search(nums: list[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l<=r:
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1 
    return -1

