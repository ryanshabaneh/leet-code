# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy

'''
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome reads the same forward and backward.
It is case-insensitive and ignores all non-alphanumeric characters.

Example 1:
Input: s = "Was it a car or a cat I saw?"
Output: true
Explanation: "wasitacaroracatisaw" is a palindrome.

Example 2:
Input: s = "tab a cat"
Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:
1 <= s.length <= 1000
s consists of only printable ASCII characters.
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start, end = 0, len(s) - 1

        while start < end:
            while start < end and s[start].isalnum() == False:
                start += 1
            while start < end and s[end].isalnum() == False:
                end -= 1
            if s[start]!=s[end]:
                return False
            start += 1
            end -= 1
        return True

"""
Approach: Two Pointers

Key insight: use a left and right pointer moving toward each other.
At each step, skip non-alphanumeric characters, then compare.
If any pair doesn't match, it's not a palindrome. If the pointers
cross without a mismatch, it is.

Why lowercase first?
    Case-insensitive comparison — do it once upfront so you don't have
    to call .lower() on every character comparison inside the loop.

Why while (not if) for skipping?
    A single non-alphanumeric character needs one skip, but "###racecar"
    needs three. `if` only skips once then compares. `while` keeps skipping
    until you hit a valid character.

Why does the inner while also need `start < end`?
    If the entire string is non-alphanumeric (e.g. "####"), the pointers
    would keep moving past each other and go out of bounds without it.
    The guard ensures we stop safely.

Even vs odd length strings:
    No special handling needed. If odd, start == end at the middle —
    the outer while condition `start < end` is false so we stop.
    If even, the pointers become adjacent and then cross — same result.

"####" edge case:
    All characters are skipped, start reaches end, loop exits, returns True.
    An empty or all-symbol string is considered a palindrome.

Time:  O(n) — each character is visited at most once by each pointer
Space: O(n) — s.lower() creates a new string (could avoid with .lower() per char to get O(1))

Key pattern: two pointers moving inward is the go-to for palindrome checks
and any problem where you're comparing elements from both ends of a sequence.
"""


        




