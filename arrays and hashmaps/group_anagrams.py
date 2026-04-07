# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium

'''
Given an array of strings strs, group all anagrams together into sublists.
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act","cat"],["stop","pots","tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
'''

from collections import defaultdict

'''
The defaultdict class is a dictionary subclass that simplifies operations involving 
missing keys by providing a default value automatically, preventing a KeyError from being raised.
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #The argument is a function that creates a default value
        #“If a key doesn’t exist, call list() to create a value --> []”
       
       res = defaultdict(list)

        for w in strs:
            count = [0] * 26
            for c in w:
               count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(w)
        return list(res.values)

        # Every word → convert into a 26-length count array

"""

Time: O(m * n) — m strings each of avg length n (building the count array per word)
Space: O(m * n) — storing all strings in the result grouped by their signature

Key pattern: when you need to group items that are "equivalent" by some criteria,
compute a canonical signature for each item and use it as a hashmap key.
Here the signature is a 26-length character count tuple — all anagrams produce
the same tuple, so they naturally fall into the same bucket.
This generalises beyond anagrams: any "group by equivalence" problem likely uses this.
ord() function returns the integer representing the
Unicode code point of a specified character
Example:

ord('a') = 97
ord('b') = 98

So:

ord('a') - ord('a') = 0
ord('b') - ord('a') = 1
ord('c') - ord('a') = 2

maps letters → positions in array

        Notes
---------------------------

defaultdict(list) is literally a shortform of:
res = {}

# BUT secretly:
if key not in res:
    res[key] = []

Counting with defaultdict;

from collections import defaultdict

count = defaultdict(int)

count["a"] += 1
count["a"] += 1
count["b"] += 1

print(count)

First line:
count["a"] += 1 --> "a" does NOT exist --> Python does: int() → 0
So it becomes: count["a"] = 0 + 1 → 1
Second line:
count["a"] += 1 --> "a" exists (value = 1) --> So: 1 + 1 → 2

Third line: 
count["b"] += 1 --> "b" does NOT exist --> Python does: int() → 0
count["b"] = 0 + 1 → 1
Final result: {'a': 2, 'b': 1}

Grouping with defaultdict:

from collections import defaultdict

groups = defaultdict(list)

groups["a"].append(1)
groups["a"].append(2)
groups["b"].append(3)

First line:
groups["a"].append(1)
"a" does NOT exist
Python does: list() → []

So:

groups["a"] = []
groups["a"].append(1) → [1] and so on.


Note: 

from collections import defaultdict

d = defaultdict(list)

d["a"]  # access missing key
print(d)  # {'a': []}
