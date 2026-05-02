# 23. Merge K Sorted Linked Lists
# https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Hard
#
# You are given an array of k linked lists lists, where each list is sorted
# in ascending order.
#
# Return the sorted linked list that is the result of merging all of the
# individual linked lists.
#
# Example 1:
#   Input:  lists = [[1, 2, 4], [1, 3, 5], [3, 6]]
#   Output: [1, 1, 2, 3, 3, 4, 5, 6]
#
# Example 2:
#   Input:  lists = []
#   Output: []
#
# Example 3:
#   Input:  lists = [[]]
#   Output: []
#
# Constraints:
#   0 <= lists.length <= 1000
#   0 <= lists[i].length <= 100
#   -1000 <= lists[i][j] <= 1000

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                #careful not to go out of bands say i is at my last element/head
                l2 = lists[i + 1]
                
        

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2
        return dummy.next

        


