# 101. Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# Difficulty: Easy
#
# Given the root of a binary tree, check whether it is a mirror of itself
# (i.e., symmetric around its center).
#
# Example 1:
#   Input:  root = [1, 2, 2, 3, 4, 4, 3]
#   Output: true
#
# Example 2:
#   Input:  root = [1, 2, 2, null, 3, null, 3]
#   Output: false
#
# Constraints:
#   The number of nodes in the tree is in the range [1, 1000].
#   -100 <= Node.val <= 100

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # empty tree is trivially symmetric (also guards against root.left crash below)
        if not root:
            return True

        # helper: takes TWO subtrees and returns True if they are mirrors of each other
        # nested so we don't have to deal with `self.` everywhere
        def dfs(left, right):
            # base case 1: both empty → trivially mirrors
            if not left and not right:
                return True
            # base case 2: exactly one empty → structures differ, can't be mirrors
            if not left or not right:
                return False
            # base case 3: both exist but values differ
            if left.val != right.val:
                return False

            # recursive case: criss-cross compare
            #   outer pair: left.left  vs right.right
            #   inner pair: left.right vs right.left
            # this diagonal recursion is what makes it MIRROR instead of SAME
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)

# Approach: Pairwise DFS comparing left and right subtrees in CRISS-CROSS fashion.
# Same template as isSameTree (#100), but recursion goes diagonally instead of straight down.
# A tree is symmetric iff its left subtree is a mirror image of its right subtree.
#
# Time:  O(n) — every node is visited at most once
# Space: O(h) — recursion stack depth = height of the tree
#
# Why O(h) and not O(n)?
# Each recursive call pushes a frame onto the call stack. Frames pop off as calls return.
# The DEEPEST the stack ever gets is when we're at the FARTHEST leaf — that's `h` frames
# (one per level from root to leaf). Even though there are n total nodes, only one path
# from root to leaf exists in memory at any moment, because DFS dives one path at a time
# and frees frames as it backtracks.
#   - Balanced tree:  h = log n → O(log n) space
#   - Skewed tree:    h = n     → O(n) space (worst case, basically a linked list)
