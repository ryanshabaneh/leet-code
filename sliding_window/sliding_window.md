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

### 2. Variable-size window with a frequency constraint + maxFreq trick
**Problem:** Longest Repeating Character Replacement

Use when: you can make at most k changes to a window to make it uniform — find the longest such window.

**Validity check:** `window_length - max_frequency <= k`
- `max_frequency` = count of the most common char in the window
- `window_length - max_frequency` = chars that need replacing

```
count = {}
maxf = 0
l = 0
for r in range(len(s)):
    count[s[r]] = 1 + count.get(s[r], 0)
    maxf = max(maxf, count[s[r]])       # only update upward
    if (r - l + 1) - maxf > k:         # window invalid: slide, don't shrink
        count[s[l]] -= 1
        l += 1
    res = max(res, r - l + 1)
```

**Key insight — why maxf never decreases:**
- `res = maxf + k` at best. k is fixed, so the only way to grow res is to grow maxf.
- If maxf would drop after sliding, leave it — a lower maxf can't beat the current best.
- This means the window either grows (maxf goes up) or slides at the same size (maxf stays).
- Avoids calling `max(count.values())` each step — O(1) per iteration instead of O(26).

**Why sliding by 1 is always enough:** the window was valid before r was added. Adding r grows it by 1, so it can only be off by 1. One slide restores it.

### 3. Variable-size window — shrink when valid (find minimum)
**Problem:** Minimum Window Substring

Use when: find the *shortest* window satisfying a condition. Opposite of the longest pattern — here you expand until valid, then greedily shrink.

**Validity:** `have == need`
- `need` = number of distinct chars in t
- `have` = number of those chars whose count is satisfied in the current window
- A condition is satisfied when `window[c] >= countT[c]` (extras are fine)

```
countT = {}
for c in t: countT[c] = 1 + countT.get(c, 0)

have, need = 0, len(countT)
res, resLen = [-1, -1], float("infinity")
window = {}
l = 0

for r in range(len(s)):
    window[s[r]] = 1 + window.get(s[r], 0)
    if s[r] in countT and window[s[r]] == countT[s[r]]:
        have += 1
    while have == need:              # valid — shrink from left
        if (r - l + 1) < resLen:
            resLen, res = r - l + 1, [l, r]
        window[s[l]] -= 1
        if s[l] in countT and window[s[l]] < countT[s[l]]:
            have -= 1                # condition broken
        l += 1

l, r = res
return s[l:r+1] if resLen != float("infinity") else ""
```

**Key details:**
- Use `<` not `!=` when checking if removing s[l] broke a condition — having extras (window > countT) is still valid, only going below breaks it.
- `need = len(countT)` not `len(t)` — conditions are per distinct char, duplicates count toward frequency not condition count.
