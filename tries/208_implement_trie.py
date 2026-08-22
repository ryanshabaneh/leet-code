# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
# Difficulty: Medium
#
# A trie (pronounced "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are various
# applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
#   Trie()                  Initializes the trie object.
#   insert(word)            Inserts the string word into the trie.
#   search(word)  -> bool   Returns True if word is in the trie (i.e. was
#                           inserted before), and False otherwise.
#   startsWith(prefix) -> bool
#                           Returns True if there is a previously inserted string
#                           word that has the prefix prefix, and False otherwise.
#
# Example:
#   Input:
#     ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
#     [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
#   Output:
#     [null, null, true, false, true, null, true]
#   Explanation:
#     trie = Trie()
#     trie.insert("apple")
#     trie.search("apple")      # returns True
#     trie.search("app")        # returns False (only "apple" was inserted)
#     trie.startsWith("app")    # returns True  (prefix of "apple")
#     trie.insert("app")
#     trie.search("app")        # returns True  (now inserted)
#
# Constraints:
#   1 <= word.length, prefix.length <= 2000
#   word and prefix consist only of lowercase English letters.
#   At most 3 * 10^4 calls total to insert, search, and startsWith.


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char in cur.children:  #maybe need get()?
                cur = cur.children[char]
            else:
                cur.children[char] = TrieNode()
                cur = cur.children[char]
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if not (char in cur.children):
                return False
            cur = cur.children[char]
        '''
        if (cur.end == True):
            return True    
        return False
        '''
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if not (char in cur.children):
                return False
            cur = cur.children[char]
        return True
