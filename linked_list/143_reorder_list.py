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

        #find middle
        slow, fast = head, head.next 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse second half -> lists cant walk backwards
        second_haf = slow.next
        prev, slow.next = None, None
        while second:
            tmp = second.next
            second.next = prev
            prevv = second
            second = tmp
        
        #merge both the lists
        first, second = head, prev
        while second:
            pass

# Why slow.next = None?
# It's so the first half terminates. Without slow.next = None:
#
# - First half from head: 1 -> 2 -> 3 -> 4 -> 5 -> 6 (the whole list! you never severed it)
# - Second half from second: 4 -> 5 -> 6
#
# When you reverse the second half, node 4's .next gets set to None. So now:
#
# - From head: 1 -> 2 -> 3 -> 4 -> None (because 4's next is now None after reversal)
# - From second (after reversal): 6 -> 5 -> 4 -> None
#
# When you merge, you'd weave: 1, 6, 2, 5, 3, 4, 4 — node 4 appears twice,
# and the merge logic gets confused.
#
# By setting slow.next = None upfront, you cleanly split into:
# - 1 -> 2 -> 3 -> None
# - 4 -> 5 -> 6 -> None
#
# Two independent lists of equal-ish length, ready to merge.
