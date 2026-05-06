# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# Difficulty: Medium
#
# Given the root of a binary tree, return true if it is a valid binary search
# tree (BST), otherwise return false.
#
# A valid BST satisfies:
#   - The left subtree of every node contains only nodes with keys LESS THAN the node's key.
#   - The right subtree of every node contains only nodes with keys GREATER THAN the node's key.
#   - Both the left and right subtrees are also BSTs.
#
# Example 1:
#   Input:  root = [2, 1, 3]
#   Output: true
#
# Example 2:
#   Input:  root = [5, 1, 4, null, null, 3, 6]
#   Output: false
#   Explanation: The right subtree of root contains a value (3) less than root.
#
# Constraints:
#   The number of nodes in the tree is in the range [1, 10^4].
#   -2^31 <= Node.val <= 2^31 - 1

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, lowLeft, highRight):
            if not node:
                return True
            if not (lowLeft < node.val < highRight):
                return False
            return valid(node.left, lowLeft, node.val) and valid(node.right, node.val, highRight)
        return valid(root, float('-inf'), float('inf'))

     
# Time:  O(n) — visit every node at most once
# Space: O(h) — recursion stack = tree height (log n balanced, n skewed)
