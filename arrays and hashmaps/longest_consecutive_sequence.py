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
        #transform nums into a set for O(1) look ip
        longest = 0 #handles the empty case
        for n in hashset:  
        #for each number in nums ill check if that number -1 is in the set
        #if it is not it can be the start of a seq  
            if (n-1) not in hashset:
                length = 1 #1 including start
                while (n+length) in hashset: #count how many consecutives are in the set
                        length+=1
                longest = max(longest, length) #go seq by seq assign largest to longest
        return longest


