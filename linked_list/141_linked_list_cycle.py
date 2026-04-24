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
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
    
'''
Hashset solution

seen = set()
node = head
while node:
    if node in seen:
        return True
    seen.add(node)
    node = node.next
return False
'''


