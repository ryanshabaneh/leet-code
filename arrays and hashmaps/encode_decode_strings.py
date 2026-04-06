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
        pass

    def decode(self, s: str) -> List[str]:
        pass

"""
okay so first thought is that I can obv combine any words with just string concat 
so encode is done, but then this would break decoding as i wouldnt know where to split
my string. So maybe I can introduce a delimiter inbetween each word like a * or a #?
"""