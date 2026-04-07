# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
#
#Given an integer array nums, return true if any value appears more than once in the array, 
#otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for num in nums:
            if num in set:
                return True
            hashset.add(n)
        return False

        # return len(set(nums)) < len(nums) #I got it right!! # shortcut

'''
Time: O(n) — single pass through the array
Space: O(n) — hashset stores up to n elements

Key pattern: when you need to check "have I seen this before?", reach for a set.
Sets give O(1) lookup vs O(n) for scanning a list.
Any "contains duplicate" or "find repeated element" problem likely uses this pattern.

Extra notes:
If nums is a list: nums = [1, 2, 2, 3, 3, 3]
Then: set(nums) -> {1, 2, 3}
if 3 in nums:      # O(n)
if 3 in set(nums): # O(1)
Sets use hashing (like dicts), so lookup is fast
'''