# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# Difficulty: Easy
#
# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest LEAF node.
#
# Note: A leaf is a node with no children.
#
# Example 1:
#   Input:  root = [3, 9, 20, null, null, 15, 7]
#   Output: 2
#
# Example 2:
#   Input:  root = [2, null, 3, null, 4, null, 5, null, 6]
#   Output: 5
#
# Constraints:
#   The number of nodes in the tree is in the range [0, 10^5].
#   -1000 <= Node.val <= 1000

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not (root.left or root.right):
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)

        #case where I have both children
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

# Time:  O(n) — visit every node at most once
# Space: O(h) — recursion stack = tree height (h = log n balanced, n worst-case skewed)
