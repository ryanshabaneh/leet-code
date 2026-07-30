# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/
# Difficulty: Medium
#
# You are given an array of distinct integers nums and a target integer target.
# Return a list of all unique combinations of nums where the chosen numbers sum
# to target.
#
# The same number may be chosen from nums an unlimited number of times. Two
# combinations are the same if the frequency of each chosen number is the same.
#
# You may return the combinations in any order.
#
# Example 1:
#   Input:  nums = [2,5,6,9], target = 9
#   Output: [[2,2,5],[9]]
#
# Example 2:
#   Input:  nums = [3,4,5], target = 16
#   Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]
#
# Example 3:
#   Input:  nums = [3], target = 5
#   Output: []
#
# Constraints:
#   All elements of nums are distinct.
#   1 <= nums.length <= 20
#   2 <= nums[i] <= 30
#   2 <= target <= 30

from typing import List

# Scratch: backtracking — make a choice, recurse, undo the choice.

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        pass
