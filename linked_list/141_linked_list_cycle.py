# 141. Linked List Cycle Detection
# Easy
#
# Given the beginning of a linked list head, return true if there is a cycle
# in the linked list. Otherwise, return false.
#
# There is a cycle in a linked list if at least one node in the list can be
# visited again by following the next pointer.
#
# Example 1:
# Input: head = [1,2,3,4], index = 1
# Output: true
# Explanation: There is a cycle where the tail connects to the 1st node (0-indexed).
#
# Example 2:
# Input: head = [1,2], index = -1
# Output: false
#
# Constraints:
# 0 <= Length of the list <= 1000
# -1000 <= Node.val <= 1000
# index is -1 or a valid index in the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Floyd's cycle detection (slow/fast pointers)
        # slow moves 1 step, fast moves 2 steps
        # if there's a cycle, fast will lap slow and they'll meet
        # if no cycle, fast hits None and we return False
        slow, fast = head, head

        while fast and fast.next:  # check fast.next too — we do fast.next.next, need it to exist
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # fast caught slow — cycle confirmed
                return True

        return False  # fast hit None, no cycle

# Time: O(n) — two phases:
#   1. slow walks the linear part (m steps) until it enters the cycle
#   2. once slow is in the cycle, fast is somewhere ahead of it.
#      the gap between them is at most c (length of the cycle).
#      fast gains exactly 1 step on slow per iteration (fast moves 2, slow moves 1),
#      so the gap shrinks by 1 each time — they meet within c more steps.
#   total: m + c = O(n)
#
# Why fast can never "skip over" slow:
#   when they're 1 apart → fast moves 2, slow moves 1 → gap becomes 0, they meet.
#   when they're 2 apart → gap becomes 1 → next iteration they meet.
#   the gap only ever shrinks by exactly 1, so it hits 0 before going negative.
#
# Space: O(1) — just two pointers, no extra storage

'''
Hashset solution (simpler but O(n) space):

seen = set()
node = head
while node:
    if node in seen:
        return True
    seen.add(node)   # ListNode objects are hashable by memory address
    node = node.next
return False

Time: O(n), Space: O(n)
'''


