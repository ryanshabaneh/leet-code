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
        charSet = set()  # tracks characters currently in the window
        l = 0
        longest = 0

        for r in range(len(s)):
            # r drives the loop — it's the right edge of the window
            # at each step we ask: "what's the longest valid window ending here at r?"

            while s[r] in charSet:
                # duplicate found — window is invalid
                # shrink from the left until the duplicate is gone
                # we remove s[l] (not s[r]) because we're kicking out the leftmost char
                charSet.remove(s[l])
                l += 1
            # now s[r] is safe to add — no duplicates in the window
            charSet.add(s[r])
 
            # r - l + 1 = current window size (inclusive on both ends)
            # e.g. l=0, r=2 → 3 chars (indices 0, 1, 2)
            longest = max(longest, r - l + 1)

        return longest

"""
Approach: Sliding Window with a Set

Key insight: you never need to check every possible substring (that's O(n²)).
Instead, maintain the best valid window at each position:
  - Greedily grow right: expand r as long as no duplicates
  - Shrink from left only when forced: when s[r] is already in the set,
    pop from the left until the duplicate is gone (minimum shrink)
  - l never moves backwards — any window to the left has already been seen
    and was either invalid or shorter than what's been recorded

At every r, you're finding the longest valid window that ends at r.
Across all r values, you've covered every possible best window.

Time:  O(n) — each character is added and removed from the set at most once
Space: O(n) — set holds at most min(n, alphabet_size) characters
"""

