# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# Difficulty: Hard
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# Example 1:
#   Input:  root = [1, 2, 3, null, null, 4, 5]
#   Output: [1, 2, 3, null, null, 4, 5]
#
# Example 2:
#   Input:  root = []
#   Output: []
#
# Constraints:
#   0 <= number of nodes <= 10^4
#   -1000 <= Node.val <= 1000

from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(res)
            


    def deserialize(self, data: str) -> Optional[TreeNode]:
        
        vals = data.split(",")
        d = deque(vals)
        def dfs():
            x = d.popleft()
            if x == "N":
                return None
            node = TreeNode(x)
