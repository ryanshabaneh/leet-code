# 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Difficulty: Medium

'''
Given an array of integers nums, return the length of the longest
consecutive sequence of elements that can be formed.

A consecutive sequence is a sequence where each element is exactly 1
greater than the previous. Elements do not need to be consecutive in
the original array.

Must run in O(n) time.

Example 1:
Input: nums = [2,20,4,10,3,4,5]
Output: 4
Explanation: The longest consecutive sequence is [2,3,4,5]

Example 2:
Input: nums = [0,3,2,5,4,6,1,1]
Output: 7

Constraints:
0 <= nums.length <= 1000
-10^9 <= nums[i] <= 10^9
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0
        for n in hashset:
            if (n-1) not in hashset:  # only start counting from sequence beginnings
                length = 1            # count includes the start number itself
                while (n + length) in hashset:
                    length += 1
                longest = max(longest, length)
        return longest

"""
Approach: HashSet + Sequence Start Detection

Key insight: only start counting from numbers that have no left neighbor (n-1 not in set).
Without this check, you'd recount sequences from every element — e.g. for [2,3,4,5]
you'd count from 2, then again from 3, then again from 4, etc. The n-1 check ensures
you only count each sequence once, from its true starting point.

Why convert to a set first?
    Checking "is n+1 in nums?" on a list is O(n) — you'd scan the whole list each time.
    A set gives O(1) lookup, which is what makes the overall algorithm O(n).

Why iterate over hashset instead of nums?
    Duplicates — if nums has [1,1,2,3], iterating over nums would process 1 twice.
    The set deduplicates automatically so each unique number is only checked once.

Why start length at 1?
    The starting number itself counts as part of the sequence.
    If no consecutive neighbors exist, the sequence is just that one number (length = 1).

Why use a while loop (not a for loop) for counting?
    We don't know in advance how long the sequence is — we keep going until
    the next number isn't in the set. A while loop handles this naturally.

Time:  O(n) — each number is added to the set once, and each number is visited
       at most twice (once in the outer for loop, once inside a while loop chain).
Space: O(n) — the hashset stores up to n unique elements.
"""


