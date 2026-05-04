# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Difficulty: Easy
#
# Given the root of a binary tree, return its depth.
# The depth of a binary tree is defined as the number of nodes along
# the longest path from the root node down to the farthest leaf node.
#
# Example 1:
#   Input:  root = [1, 2, 3, null, null, 4]
#   Output: 3
#
# Example 2:
#   Input:  root = []
#   Output: 0
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # base case: empty tree has depth 0 (no nodes on any path)
        if not root:
            return 0

        # recursive case: this node contributes 1 to the path,
        # plus the deeper of the two subtrees
        # leap of faith: trust that maxDepth on the children returns the right number
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Approach: Post-order DFS recursion.
# Definition: depth(tree) = 0 if empty, else 1 + max(depth(left), depth(right)).
# The "1" accounts for the current node on the path; the max picks the deeper subtree.
#
# Time:  O(n) — every node is visited exactly once
# Space: O(h) — recursion stack = tree height (h = log n balanced, n worst-case skewed)
