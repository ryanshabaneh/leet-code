# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Difficulty: Medium
#
# Given a binary search tree (BST) where all node values are unique, and two
# nodes p and q from the tree, return the lowest common ancestor (LCA) of p and q.
#
# The lowest common ancestor of two nodes p and q is the lowest node in the tree
# such that both p and q are descendants of it. A node is allowed to be a
# descendant of itself.
#
# Example 1:
#   Input:  root = [5, 3, 8, 1, 4, 7, 9, null, 2], p = 3, q = 8
#   Output: 5
#
# Example 2:
#   Input:  root = [5, 3, 8, 1, 4, 7, 9, null, 2], p = 3, q = 4
#   Output: 3
#   Explanation: A node can be a descendant of itself, so the LCA of 3 and 4 is 3.
#
# Constraints:
#   2 <= number of nodes <= 100
#   -100 <= Node.val <= 100
#   p != q
#   p and q will both exist in the BST.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        
        #my simplest case is if one of these are none right? 
        if not root:
            pass

        if p.val > root.val and q.val > root.val:
            return lowestCommonAncestor(root.left, p, q)
        elif p.val < root.val and q.val < root.val:
            return lowestCommonAncestor(root.right, p, q)
        #case 3 they split meaning the root im at is their ancestor
        return root # i want to hit this because any 2 nodes will split at some point
        

