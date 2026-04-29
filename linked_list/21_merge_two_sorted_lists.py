# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Difficulty: Easy
#
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted linked list and return the head of
# the new sorted linked list. The new list should be made up of nodes from
# list1 and list2.
#
# Example 1:
#   Input: list1 = [1,2,4], list2 = [1,3,5]
#   Output: [1,1,2,3,4,5]
#
# Example 2:
#   Input: list1 = [], list2 = [1,2]
#   Output: [1,2]
#
# Example 3:
#   Input: list1 = [], list2 = []
#   Output: []
#
# Constraints:
#   0 <= length of each list <= 100
#   -100 <= Node.val <= 100

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy is a placeholder node sitting in front of the real head.
        # It lets the first append use the same code as every other append,
        # avoiding a special case for "what's the head of the merged list?".
        dummy = ListNode()

        # `tail` always points to the last node of the merged list so far.
        # We attach new nodes via `tail.next` and advance `tail` forward.
        tail = dummy

        # Walk both lists in lockstep. On each iteration, pick the smaller
        # front node and splice it onto the tail of the merged list.
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1     # splice l1's front node onto our list
                l1 = l1.next       # advance l1 past the node we just took
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next       # tail moves forward to the node we just appended

        # When the loop exits, AT LEAST one list is empty. Whatever's left
        # in the other list is already sorted and already linked together,
        # so we can attach the entire remaining chain in one shot.
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # dummy.next is the actual head of the merged list (skip the placeholder).
        return dummy.next
