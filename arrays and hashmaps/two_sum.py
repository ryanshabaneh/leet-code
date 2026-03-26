# 1. Two Sum
# https://leetcode.com/problems/two-sum/
# Difficulty: Easy

'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input: 

nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Strategy: hashmap lookup is O(1), so we trade space for time
        # Key insight: for each number n, we need (target - n) to exist somewhere
        # We check BEFORE inserting to avoid using the same index twice (i != j)
        prevMap = {}  # {value: index}
        for i, n in enumerate(nums):
            diff = target - n  # the complement we're looking for (so essentialy im checking if the complement which matches n is in my dict)
            if diff in prevMap:
                # prevMap[diff] is always the smaller index since we iterate left to right
                return [prevMap[diff], i]
            prevMap[n] = i  # store current number AFTER checking, so we don't match with itself

        # Time:  O(n) — single pass
        # Space: O(n) — hashmap stores up to n entries
        # vs. brute force: O(n²) time, O(1) space (nested loops checking every pair)

        # -------------------------------------------------------------------
        # WHY WE CHECK BEFORE INSERTING INTO prevMap
        # -------------------------------------------------------------------
        # The problem requires i != j — you can't use the same index twice.
        # The order of operations inside the loop protects against this.
        #
        # The rule: a number can only match with numbers from PREVIOUS iterations,
        # never with itself at the current step.
        #
        # BUGGY version (insert first, then check):
        #
        #   nums = [3, 3], target = 6
        #
        #   i=0, n=3
        #     prevMap = {3: 0}        ← inserted first
        #     diff = 6 - 3 = 3
        #     is 3 in prevMap? YES    ← matches itself!
        #     return [0, 0]           ← WRONG, same index used twice
        #
        # CORRECT version (check first, then insert):
        #
        #   i=0, n=3
        #     diff = 3
        #     is 3 in prevMap? NO     ← map is still empty, nothing to match against
        #     prevMap = {3: 0}        ← now insert
        #
        #   i=1, n=3
        #     diff = 3
        #     is 3 in prevMap? YES    ← finds index 0 from the previous iteration
        #     return [0, 1]           ← CORRECT, two different indices
        #
        # Key takeaway: by inserting AFTER the check, the current number is never
        # in the map when we look it up. So a match can only come from a number
        # we already passed, guaranteeing the two indices are always different.
        # -------------------------------------------------------------------

        '''
        Case 1: The duplicate pair IS the answer


nums = [3, 3], target = 6

i=0, n=3: map is empty, no match → insert {3: 0}
i=1, n=3: diff=3, found in map at index 0 → return [0, 1] ✓
Works because the first 3 is already stored when the second 3 is checked.

Case 2: Duplicates exist but aren't the answer


nums = [3, 3, 5], target = 8

i=0, n=3: diff=5, not in map → insert {3: 0}
i=1, n=3: diff=5, not in map → insert {3: 1}  ← overwrites index 0
i=2, n=5: diff=3, found in map at index 1 → return [1, 2] ✓
Here the map overwrites the old duplicate with the newer index. 
This is fine because the problem guarantees exactly one valid answer — 
so you'll never have a situation where overwriting causes you to miss the correct pair.

Bottom line: duplicates are handled correctly in both cases, 
and the overwrite behavior is safe because of the one-valid-answer guarantee in the problem constraints.
'''