# 33. Search in Rotated Sorted Array
# Medium
#
# You are given an array of length n which was originally sorted in ascending order.
# It has now been rotated between 1 and n times. For example, the array
# nums = [1,2,3,4,5,6] might become:
#   [3,4,5,6,1,2] if it was rotated 4 times.
#   [1,2,3,4,5,6] if it was rotated 6 times.
#
# Given the rotated sorted array nums and an integer target, return the index
# of target within nums, or -1 if it is not present.
#
# You may assume all elements in the sorted rotated array nums are unique.
#
# A solution that runs in O(n) is trivial — write one that runs in O(log n).
#
# Example 1:
# Input: nums = [3,4,5,6,1,2], target = 1
# Output: 4
#
# Example 2:
# Input: nums = [3,5,6,0,1,2], target = 4
# Output: -1
#
# Constraints:
# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:  # l <= r because we're searching for a specific value — need to check when l == r
            mid = (l + r) // 2

            if target == nums[mid]:  # found it
                return mid

            # Determine which half is sorted by comparing mid to the left boundary.
            # Use >= to handle the case where l == mid (single element on left).
            if nums[mid] >= nums[l]:
                # Left half [l...mid] is sorted
                if target > nums[mid] or target < nums[l]:
                    # Target is outside the left sorted half — must be in the right
                    l = mid + 1
                else:
                    # Target is within the left sorted half
                    r = mid - 1
            else:
                # Right half [mid...r] is sorted
                if target < nums[mid] or target > nums[r]:
                    # Target is outside the right sorted half — must be in the left
                    r = mid - 1
                else:
                    # Target is within the right sorted half
                    l = mid + 1

        return -1  # target not found

# Time: O(log n) — halving the search space each iteration
# Space: O(1)
                


                

