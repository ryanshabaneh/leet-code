# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Medium

'''
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums))]


"""
pre solution thoughts:
first of all i notice that the maximum times a number can show up in this given array is the length of the array
what this sort of means is that i can rep the frequency using bucket sort
so nums that show up once put in pos 1 of arr, twice at pos 2 and so on. pos n would be the case
that all nums are the same. 

the big issue here is that i dont really see how to return the k= whatever part. 
maybe i can walk backwards from the list and once i hit k= target return everything until array[0]?
im not too sure

each index is actually a list so for ex:
[[], [7], [9,10], [3]] is taken as 7 shows up once 9,10 twice so on. but what do i do for the zeroth position?
numbers that show up zero time sounds wrong. anyways. now walking back if i want to return say the 3 most frequent 
it wouldnt just be k=3 then walk back to the start of the array, 
thats because i can have 3 elements at k=3 which is very troublesome.
"""
