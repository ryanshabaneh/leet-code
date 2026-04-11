# 167. Two Sum II - Input Array Is Sorted
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to target.
# Return their 1-indexed positions as [index1, index2].
# Must use only constant extra space.
#
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
#
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
#
# Constraints:
# - 2 <= numbers.length <= 3 * 10^4
# - numbers is sorted in non-decreasing order
# - exactly one solution exists
# - may not use the same element twice
# - O(1) extra space

from typing import List


def two_sum_ii(nums: List[int], target: int) -> List[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum > target:
            r -= 1      # sum too big — move r left to get a smaller value
        elif sum < target:
            l += 1      # sum too small — move l right to get a bigger value
        else:
            return [l+1, r+1]   # +1 because problem uses 1-indexed positions
    return []

"""
Approach: Two Pointers

Key insight: because the array is sorted, we know exactly which direction
to move when the sum is wrong. Too big → shrink from the right. Too small
→ grow from the left. This eliminates the need for a hashmap entirely.

Why not use a hashmap like original Two Sum?
    The constraint says O(1) space — no hashmap allowed.
    But we don't need one: the sorted order gives us directional information
    that lets us home in on the answer without storing anything.

Why does this work in O(n)?
    Each step either moves l right or r left — they can only move toward
    each other, so the total number of steps is at most n.

Time:  O(n)
Space: O(1)
"""
