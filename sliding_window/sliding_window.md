# Sliding Window

A technique where you maintain a window (a subarray or substring) defined by two pointers `l` and `r`, and slide it across the input. Instead of recomputing the result from scratch each time, you add the new element on the right and remove the old element on the left — keeping the computation O(n) instead of O(n²).

Use it when the problem asks about a contiguous subarray or substring that satisfies some condition (max sum, longest without repeats, etc.).

The algorithm is always:
1. **Greedily grow right** as long as the window is valid
2. **Shrink from left** only when forced to (constraint violated)
3. **Record the max** at every step

---

## Why it's O(n) — "One best candidate per r"

The algorithm does not check every valid substring. It checks **one best candidate per r**. That's why it's O(n) instead of O(n²).

At a fixed index `r`, there are many substrings ending there:

```
s = "abcd", r = 3
"d"     (l=3)
"cd"    (l=2)
"bcd"   (l=1)
"abcd"  (l=0)  ← 4 candidates
```

For a *longest* problem, the best one is always the longest valid one. So you don't need the rest.

**What sliding window finds at each r:** the longest valid substring ending at r — by keeping `l` as far left as possible, only shrinking when forced.

After fixing any violations, `l` is the smallest index that makes `[l...r]` valid. That means `[l...r]` is the longest valid window ending at `r`. Every other candidate `[l+1...r]`, `[l+2...r]`, etc. is strictly shorter — already worse.

**The guarantee:**
- If the true answer ends at index `r`
- Then it's the longest valid substring ending at `r`
- And that's exactly what sliding window keeps

**One-line takeaway:** Sliding window compresses O(n²) candidates into O(n) by keeping only the winner at each endpoint.

---

## Patterns from Problems Solved

### 1. Variable-size window with a validity constraint (set)
**Problem:** Longest Substring Without Repeating Characters

Use when: find the longest/shortest subarray/substring satisfying some constraint.

```
charSet = set()
l = 0
for r in range(len(s)):
    while constraint_violated(s[r], charSet):
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    result = max(result, r - l + 1)
```

- `r` drives the loop (right edge, always moves forward)
- `l` only moves when the window becomes invalid (shrink the minimum amount)
- `l` never moves backwards — past windows are already accounted for
- Window size = `r - l + 1` (inclusive both ends)
- At each `r`: finds the longest valid window ending at that position

**Why it's O(n):** each character is added and removed from the set at most once.
