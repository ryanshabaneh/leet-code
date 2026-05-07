# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Difficulty: Medium
#
# Given the root of a binary search tree (BST), and an integer k, return the
# kth smallest value (1-indexed) in the tree.
#
# A BST satisfies:
#   - The left subtree of every node contains only nodes with keys LESS than the node's key.
#   - The right subtree of every node contains only nodes with keys GREATER than the node's key.
#   - Both the left and right subtrees are also BSTs.
#
# Example 1:
#   Input:  root = [2, 1, 3], k = 1
#   Output: 1
#
# Example 2:
#   Input:  root = [4, 3, 5, 2, null], k = 4
#   Output: 5
#
# Constraints:
#   1 <= k <= number of nodes <= 1000
#   0 <= Node.val <= 1000

from typing import Optional

count = 0

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    self.count = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return # not sure what the empty case is -1? maybe or 
        
        return self.kthSmallest(root.left, k)
        self.count += 1
        if k == self.count:
            return root.val
        return self.kthSmallest(root.right, k)
    



