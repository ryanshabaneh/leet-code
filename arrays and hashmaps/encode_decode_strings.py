# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/
# Difficulty: Medium

'''
Design an algorithm to encode a list of strings to a single string.
The encoded string is then sent over the network and decoded back to
the original list of strings.

Example 1:
Input: strs = ["Hello","World"]
Output: ["Hello","World"]

Example 2:
Input: strs = [""]
Output: [""]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains any possible characters out of 256 valid ASCII characters.
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = str(len(s)) + "#" + s

    def decode(self, s: str) -> List[str]:
        pass

"""
Concatenating strings loses boundaries, so decoding fails.
A delimiter seems like a natural fix.
But a plain delimiter is unsafe because the original strings can also contain that character.
So I need something unambiguous.
A good way is to store each string as:
length + "#" + string
Then when decoding, I read the length first, 
and use it to know exactly how many characters belong to the next string.
"""