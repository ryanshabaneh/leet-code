# Binary Search

Binary search finds a target in a **sorted** array in O(log n) by repeatedly halving the search space.

Instead of checking every element, you check the middle. If it's too big, search the left half. If it's too small, search the right half.

```
l, r = 0, len(nums) - 1

while l <= r:
    mid = (l + r) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        l = mid + 1   # target is in the right half
    else:
        r = mid - 1   # target is in the left half

return -1
```

- Time: O(log n)
- Space: O(1)

---

## Key details

- `l <= r` not `l < r` — you need to check when l and r converge on one element
- `mid = (l + r) // 2` — integer division, always rounds down
- Move `l = mid + 1` and `r = mid - 1` (not `mid`) to avoid infinite loops
- Only works on **sorted** input

---

## When to reach for binary search

- Array is sorted and you're searching for a value
- You're asked for O(log n) search
- The answer space is monotonic — you can ask "is X too big or too small?" and eliminate half
  - e.g. "find minimum X such that condition holds" → binary search on the answer

---

## Patterns from Problems Solved

### 1. Classic binary search
**Problem:** Binary Search (LC 704)

Standard template above. Find target in sorted array, return index or -1.
