# Find Minimum in Rotated Sorted Array
# Medium
#
# You are given an array of length n which was originally sorted in ascending order.
# It has now been rotated between 1 and n times. For example, the array
# nums = [1,2,3,4,5,6] might become:
#   [3,4,5,6,1,2] if it was rotated 4 times.
#   [1,2,3,4,5,6] if it was rotated 6 times.
#
# Assuming all elements in the rotated sorted array nums are unique,
# return the minimum element of this array.
#
# A solution that runs in O(n) is trivial — write one that runs in O(log n).
#
# Example 1:
# Input: nums = [3,4,5,6,1,2]
# Output: 1
#
# Example 2:
# Input: nums = [4,5,0,1,2,3]
# Output: 0
#
# Example 3:
# Input: nums = [4,5,6,7]
# Output: 4
#
# Constraints:
# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

class Solution:
    def findMin(self, nums: list[int]) -> int:
        while l < r:
            pass

