# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
# Difficulty: Easy
#
# You are given the root of a binary tree root. Invert the binary tree and return its root.
#
# Example 1:
#   Input:  root = [1, 2, 3, 4, 5, 6, 7]
#   Output: [1, 3, 2, 7, 6, 5, 4]
#
# Example 2:
#   Input:  root = [3, 2, 1]
#   Output: [3, 1, 2]
#
# Example 3:
#   Input:  root = []
#   Output: []
#
# Constraints:
#   0 <= number of nodes <= 100
#   -100 <= Node.val <= 100

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # base case: empty tree (or recursion hit a None child) — nothing to invert
        if not root:
            return None

        # swap this node's children in place
        root.left, root.right = root.right, root.left

        # recurse — each child knows how to invert its own subtree
        # no need to capture returns: we mutate in place
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

# Approach: Recursion mirrors the tree's recursive structure.
# At every node: swap left and right children, then trust recursion to fix the subtrees.
#
# Time:  O(n) — visit every node exactly once
# Space: O(h) — recursion stack depth = tree height (h = log n balanced, n worst-case skewed)

