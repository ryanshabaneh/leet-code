# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Difficulty: Easy
#
# Given the head of a singly linked list, reverse the list and return the reversed list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev = the reversed portion built so far (starts empty -> None)
        # curr = the node we're about to flip (starts at head)
        prev, curr = None, head

        while curr is not None:
            # 1. Save the rest of the list BEFORE we overwrite curr.next,
            #    otherwise we'd be cut off from the remaining nodes.
            nextt = curr.next

            # 2. Flip curr's pointer to face backwards into the reversed portion.
            curr.next = prev

            # 3. Slide the window forward by one node:
            #    prev advances to curr (which is now part of the reversed list),
            #    curr advances to the node we saved in step 1.
            prev = curr
            curr = nextt

        # When curr is None, we've walked off the end of the original list.
        # prev is now sitting on what used to be the tail = the new head.
        return prev
        

     