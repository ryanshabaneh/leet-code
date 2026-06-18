 # Minimum Window Substring
# Hard
#
# Given two strings s and t, return the shortest substring of s such that
# every character in t, including duplicates, is present in the substring.
# If such a substring does not exist, return an empty string "".
#
# You may assume that the correct output is always unique.
#
# Example 1:
# Input: s = "OUZODYXAZV", t = "XYZ"
# Output: "YXAZ"
# Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from t.
#
# Example 2:
# Input: s = "xyz", t = "xyz"
# Output: "xyz"
#
# Example 3:
# Input: s = "x", t = "xy"
# Output: ""
#
# Constraints:
# 1 <= s.length <= 1000
# 1 <= t.length <= 1000
# s and t consist of uppercase and lowercase English letters.

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""
        countT, window = {}, {}

        # build frequency map for t
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        # have: # of t's chars whose count is satisfied in current window
        # need: # of distinct chars in t that must be satisfied
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
 
          for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # check if adding c just satisfied one of t's conditions
            if c in countT and window[c] == countT[c]:
                have += 1

            # window is valid — shrink from left to find minimum
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]

                # remove leftmost char from window
                window[s[l]] -= 1
                # if removing it broke a condition, decrement have
                # use < not != because extras (window > countT) are still fine
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1

        l, r = res  # unpack best window indices
        return s[l:r + 1] if resLen != float("infinity") else ""

# Time: O(n + m) — n = len(s), m = len(t). r and l each visit every char in s at most once.
# Space: O(m) — countT and window store at most |charset| entries, bounded by len(t).


        

