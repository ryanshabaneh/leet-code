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
        freq = [[] for i in range(len(nums) + 1)]
        # +1 because index = frequency, and max frequency = len(nums)
        # without +1, valid indices are 0..n-1, so freq[n] would be out of bounds
        # index 0 is always empty (no number appears 0 times)

        for num in nums:
            count[num] = 1 + count.get(num, 0)
    
        for n, c in count.items():
            freq[c].append(n) 
            
        res = []
        for i in range(len(frequency)-1, 0, -1):
            for n in freq[i]:
                res.append[n]
                if len(res) == k:
                    return res

"""
Approach: Bucket Sort

Key insight: the maximum frequency any number can have is len(nums)
(if all elements are the same). This lets us use bucket sort where
index = frequency, giving us O(n) instead of O(n log n) from sorting.

Step 1 — build a count map: { number: frequency }
    e.g. [1,1,1,2,2,3] → {1:3, 2:2, 3:1}

Step 2 — build freq buckets of size n+1 (need +1 so index n is valid):
    index = how many times a number appears
    freq[1] = [3], freq[2] = [2], freq[3] = [1]

    Note: index 0 is always empty (no number appears 0 times)
    Multiple numbers can share the same bucket, e.g. freq[2] = [9, 10]

Step 3 — walk backwards from the end, collecting numbers until we have k:
    The problem guarantees a unique answer so we never need to partially
    take from a bucket — we always hit exactly k.

Time:  O(n) — counting is O(n), bucket fill is O(n), walk-back is O(n)
Space: O(n) — count dict + freq array both scale with input size

"""
