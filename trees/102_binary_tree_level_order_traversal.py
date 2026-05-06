# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Difficulty: Medium
#
# Given the root of a binary tree, return the level order traversal of its
# nodes' values as a nested list, where each sublist contains the values of
# nodes at a particular level in the tree, from left to right.
#
# Example 1:
#   Input:  root = [1, 2, 3, 4, 5, 6, 7]
#   Output: [[1], [2, 3], [4, 5, 6, 7]]
#
# Example 2:
#   Input:  root = [1]
#   Output: [[1]]
#
# Example 3:
#   Input:  root = []
#   Output: []
#
# Constraints:
#   0 <= number of nodes <= 1000
#   -1000 <= Node.val <= 1000

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []

        q = deque([root])
        while q:
            level = []
            qlen = len(q)
            for _ in range(qlen):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level)
        return result


        
            

