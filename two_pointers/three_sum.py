# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
# The output should not contain any duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4] ; sorted [-4, -1, -1, 0, 2 ,2]
                                            x1  l            r
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
    nums.sort()  # sorting enables two pointers and makes duplicate skipping trivial (dupes are adjacent)

    for i, x1 in enumerate(nums):
        # if x1 is positive, x2 and x3 (to the right in sorted array) are also positive
        # so x1+x2+x3 > 0 always — no point continuing
        if x1 > 0:
            break

        # skip duplicate values of x1 — the first occurrence already found all triplets with this value
        # i > 0 guard prevents nums[-1] (last element) being checked on the first iteration
        if i > 0 and x1 == nums[i-1]:
            continue

        # l starts just after x1, r starts at the end
        # if x1 is near the end (e.g. 2nd last element), l == r and the while loop doesn't run
        l, r = i + 1, len(nums) - 1

        while l < r:  # l < r ensures we never use the same element twice
            threesum = x1 + nums[l] + nums[r]

            if threesum > 0:
                r -= 1      # sum too big — move r left to get a smaller value
            elif threesum < 0:
                l += 1      # sum too small — move l right to get a bigger value
            else:
                res.append([x1, nums[l], nums[r]])
                l += 1      # move off current value before checking for duplicates
                # skip duplicate values of l — would produce the same triplet with x1 and r
                # l < r guard must come FIRST to avoid index out of bounds
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                # r adjusts naturally from the threesum > 0 branch on the next iteration

    return res

"""
Approach: Sort + Outer Loop + Two Pointers

Key insight: fix x1 with an outer loop, then reduce to a 2Sum problem on the
remaining subarray. Since x1 + x2 + x3 = 0, we need x2 + x3 = -x1.
Use two pointers on the sorted subarray to find that pair in O(n).

Why sort?
    1. Two pointers only work on sorted input — moving l right increases the sum,
       moving r left decreases it. This breaks on unsorted arrays.
    2. Duplicates become adjacent, so skipping them is just one comparison.

Duplicate handling — three levels:
    1. x1: skip if nums[i] == nums[i-1] (already processed this value as x1)
    2. l: after finding a triplet, skip while nums[l] == nums[l-1]
    3. r adjusts naturally — no explicit skip needed

Why l += 1 BEFORE the duplicate skip while loop?
    After appending, l still points at the value we just used. We move it first,
    then check if the new position is a duplicate of what we just used.
    If we skipped first, we'd compare nums[l] to itself and skip valid values.

Why l < r inside the duplicate skip?
    Without it, l could go past r and index out of bounds on an array of all
    the same value e.g. [0, 0, 0, 0].

Time:  O(n²) — outer loop O(n), inner two-pointer O(n) per iteration
Space: O(1) extra — sorting is in-place, only two pointer variables
"""


            
