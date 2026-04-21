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

        l, r = 0, len(nums) - 1

        # loop until l and r converge on the minimum
        while l < r:
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                # mid is on the right (smaller) hill — drop already happened
                # minimum is at mid or to the left
                r = mid
            else:
                # mid is on the left (bigger) hill — drop hasn't happened yet
                # minimum is to the right of mid
                l = mid + 1  # mid + 1 not mid, or l never moves and we loop forever

        # l == r, both pointing at the minimum
        return nums[l]

# Time: O(log n) — halving the search space each iteration
# Space: O(1)



