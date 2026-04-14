# 121. Best Time to Buy and Sell Stock
# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.
# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
# Return the maximum profit you can achieve. You may choose to not make any transactions,
# in which case the profit would be 0.
#
# Example 1:
# Input: prices = [10,1,5,6,7,1]
# Output: 6
# Explanation: Buy prices[1] and sell prices[4], profit = 7 - 1 = 6.
#
# Example 2:
# Input: prices = [10,8,7,5,2]
# Output: 0
# Explanation: No profitable transactions can be made, thus the max profit is 0.
#
# Constraints:
# - 1 <= prices.length <= 100
# - 0 <= prices[i] <= 100

from typing import List

def maxProfit(prices: List[int]) -> int:
    profit = 0
    l, r = 0, 1  # l = buy day (cheapest so far), r = sell day scanning forward

    while r < len(prices):
        if prices[r] > prices[l]:
            # profitable: calculate profit if we sell today
            # l is already the cheapest buy day seen before r, so this is the best
            # possible profit for selling on day r
            curr_profit = prices[r] - prices[l]
            profit = max(curr_profit, profit)
        else:
            # prices[r] <= prices[l]: found a cheaper buy day
            # buying at l can never beat buying at r for any future sell day,
            # so update l to this new minimum
            l = r
        r += 1  # always advance sell pointer — check every possible sell day
    return profit

"""
Approach: Two Pointers marching forward (NOT shrinking from both ends)

Why not start r at the end and shrink inward?
    This problem has an ordering constraint: you must buy BEFORE you sell.
    l < r guarantees order, but there's no greedy rule for inward movement.

    Example — [3, 1, 5, 7], answer is 6:
        l=0(3), r=3(7): profitable (4), move r left
        l=0(3), r=2(5): profitable (2), move r left
        l=0(3), r=1(1): not profitable, move l right
        l=1, r=1: loop ends → returns 4. WRONG.
    No inward movement strategy works because finding a cheaper buy and a
    better sell are independent decisions — you need to scan all sell days
    against the running minimum buy.

Key insight: don't need to compare every pair
    l compresses all previous buy options into one number — the minimum so far.
    Once you find a price cheaper than l, everything before it is irrelevant as
    a buy day. So you're not skipping cases — you're eliminating provably worse ones.

    [10, 1, 5, 6, 7, 1]:
        day 1 (price 1): new minimum → l moves here
        day 2 (price 5): sell? profit = 5-1 = 4
        day 3 (price 6): sell? profit = 6-1 = 5
        day 4 (price 7): sell? profit = 7-1 = 6 ✓
        day 5 (price 1): new minimum → l moves here
    Never needed to check 5 vs 6, 5 vs 7, etc. — buying at 1 always beats buying at 5.

Time:  O(n) — single pass, each element visited once
Space: O(1) — only two pointers and a max variable
"""
