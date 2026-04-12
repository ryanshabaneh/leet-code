# Sliding Window

A technique where you maintain a window (a subarray or substring) defined by two pointers `l` and `r`, and slide it across the input. Instead of recomputing the result from scratch each time, you add the new element on the right and remove the old element on the left — keeping the computation O(n) instead of O(n²).

Use it when the problem asks about a contiguous subarray or substring that satisfies some condition (max sum, longest without repeats, etc.).

---

## Patterns from Problems Solved

