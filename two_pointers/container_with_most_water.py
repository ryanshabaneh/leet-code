# 11. Container With Most Water
# You are given an integer array heights where heights[i] represents the height of the ith bar.
# You may choose any two bars to form a container.
# Return the maximum amount of water a container can store.
#
# Example 1:
# Input: height = [1,7,2,5,4,7,3,6]
# Output: 36
#
# Example 2:
# Input: height = [2,2,2]
# Output: 4
#
# Constraints:
# - 2 <= height.length <= 1000
# - 0 <= height[i] <= 1000

def max_area(heights: List[int]) -> int:
    l, r = 0, len(heights) - 1  # start at both ends — maximizes width on the first check
    res = 0

    while l < r:
        # area = width × height
        # width  = r - l (distance between the two bars)
        # height = min(heights[l], heights[r]) — water spills over the shorter bar
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)

        # KEY INSIGHT: always move the shorter pointer inward
        # Moving the taller pointer inward: width shrinks AND height cap stays the same
        # or gets worse — can never improve. So it's pointless.
        # Moving the shorter pointer inward: width shrinks but there's at least a CHANCE
        # of finding a taller bar that increases the area.
        # If equal, it doesn't matter which we move — both are the same height cap,
        # width shrinks either way, and the other will get skipped on the next iteration.
        # Move l by convention.
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1

    return res

"""
Approach: Two Pointers from both ends

The area formula is: min(heights[l], heights[r]) * (r - l)
We want to maximize this product of two competing terms:
    - (r - l): always decreasing as pointers move inward — out of our control
    - min(heights[l], heights[r]): we can influence this by choosing which pointer to move

Why start at the edges?
    Starting at l=0, r=n-1 gives the maximum possible width. From there we only
    move inward, so we check every width from largest to smallest — guaranteed not
    to miss the optimal pair.

Why move the shorter pointer?
    Moving the taller pointer inward:
        - width decreases (always)
        - height is still capped at the shorter bar (unchanged or worse)
        → strictly worse or equal, never better

    Moving the shorter pointer inward:
        - width decreases (always)
        - height cap MIGHT increase if we find a taller bar
        → the only way to possibly improve area

    So moving the taller pointer is provably never optimal — always move the shorter one.

Why does this not miss the optimal answer?
    For any pair (i, j) that is optimal, when l=i the only reason we'd skip to l=i+1
    is if heights[i] <= heights[j], meaning heights[i] was the shorter bar. But then
    every pair (i, k) for k < j has smaller width and the same or worse height — none
    of them can beat (i, j). So skipping i is safe.

Time:  O(n) — each pointer moves at most n times total
Space: O(1) — only two pointers and a max variable
"""
        
    
    
