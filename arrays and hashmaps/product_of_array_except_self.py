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
        # start with all 1s — acts as a neutral base so we can multiply into it
        # in two separate passes without needing extra pref/suff arrays
        res = [1] * (len(nums))

        # PASS 1: fill res[i] with the product of everything to the LEFT of i
        # prefix starts at 1 because there's nothing to the left of index 0
        # (multiplying by 1 = no contribution, which is correct)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix       # store product of everything before i
            prefix *= nums[i]     # now include nums[i] for the NEXT index

        # PASS 2: multiply res[i] by the product of everything to the RIGHT of i
        # postfix starts at 1 because there's nothing to the right of the last index
        # we walk backwards so postfix accumulates from the right
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix     # res[i] already has left product, now multiply right product
            postfix *= nums[i]    # include nums[i] for the NEXT index (going left)

        # after both passes: res[i] = (product of left) * (product of right) = product except self
        return res

"""
Approach: Two-Pass Prefix & Postfix (Optimal)

Key insight: output[i] = product of everything to the left of i * product of everything to the right of i
Instead of using two separate arrays, we reuse res:
    - Pass 1 loads the left products into res
    - Pass 2 multiplies in the right products on top

Why start prefix/postfix at 1?
    Index 0 has nothing to its left  → left product = 1 (identity for multiplication)
    Last index has nothing to its right → right product = 1

Why set res[i] BEFORE updating prefix/postfix?
    We want the product of everything BEFORE i, not including i itself.
    If we updated first, nums[i] would be included — which is exactly what we're trying to exclude.

Time:  O(n) — two separate passes, each O(n)
Space: O(1) extra — only two variables (prefix, postfix), output array doesn't count

Backwards for loop — range(len(nums) - 1, -1, -1):
    range(start, stop, step)
    start = len(nums) - 1  → last valid index (if len=4, indices are 0-3, so start at 3)
    stop  = -1             → stop is exclusive, so -1 means we go all the way down to index 0
    step  = -1             → walk backwards

    Common mistake: using range(len(nums), -1, -1) — that starts at len(nums) which is
    out of bounds. Always len(nums) - 1 when you want to start at the last element.
"""







