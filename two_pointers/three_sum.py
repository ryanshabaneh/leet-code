# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = [0,1,1]
# Output: []
#
# Example 3:
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
#
# Constraints:
# - 3 <= nums.length <= 1000
# - -10^5 <= nums[i] <= 10^5

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, x1 in enumerate(nums):
        if x1 > 0:
            break #impossible to get 0 since x1+x2 = -x1 if x1 is pos x2, x3 are post cant sum to zero
        if i > 0 and x1 == nums[i-1]:
            continue
            # skip the SECOND duplicate, not the first — the first already found all triplets with this value
            # if first uses second this would work but if the second also needs the first wouldnt work
            #checking i > 0 avoids nums[-1] (last element) on the first iteration
        l,r = i+1, len(nums) - 1
        while l<r:
            if nums[l]+nums[r] == -x1:
                res.extend([x1,nums[l],nums[r]])
            
