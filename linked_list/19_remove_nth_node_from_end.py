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
        dummy = ListNode(0, head)
        left, right = dummy, head

        for _ in range(n):
            right = right.next

        while right:
            right = right.next
            left = left.next

        left.next = left.next.next
        return dummy.next


# Pattern: two-pointer fixed window.
# - Offset right by n, then walk both in lockstep until right falls off.
#   left lands on the predecessor of the target.
# - Dummy node makes head-removal a non-special case (predecessor of head = dummy).
# - left.next = left.next.next splices out the target; Python GC handles freeing.
# - Return dummy.next (not head) — head itself may be the removed node.
#
# Time: O(L) — single pass. Space: O(1) — three pointers.
