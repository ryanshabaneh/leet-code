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

*More patterns coming as problems are solved (3Sum, Container With Most Water, ...)*
