#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
# TAGS: Dynamic Programming
from typing import List


class Solution:
    # 60 ms, 84.22% Greedy. Time: O(N). Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        start = prices[0]
        total = 0
        for price in prices[1:]:
            if price < start:
                start = price
            else:
                total = max(total, price - start)
        return total

    # DP or cumulative min. Time: O(N). Space: O(1)
    def maxProfit(self, prices: List[int]) -> int:
        buy = ans = 0
        for price in prices:
            buy = min(buy, price)
            ans = max(ans, price - buy)
        return ans
# @lc code=end
