# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Difficulty: Hard
#
# Given the root of a non-empty binary tree, return the maximum path sum of any
# non-empty path.
#
# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes has an edge connecting them. A node cannot appear in the sequence more
# than once. The path does not necessarily need to include the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Example 1:
#   Input:  root = [1, 2, 3]
#   Output: 6
#   Explanation: The path 2 -> 1 -> 3 has sum 2 + 1 + 3 = 6.
#
# Example 2:
#   Input:  root = [-15, 10, 20, null, null, 15, 5, -5]
#   Output: 40
#   Explanation: The path 15 -> 20 -> 5 has sum 15 + 20 + 5 = 40.
#
# Constraints:
#   1 <= number of nodes <= 1000
#   -1000 <= Node.val <= 1000

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
       res = [root.val]

       #return max path without splitting
       def dfs(root): 
        if not root:
            return 0
        
        leftMax = max(dfs(root.left), 0)
        rightMax = max(dfs(root.right), 0)

        res[0] = max(res[0], leftMax + root.val + rightMax)

        return max(leftMax, rightMax) + root.val

        
        
