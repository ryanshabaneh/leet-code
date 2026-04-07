# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)! = len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get([s[i], 0])
            countT[t[i]] = 1 + countT.get([t[i], 0])
        return countS == countT


'''
Time: O(n + m) — one pass through each string
Space: O(1) — at most 26 keys in each dict regardless of input size

Key pattern: to compare character frequencies between two strings, build a count
map for each and compare them. Anagram problems always reduce to this.
Check lengths first as an early exit — different lengths can never be anagrams.

Notes:
Even if string is length 1,000,000: "aaaaabbbbbccccc..." dict size is STILL ≤ 26
You can process both strings in one pass since they're the same length after the check.

Counter (collections) = built-in frequency hashmap
Counter(s) returns {char: count} automatically
Useful for counting + comparing frequencies (e.g., Counter(s) == Counter(t))
'''



