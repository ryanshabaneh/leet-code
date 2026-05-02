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
        # edge case: no input at all → nothing to merge
        if not lists or len(lists) == 0:
            return None

        # Divide-and-conquer: each "round" merges adjacent pairs, halving the
        # number of lists. After log₂(k) rounds, only one merged list remains.
        while len(lists) > 1:
            # buffer for this round's results — built fresh, swapped in at the end
            merged = []

            # walk through `lists` in steps of 2 to grab pairs
            for i in range(0, len(lists), 2):
                l1 = lists[i]

                # if i+1 is out of bounds, this list has no partner this round.
                # set l2 = None and let mergeTwoLists carry l1 through unchanged
                # (the `if l1: tail.next = l1` branch handles a None partner).
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                merged.append(self.mergeTwoLists(l1, l2))

            # buffer-swap: this round's output becomes next round's input
            lists = merged

        # only one list left — that's the fully merged result
        return lists[0]

    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy avoids the "is this the first node?" special case for the head
        dummy = ListNode()
        tail = dummy

        # walk both lists in lockstep; splice the smaller front node onto tail
        while l1 and l2:
            if l1.val > l2.val:
                tail.next = l2
                l2 = l2.next
            else:
                tail.next = l1
                l1 = l1.next
            tail = tail.next

        # one list is exhausted — attach the remaining (already-sorted) tail
        if l1:
            tail.next = l1
        elif l2:
            tail.next = l2

        # dummy.next skips the placeholder and returns the real head
        return dummy.next


"""
Approach: Divide-and-Conquer Pairwise Merging

Key insight: instead of merging lists one at a time into a growing accumulator
(which re-walks early elements over and over), pair lists up and merge in
parallel rounds. Each node is touched only once per round, and we halve the
number of lists each round → log₂(k) rounds total.

Naive (sequential) approach:
    merge(L1, L2) → merge(_, L3) → merge(_, L4) → ...
    The accumulator keeps growing; nodes from L1 get walked k-1 times.
    Time: O(N·k) where N = total nodes, k = number of lists

This (divide-and-conquer):
    Round 1: merge pairs (L1,L2), (L3,L4), (L5,L6), (L7,L8) → 4 lists
    Round 2: merge those pairs                            → 2 lists
    Round 3: merge those                                  → 1 list
    Each round touches every node exactly once = O(N) work per round.

Pattern: Buffer-Swap
    while not_done:
        next_state = []           # fresh buffer
        for thing in current:     # process current state
            next_state.append(...)
        current = next_state      # atomic swap
    Same pattern shows up in BFS level-order, topological sort (Kahn's),
    Game of Life, double-buffered rendering. Anywhere you process in
    discrete rounds where round N+1 depends on the FULL result of round N.

Edge cases:
    - empty input → return None
    - single list → while loop never runs, return lists[0]
    - odd number of lists in a round → lonely one carried via merge(l1, None)

Time:  O(N log k) — N total nodes, log k rounds, each round O(N)
Space: O(1) extra beyond the rewiring (no new nodes allocated; we splice
       existing nodes via .next pointers). The `merged` buffer holds list
       pointers, not nodes — at most k/2 references per round.
"""

        


