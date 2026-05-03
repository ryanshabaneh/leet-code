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
        if not root:
            return None
        root.left, root.right = root.right, root.left
        
        
