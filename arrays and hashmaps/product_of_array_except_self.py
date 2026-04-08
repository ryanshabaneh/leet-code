# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Difficulty: Medium

'''
Given an integer array nums, return an array output where output[i] is the
product of all elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.
Follow-up: solve in O(n) time without using division.

Example 1:
Input: nums = [1,2,4,6]
Output: [48,24,12,8]

Example 2:
Input: nums = [-1,0,1,2,3]
Output: [0,-6,0,0,0]

Constraints:
2 <= nums.length <= 1000
-20 <= nums[i] <= 20
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
            postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post





