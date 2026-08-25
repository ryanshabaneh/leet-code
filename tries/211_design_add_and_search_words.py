# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
# Difficulty: Medium
#
# Design a data structure that supports adding new words and finding if a string
# matches any previously added string.
#
# Implement the WordDictionary class:
#
#   WordDictionary()            Initializes the object.
#   addWord(word)               Adds word to the data structure, it can be
#                               matched later.
#   search(word) -> bool        Returns True if there is any string in the data
#                               structure that matches word, or False otherwise.
#                               word may contain dots '.' where a dot can match
#                               any letter.
#
# Example:
#   Input:
#     ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
#     [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
#   Output:
#     [null,null,null,null,false,true,true,true]
#   Explanation:
#     wd = WordDictionary()
#     wd.addWord("bad")
#     wd.addWord("dad")
#     wd.addWord("mad")
#     wd.search("pad")   # return False
#     wd.search("bad")   # return True
#     wd.search(".ad")   # return True  ('.' matches b/d/m)
#     wd.search("b..")   # return True  ('bad')
#
# Constraints:
#   1 <= word.length <= 25
#   word in addWord consists of lowercase English letters.
#   word in search consists of '.' or lowercase English letters.
#   There are at most 2 dots in word for search queries.
#   At most 10^4 calls will be made to addWord and search.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:
                cur = children[char]
            else:
                cur.children[char] = TrieNode() 
                cur = children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        pass
