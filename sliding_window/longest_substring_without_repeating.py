# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring
# without duplicate characters.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
# Input: s = "zxyzxyz"
# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.
#
# Example 2:
# Input: s = "xxxx"
# Output: 1
#
# Constraints:
# - 0 <= s.length <= 1000
# - s may consist of printable ASCII characters.

'''
Initial thoughts:
- Sliding window = keep track of a valid subarray, valid = no duplicates
- Use 2P: l and r both start at 0, expand r and add characters to a set
- When s[r] is already in the set (duplicate):
    while s[r] in set: remove s[l], l++
    then add s[r] to the set
- Track max window length throughout
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, longest = 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l=l+1
            charSet.add(s[r])
            pass
            

