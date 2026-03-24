# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Difficulty: Easy
#
#Given an integer array nums, return true if any value appears more than once in the array, 
#otherwise return false.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums) #I got it right!!



'''
extra notes
If nums is a list: nums = [1, 2, 2, 3, 3, 3]
Then: set(nums) -> {1, 2, 3}
if 3 in nums:      # O(n)
if 3 in set(nums): # O(1)
Sets use hashing (like dicts), so lookup is fast
'''