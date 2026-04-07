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
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j=i
            while s[j] != "#":
                j += 1
            length = int(s[i:j]) #handles the case len is > 9
            res.append(s[j+1: j+1 + length])
            i = j+1+length
        return res

        

"""
Concatenating strings loses boundaries, so decoding fails.
A delimiter seems like a natural fix.
But a plain delimiter is unsafe because the original strings can also contain that character.
So I need something unambiguous.
A good way is to store each string as:
length + "#" + string
Then when decoding, I read the length first,
and use it to know exactly how many characters belong to the next string.

Why encode works:
The problem is that joining strings together loses track of where one ends and the next begins.
For example ["ab", "cd"] and ["a", "bcd"] both become "abcd" — impossible to decode.

A plain delimiter like "#" doesn't work either because the strings themselves can contain "#".
So ["he#llo", "world"] becomes "he#llo#world" — you can't tell which "#" is the delimiter.

The fix is to prefix each string with its length:
    ["Hello", "World"]  →  "5#Hello5#World"
    ["he#llo", "world"] →  "6#he#llo5#world"

When decoding, you never guess where a string ends — you read the number before "#",
and that tells you exactly how many characters to grab after it.
The "#" inside string content is irrelevant because you're counting characters, not scanning for "#".

So "6#he#llo5#world":
    - read 6, skip "#", grab next 6 chars → "he#llo"
    - read 5, skip "#", grab next 5 chars → "world"

The length prefix makes it unambiguous no matter what characters are in the strings.
"""