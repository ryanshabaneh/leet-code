# Linked Lists

A linked list is a chain of nodes where each node holds a value and a pointer to the next. Unlike arrays, nodes are scattered in memory — the only way to reach node `k` is to walk from the head, following `.next` pointers. No `head + n` arithmetic; no random access.

---

## Why this changes how you think

- **No index access.** O(1) lookup by index is gone. Walking to position `k` is O(k).
- **Mutations are pointer surgery.** Insertion and deletion are O(1) *if you already have a pointer to the node before the change point* — you just rewire `.next`.
- **You only need access to the predecessor to delete.** `prev.next = prev.next.next` removes `prev.next` from the list. Python's GC frees the orphaned node automatically (no manual `free()`).
- **Dummy nodes simplify edge cases.** A dummy `ListNode(0, head)` placed before the head means head-removal stops being a special case — the "predecessor" of the head is just the dummy.

---

## Patterns from Problems Solved

### 1. Two-pointer fixed window — find a node by offset (Remove Nth From End)

The trick: you can't index into a linked list, but you *can* maintain a fixed gap between two pointers. Offset one pointer by `k` steps, then walk both in lockstep. When the leading one hits the end, the trailing one is exactly `k` nodes behind — i.e., the kth-from-end node, in a single pass.

```python
dummy = ListNode(0, head)
left, right = dummy, head

for _ in range(n):              # open a gap of n+1 nodes between left and right
    right = right.next

while right:                    # slide the window until right falls off the end
    right = right.next
    left = left.next

left.next = left.next.next      # left is now the predecessor of the target — splice it out
return dummy.next
```

> **Why offset by `n` with `left = dummy` (not `left = head` with offset `n`)?** We need `left` to land on the *predecessor* of the target so we can rewire its `.next`. Starting `left` one node earlier (at the dummy) shifts the landing point back by one — which is exactly the predecessor.
>
> **Why the dummy at all?** It collapses the "remove the head" edge case. Without it, removing the head needs a separate branch (`return head.next`). With it, `dummy.next` is whatever the new head is — original or the old second node.
>
> **Why return `dummy.next`, not `head`?** Because `head` may have been the node we just removed. `dummy.next` always points to the current first real node.

**Complexity:**
- **Time: O(L)** where L is the length of the list. The first loop walks `n` steps; the second loop walks the remaining `L - n` steps. Total: L. Single pass.
- **Space: O(1).** Just three pointers (`dummy`, `left`, `right`) regardless of list size. No recursion, no extra structures.

**This pattern generalizes to:** "find the kth-from-end node," "find the middle of a list" (use a fast pointer moving 2x), "detect a cycle" (Floyd's tortoise and hare — same idea, different gap behavior).
