#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#

# @lc code=start
# TAGS: Array, Dynamic Programming, Greedy
# REVIEWME: Array, Dynamic Programming, Greedy


class Solution:
    # 704 ms, 66.85%. Time: O(N). Space: O(1)
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # 1    3    2    8    4   9
        # -1   -1   -1   -1   1
        # 0    0    0    5    5   8
        with_stock = float("-inf")
        no_stock = 0
        for p in prices:
            old_stock = with_stock
            with_stock = max(with_stock, no_stock - p)
            no_stock = max(no_stock, old_stock + p - fee)
        return no_stock
# @lc code=end
