# 100. Same Tree
# https://leetcode.com/problems/same-tree/
# Difficulty: Easy
#
# Given the roots of two binary trees p and q, write a function to check
# if they are the same or not.
#
# Two binary trees are considered the same if they are structurally
# identical, and the nodes have the same value.
#
# Example 1:
#   Input:  p = [1, 2, 3], q = [1, 2, 3]
#   Output: true
#
# Example 2:
#   Input:  p = [1, 2], q = [1, null, 2]
#   Output: false
#
# Example 3:
#   Input:  p = [1, 2, 1], q = [1, 1, 2]
#   Output: false
#
# Constraints:
#   The number of nodes in both trees is in the range [0, 100].
#   -10^4 <= Node.val <= 10^4

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # base case 1: both empty → trivially the same
        if not (p or q):
            return True

        # base case 2: exactly one is empty (we know not both from above)
        # → structures differ, can't be same
        if not p or not q:
            return False

        # base case 3: both exist but values differ → not same
        if p.val != q.val:
            return False

        # recursive case: both exist with matching values, AND both subtree pairs match
        # leap of faith: trust each recursive call to correctly answer its subtree pair
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Approach: Parallel DFS on two trees, comparing structure and values at each pair.
# Each base case guards against either a trivial answer or a None-attribute crash on the next line.
#
# Time:  O(n) — n = min(|p|, |q|); we stop early on any mismatch
# Space: O(h) — recursion stack = height of the smaller-or-equal tree
