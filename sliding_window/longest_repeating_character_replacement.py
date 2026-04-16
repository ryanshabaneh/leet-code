# Longest Repeating Character Replacement
# Medium
#
# You are given a string s consisting of only uppercase English characters
# and an integer k. You can choose up to k characters of the string and
# replace them with any other uppercase English character.
#
# After performing at most k replacements, return the length of the longest
# substring which contains only one distinct character.
#
# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.
#
# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5
#
# Constraints:
# 1 <= s.length <= 1000
# 0 <= k <= s.length

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        count = {} 
        maxfreq = 0 #tracks max freq of a char in every window

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            maxfreq = max(maxfreq, count[s[r]])
            if (r-l+1) - maxf > k:
                count[s[l]] -= 1
        
