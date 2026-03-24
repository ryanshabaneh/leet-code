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
Notes:
Even if string is length 1,000,000: "aaaaabbbbbccccc..." My dict size is STILL ≤ 26 
Time complexity: O ( n + m ) 
Space complexity: O(1) since we have at most  26 different characters.

Remember to check length right away
Key Insight You can process both strings in one pass

'''



