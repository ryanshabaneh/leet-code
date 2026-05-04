# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
# Difficulty: Easy
#
# Given the roots of two binary trees root and subRoot, return true if there
# is a subtree of root with the same structure and node values as subRoot,
# and false otherwise.
#
# A subtree of a binary tree tree is a tree that consists of a node in tree
# and all of this node's descendants. The tree tree could also be considered
# as a subtree of itself.
#
# Example 1:
#   Input:  root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]
#   Output: true
#
# Example 2:
#   Input:  root = [3, 4, 5, 1, 2, null, null, null, null, 0], subRoot = [4, 1, 2]
#   Output: false
#
# Constraints:
#   The number of nodes in the root tree is in the range [1, 2000].
#   The number of nodes in the subRoot tree is in the range [1, 1000].
#   -10^4 <= root.val <= 10^4
#   -10^4 <= subRoot.val <= 10^4

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: walked off the end of root without finding a match
        if not root:
            return False

        # is the subtree starting AT THIS node the same as subRoot?
        if self.isSameTree(root, subRoot):
            return True

        # otherwise, search both subtrees — match might be deeper down
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # standard "are these two trees identical?" helper (same as problem #100)
        if not (p or q):
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# Approach: Two-layer recursion.
#   Outer (isSubtree): walks every node in `root`, asking at each one,
#                      "is the subtree here identical to subRoot?"
#   Inner (isSameTree): the standard pairwise-DFS comparison.
# The first node where isSameTree returns True is a hit; if we exhaust root → False.
#
# Time:  O(m * n) — m = nodes in root, n = nodes in subRoot.
#                   isSubtree visits each of m nodes, and at each one isSameTree
#                   may walk up to n nodes before deciding.
# Space: O(m + n) — two recursion stacks: isSubtree's stack is O(height of root),
#                   and the isSameTree call inside it adds O(height of subRoot).
#                   Worst case both trees are skewed → O(m + n).