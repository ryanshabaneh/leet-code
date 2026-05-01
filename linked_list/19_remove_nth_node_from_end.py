# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Difficulty: Medium
#
# Given the head of a linked list, remove the nth node from the end of
# the list and return its head.
#
# Example 1:
#   Input:  head = [1, 2, 3, 4, 5], n = 2
#   Output: [1, 2, 3, 5]
#
# Example 2:
#   Input:  head = [1], n = 1
#   Output: []
#
# Example 3:
#   Input:  head = [1, 2], n = 1
#   Output: [1]
#
# Constraints:
#   The number of nodes in the list is sz.
#   1 <= sz <= 30
#   0 <= Node.val <= 100
#   1 <= n <= sz
#
# Follow up: Could you do this in one pass?

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Pattern: two-pointer fixed window. We want left to land on the node
        # BEFORE the target so we can splice via left.next = left.next.next.
        # Dummy node lets us handle "remove the head" without a special case.
        dummy = ListNode(0, head)
        left, right = dummy, head

        # Offset right by n so the gap between left and right is n+1 nodes.
        # When right walks off the end (None), left will be exactly one node
        # before the target.
        for _ in range(n):
            right = right.next

        # Walk both pointers in lockstep until right falls off.
        while right:
            right = right.next
            left = left.next

        # left is now the predecessor of the node to remove. Unlink it —
        # Python's GC reclaims the orphaned node automatically.
        left.next = left.next.next

        # Return dummy.next (not head) because head itself may have been removed.
        return dummy.next

