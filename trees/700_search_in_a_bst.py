# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/
# Difficulty: Easy
#
# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the
# subtree rooted with that node. If such a node does not exist, return null.
#
# Example 1:
#   Input:  root = [4, 2, 7, 1, 3], val = 2
#   Output: [2, 1, 3]
#
# Example 2:
#   Input:  root = [4, 2, 7, 1, 3], val = 5
#   Output: []
#
# Constraints:
#   The number of nodes in the tree is in the range [1, 5000].
#   1 <= Node.val <= 10^7
#   root is a binary search tree.
#   1 <= val <= 10^7

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)

# Time:  O(h) — h = height of the tree. Each step uses the BST invariant to discard
#               half the remaining tree, so we descend one path from root to leaf.
#               Balanced BST: O(log n). Skewed (worst case): O(n).
# Space: O(h) — recursion stack depth = path length from root to current node.
