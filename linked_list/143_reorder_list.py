# 143. Reorder List
# https://leetcode.com/problems/reorder-list/
# Difficulty: Medium
#
# You are given the head of a singly linked list.
# The positions of a linked list of length n are initially represented as:
#   [0, 1, 2, ..., n-1]
#
# Reorder the nodes so the new order is:
#   [0, n-1, 1, n-2, 2, n-3, ...]
#
# You may not modify the values of the nodes — you must reorder the nodes themselves.
#
# Example 1:
#   Input:  head = [2, 4, 6, 8]
#   Output: [2, 8, 4, 6]
#
# Example 2:
#   Input:  head = [2, 4, 6, 8, 10]
#   Output: [2, 10, 4, 8, 6]
#
# Constraints:
#   1 <= length of list <= 1000
#   1 <= Node.val <= 1000
#
# Note: do not return anything; modify head in-place.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        
        second_haf = slow.next
