# Two Pointers

The core idea: place two pointers at different positions in an array or string and move them based on some condition — avoiding the O(n²) cost of checking every pair with nested loops.

---

## When to reach for two pointers

- The input is a sorted array (or can be sorted)
- You're searching for a pair, triplet, or subarray that satisfies a condition
- You're comparing elements from both ends of a sequence
- The problem asks you to do something in O(n) that naively requires O(n²)

---

## Patterns from Problems Solved

### 1. Inward pointers — compare from both ends (Valid Palindrome)
Start one pointer at the left, one at the right, and move them toward each other. Useful for symmetry checks and pair-finding on sorted arrays.

```python
l, r = 0, len(s) - 1
while l < r:
    # skip invalid characters
    while l < r and not s[l].isalnum():
        l += 1
    while l < r and not s[r].isalnum():
        r -= 1
    if s[l] != s[r]:
        return False
    l += 1
    r -= 1
return True
```

> Use `while` (not `if`) for skipping — there can be multiple characters to skip in a row.  
> The inner `while` also needs the `l < r` guard to avoid going out of bounds if all characters are invalid.

---

### 2. Inward pointers on sorted array — find a pair (Two Sum II)
When the array is sorted, you can find a pair summing to a target in O(n). Too big → shrink from the right. Too small → grow from the left. No hashmap needed.

```python
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s > target:
        r -= 1
    elif s < target:
        l += 1
    else:
        return [l + 1, r + 1]  # 1-indexed
```

> This only works because the array is sorted — a larger index means a larger value, so pointer direction is meaningful.

---

### 3. Outer loop + inner two pointers — find triplets (3Sum)
Fix one element with an outer loop, then reduce to a two-pointer pair search on the rest. Sort first to enable both the pointer logic and duplicate skipping.

```python
nums.sort()
for i, x1 in enumerate(nums):
    if x1 > 0:
        break  # sorted: everything to the right is also positive, can't sum to 0
    if i > 0 and x1 == nums[i - 1]:
        continue  # skip duplicate x1 values — first occurrence already found all triplets
    l, r = i + 1, len(nums) - 1
    while l < r:
        total = x1 + nums[l] + nums[r]
        if total > 0:
            r -= 1
        elif total < 0:
            l += 1
        else:
            res.append([x1, nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l - 1]:  # skip duplicate l values
                l += 1
```

> `l < r` must come before `nums[l] == nums[l-1]` in the duplicate skip — Python short-circuits, so if `l >= r` it never touches `nums[l]` and avoids index out of bounds.  
> You only need to skip duplicates for `l` explicitly — `r` adjusts naturally from the `total > 0` branch.

---

### 4. Inward pointers — maximize area (Container With Most Water)
Start at both ends (maximum width) and move the shorter pointer inward. Moving the taller one can never improve the area — width shrinks and the height cap stays the same or gets worse.

```python
l, r = 0, len(heights) - 1
res = 0
while l < r:
    area = min(heights[l], heights[r]) * (r - l)
    res = max(res, area)
    if heights[l] <= heights[r]:
        l += 1  # l is shorter (or equal) — only chance of improvement is moving it
    else:
        r -= 1
```

> This doesn't check every pair — it skips pairs that are provably worse. When you move a pointer, all pairs involving the old position with smaller widths are skipped, but they're all capped at the same short height with less width, so they can never beat what you already checked.  
> When heights are equal, it doesn't matter which pointer you move — both are the same height cap, and the other gets skipped on the next iteration anyway.

---

### 5. Forward pointers — track minimum buy day (Best Time to Buy and Sell Stock)
Both pointers start at the left and move rightward. Order matters here (must buy before sell), so you can't shrink from both ends. `l` tracks the cheapest price seen so far; `r` scans every potential sell day.

```python
l, r = 0, 1
profit = 0
while r < len(prices):
    if prices[r] > prices[l]:           # profitable: try selling today
        profit = max(profit, prices[r] - prices[l])
    else:                               # found a cheaper buy day
        l = r                           # update buy pointer to new minimum
    r += 1
return profit
```

> Key insight: you don't need to compare every pair. `l` compresses all previous buy options into one number — the minimum so far. Once you find a cheaper price, everything before it is irrelevant as a buy day.  
> **When to use forward vs inward pointers:** if the problem has an ordering constraint (buy before sell, left index before right), both pointers start left and march forward. If order doesn't matter (any two elements), shrink from both ends.
