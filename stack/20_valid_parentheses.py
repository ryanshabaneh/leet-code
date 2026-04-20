# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
#
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
# The input string s is valid if and only if:
# - Every open bracket is closed by the same type of close bracket.
# - Open brackets are closed in the correct order.
# - Every close bracket has a corresponding open bracket of the same type.
#
# Return true if s is a valid string, and false otherwise.
#
# Example 1:
# Input: s = "[]"
# Output: true
#
# Example 2:
# Input: s = "([{}])"
# Output: true
#
# Example 3:
# Input: s = "[(])"
# Output: false
# Explanation: The brackets are not closed in the correct order.
#
# Constraints:
# 1 <= s.length <= 1000

class Solution:
    def isValid(self, s: str) -> bool:
        # map each closing bracket to its expected open bracket
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []  # holds unmatched open brackets in order

        for c in s:
            if c in closeToOpen:
                # closing bracket: top of stack must be the matching open bracket
                # check stack is non-empty first to avoid index error on empty stack
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)  # open bracket: push and wait for its match

        # if stack is empty, all brackets were matched; leftover open brackets = invalid
        return not stack

# Time: O(n) — one pass through the string
# Space: O(n) — worst case all open brackets (e.g. "(((((")

