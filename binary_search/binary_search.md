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

**Why `l <= r`:** When `l == r`, there's exactly one element left and you don't know yet if it's the target — you need to check it. `l <= r` lets you inspect it. If it's not the target, `l` or `r` moves past it and the loop ends cleanly.

**Why `mid + 1` and `mid - 1`:** You already checked `mid` — it's not the target. So there's no reason to include it in the next search. `mid + 1` / `mid - 1` cuts it out. If you used just `mid`, `l` or `r` would never move when `l == mid`, causing an infinite loop.

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

### 2. Binary search on rotated sorted array — find minimum
**Problem:** Find Minimum in Rotated Sorted Array (LC 153)

A sorted array got rotated, creating two "hills" — a left hill (bigger numbers) and a right hill (smaller numbers). The minimum is always the first element of the right hill (right after the drop).

**The key insight:** Compare `nums[mid]` to `nums[r]` to figure out which hill `mid` is on:
- `nums[mid] > nums[r]` → mid is on the **left hill** (bigger side). The drop hasn't happened yet — minimum is to the right → `l = mid + 1`
- `nums[mid] < nums[r]` → mid is on the **right hill** (smaller side). The drop already happened — minimum is at mid or to the left → `r = mid`

**Why `r = mid` not `r = mid - 1`:** mid itself could be the minimum — you can't exclude it.

**Why `l = mid + 1` not `l = mid`:** mid is already confirmed to NOT be the minimum (it's on the bigger hill). If you set `l = mid`, when `l == mid`, l never moves → infinite loop.

**Why `l < r` not `l <= r`:** You're not looking for a specific value — you're narrowing down to a position. When `l == r`, both pointers have converged on the minimum by the logic of the algorithm. No need to check it, just return it. With `l <= r`, you'd run one extra unnecessary iteration.

```
l, r = 0, len(nums) - 1

while l < r:
    mid = (l + r) // 2
    if nums[mid] < nums[r]:
        r = mid          # mid is on right hill, minimum is here or left
    else:
        l = mid + 1      # mid is on left hill, minimum is to the right

return nums[l]           # l == r, both point at the minimum
```

- Time: O(log n)
- Space: O(1)

**Trace through `[3,4,5,6,1,2]`:**
- l=0, r=5, mid=2 → nums[2]=5 > nums[5]=2 → left hill → l=3
- l=3, r=5, mid=4 → nums[4]=1 < nums[5]=2 → right hill → r=4
- l=3, r=4, mid=3 → nums[3]=6 > nums[4]=1 → left hill → l=4
- l=4, r=4 → loop ends → return nums[4] = 1 ✓
